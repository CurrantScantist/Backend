from fastapi import FastAPI
from server.routes.techstack import router as TechstackRouter # Wiring up the techstack route in app/server/app.py
from server.routes.release import router as ReleaseRouter # Wiring up the techstack route in app/server/app.py
from server.routes.sca import router as SCARouter # Wiring up the techstack route in app/server/app.py
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
app.include_router(SCARouter, tags=["sca_data"], prefix="/sca_data")
# Tags are identifiers used to group routes. Routes with the same tags are grouped into a section on the API documentation.

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Currant Scantist Backend Services!"}