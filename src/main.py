from fastapi import FastAPI

from src.routes import fibonacci, health

app = FastAPI()

app.include_router(health.api_health, prefix="/health")
app.include_router(fibonacci.api_fibonacci, prefix="/fibonacci")
