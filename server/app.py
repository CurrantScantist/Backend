from fastapi import FastAPI
from server.routes.techstack import router as TechstackRouter # Wiring up the techstack route in app/server/app.py

app = FastAPI()

app.include_router(TechstackRouter, tags=["Techstack"], prefix="/techstack")
# Tags are identifiers used to group routes. Routes with the same tags are grouped into a section on the API documentation.

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

