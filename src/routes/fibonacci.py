from fastapi import APIRouter, Request
from typing import List
from src.schemas.fibonacci_models import FibonacciRequest

api_fibonacci = APIRouter()

@api_fibonacci.post("/fibonacci", response_model=List[int])
async def fibonacci_sequence(request: FibonacciRequest):
    try:
        n = request.n
        if n <= 0:
            raise HTTPException(status_code=400, detail="O valor de 'n' deve ser maior que zero.")

        sequence = [0, 1]
        if n <= 2:
            return sequence[:n]
        else:
            while len(sequence) < n:
                sequence.append(sequence[-1] + sequence[-2])
            return sequence[:n]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
