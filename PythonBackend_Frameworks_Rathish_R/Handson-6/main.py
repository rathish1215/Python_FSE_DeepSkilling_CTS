from fastapi import FastAPI
from app.database import engine, Base
from app.routers.course import router

app = FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "API running"}


app.include_router(router)