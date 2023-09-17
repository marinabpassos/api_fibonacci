from fastapi import APIRouter

api_health = APIRouter()

@api_health.get("/health", summary="Verifica a saúde da API", description="Verifica se a API está saudável e pronta para uso.")
async def check_health():
    return {"status": "API está saudável!"}