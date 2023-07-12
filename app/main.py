from fastapi import FastAPI
from app.routers import files_router

app = FastAPI()

app.include_router(files_router)


@app.get("/health")
async def root() -> dict:
    return {"status": "ok"}

