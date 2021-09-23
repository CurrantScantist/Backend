# @ Used Code from https://github.com/long2ice/fastapi-limiter

from math import ceil
from typing import Callable
import aioredis
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from middleware.fastapi_limiter import database
import os
from dotenv import load_dotenv


async def default_identifier(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = request.client.host
    print(ip + ":" + request.scope["path"])
    return ip + ":" + request.scope["path"]


async def default_callback(request: Request, response: Response, pexpire: int):
    """
    default callback when too many requests
    :param request:
    :param pexpire: The remaining milliseconds
    :param response:
    :return:
    """
    expire = ceil(pexpire / 1000)
    print(expire)
    raise HTTPException(
        HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
    )
def connect_to_database():
    load_dotenv()
    PASSWORD = os.getenv('PASSWORD')
    USERNAME = os.getenv('NAME')
    DB_NAME = "development"
    collection_name = "developers_ip"
    CONNECTION_STRING = f"mongodb+srv://{USERNAME}:" \
                        f"{PASSWORD}@cluster0.vao3k.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

    return database.DatabaseConnection(CONNECTION_STRING, DB_NAME, collection_name)

class FastAPILimiter:
    redis: aioredis.Redis = None
    prefix: str = None
    lua_sha: str = None
    lua_check_key_script_sha: str = None
    identifier: Callable = None
    ip_collection_from_db: Callable =None
    callback: Callable = None
    lua_check_key_script = """local key = KEYS[1]
local current = tonumber(redis.call('get', key) or -1)
local newKey = "x" ..key
local current = tonumber(redis.call('get', key) or "0")
local currentx = tonumber(redis.call('get', newKey) or "0")

if (currentx > 0 or current > 0) then
    return 1
else
    return 0
end"""
    lua_script = """local key = KEYS[1]
local limit = tonumber(ARGV[1])
local expire_time = ARGV[2]
local newKey = "x" ..key
local current = tonumber(redis.call('get', key) or "0")
local currentx = tonumber(redis.call('get', newKey) or "0")

if (string.sub(key, 1, 1) == "x" or currentx > 0 ) then
    if (current <= 0) then
        redis.call("SET", key, 1,"px",expire_time)
        return 0
    end
  return redis.call("PTTL",newKey)  
end
if current > 0 then
 if current + 1 > limit then
 return redis.call("PTTL",key)
 else
        redis.call("INCR", key)
 return 0
 end
else
    redis.call("SET", key, 1,"px",expire_time)
 return 0
end"""

    @classmethod
    async def init(
        cls,
        redis: aioredis.Redis,
        prefix: str = "fastapi-limiter",
        identifier: Callable = default_identifier,
        callback: Callable = default_callback,
    ):
        cls.redis = redis
        cls.prefix = prefix
        cls.identifier = identifier
        cls.callback = callback
        cls.lua_sha = await redis.script_load(cls.lua_script)
        cls.lua_check_key_script_sha= await redis.script_load(cls.lua_check_key_script)
        cls.ip_collection_from_db = connect_to_database() 

    @classmethod
    async def close(cls):
        cls.redis.close()
        await cls.redis.wait_closed()



