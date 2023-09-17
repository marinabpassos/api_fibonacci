from fastapi import FastAPI

from src.routes.fibonacci import api_fibonacci

app = FastAPI()
#api.include_router(api_health, prefix="/api")
app.include_router(api_fibonacci, prefix="/fibonacci")
