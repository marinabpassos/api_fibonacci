from fastapi import FastAPI

from src.routes import fibonacci, health

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "API"}

app.include_router(health.api_health, prefix="/api")
app.include_router(fibonacci.api_fibonacci, prefix="/api")
