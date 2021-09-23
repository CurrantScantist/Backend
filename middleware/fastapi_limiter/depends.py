# @ Used Code from https://github.com/long2ice/fastapi-limiter

from typing import Callable, Optional
from pydantic import conint
from starlette.requests import Request
from starlette.responses import Response
from middleware.fastapi_limiter import FastAPILimiter


   
class RateLimiter:
    def __init__(
        self,
        times: conint(ge=0) = 1,
        milliseconds: conint(ge=-1) = 0,
        seconds: conint(ge=-1) = 0,
        minutes: conint(ge=-1) = 0,
        hours: conint(ge=-1) = 0,
        identifier: Optional[Callable] = None,
        callback: Optional[Callable] = None,
    ):
        self.times = times
        self.milliseconds = milliseconds + 1000 * seconds + 60000 * minutes + 3600000 * hours
        self.identifier = identifier
        self.callback = callback
  

    async def __call__(self, request: Request, response: Response):
        if not FastAPILimiter.redis:
            raise Exception("You must call FastAPILimiter.init in startup event of fastapi!")
        index = 0
        for route in request.app.routes:
            if route.path == request.scope["path"]:
                for idx, dependency in enumerate(route.dependencies):
                    if self is dependency.dependency:
                        index = idx
                        break
        # moved here because constructor run before app startup
        identifier = self.identifier or FastAPILimiter.identifier
        callback = self.callback or FastAPILimiter.callback
        redis = FastAPILimiter.redis
        rate_key = await identifier(request)
    
        key = f"{rate_key}:{index}"
      
        check_key = await redis.evalsha(FastAPILimiter.lua_check_key_script_sha, 1, key)
        # print(check_key)
        # new ip address will return 0 and registred ip will return 1
        
        if check_key == 0:
            # print("new")
            whitelisted_ips = await FastAPILimiter.ip_collection_from_db.getListOfWhiteListedIp()
            # print(whitelisted_ips)
            whitelisted_ip_access_time = 10
            whitelisted_ip_access_second = 1000 * 50
            ip_address =  rate_key.split(":")[0]
            # print(ip_address)
            ip_check = ip_address in whitelisted_ips
            if (ip_check):
                # print("ip_check_success")
                pexpire = await redis.evalsha(FastAPILimiter.lua_sha, 1, "x"+key, whitelisted_ip_access_time, whitelisted_ip_access_second)
            else:
                pexpire = await redis.evalsha(FastAPILimiter.lua_sha, 1, key, self.times, self.milliseconds)
            # print(pexpire)
            if pexpire > 0:
                return await callback(request, response, pexpire)
        else:
            # pexpire --> non-blocked ip would return 0 and blocked ip will return expiration time in seconds
            pexpire = await redis.evalsha(FastAPILimiter.lua_sha, 1, key, self.times, self.milliseconds)
            if pexpire > 0:
                return await callback(request, response, pexpire)
            # print("non-listed")
            # print(pexpire)
