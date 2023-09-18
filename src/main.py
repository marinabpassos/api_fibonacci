from fastapi import FastAPI

from src.routes import fibonacci, health

app = FastAPI(
    title="API de Fibonacci",
    description="API usada como exercício para code review, onde retornamos a sequência de Fibonacci até o n-ésimo número",
    version="1"
)

@app.get("/")
def read_root():
    return {"Hello": "API"}

app.include_router(health.api_health, prefix="/api")
app.include_router(fibonacci.api_fibonacci, prefix="/api")
