from fastapi import APIRouter

api_health = APIRouter()

@api_health.get("/health")
async def check_health():
    return "API está saudável!"