from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from typing import List
from src.schemas.fibonacci_models import FibonacciRequest

api_fibonacci = APIRouter()

@api_fibonacci.post("/fibonacci", response_model=List[int], summary="Calcula a sequência de Fibonacci", description="Essa rota calcula os n primeiros números da sequência de Fibonacci e retorna numa lista.")
async def fibonacci_sequence(request: FibonacciRequest):
    try:
        response = request.calculate_fibonacci()
        return response
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve), 
                            headers={"error": "Valor inválido"},
                            description="O valor de 'n' deve ser maior que zero.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")