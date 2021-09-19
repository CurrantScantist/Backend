from fastapi import FastAPI
from server.routes.techstack import router as TechstackRouter # Wiring up the techstack route in app/server/app.py
from server.routes.release import router as ReleaseRouter # Wiring up the techstack route in app/server/app.py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TechstackRouter, tags=["Techstack"], prefix="/techstack")
app.include_router(ReleaseRouter, tags=["Release"], prefix="/release")
# Tags are identifiers used to group routes. Routes with the same tags are grouped into a section on the API documentation.

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}