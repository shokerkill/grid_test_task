from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Scenario Generator API",
    version="1.0.0",
)

app.include_router(router, prefix="/v1/scenarios")