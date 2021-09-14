from fastapi import FastAPI
from starlette.requests import Request
from server.routes.techstack import router as TechstackRouter # Wiring up the techstack route in app/server/app.py
from server.routes.release import router as ReleaseRouter # Wiring up the techstack route in app/server/app.py
from fastapi.middleware.cors import CORSMiddleware
import aioredis
from fastapi import Depends

from middleware.fastapi_limiter import FastAPILimiter
from middleware.fastapi_limiter.depends import RateLimiter


app = FastAPI()

origins = ["http://119.181.73:8083", "https://119.181.73:8083"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TechstackRouter, tags=["Techstack"], prefix="/techstack", dependencies=[Depends(RateLimiter(times=2, seconds=500))])
app.include_router(ReleaseRouter, tags=["Release"], prefix="/release", dependencies=[Depends(RateLimiter(times=2, seconds=500))])
# Tags are identifiers used to group routes. Routes with the same tags are grouped into a section on the API documentation.

@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)

@app.get("/", tags=["Root"], dependencies=[Depends(RateLimiter(times=2, seconds=500))])
async def read_root(request: Request):
    return {"message": "Welcome to this fantastic app!"}