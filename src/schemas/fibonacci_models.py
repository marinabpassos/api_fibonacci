from pydantic import BaseModel, validator

class FibonacciRequest(BaseModel):
    """Modelo para o request do post da sequência de Fibonacci"""
    n: int

    @validator("n")
    @classmethod
    def check_positive(cls,value):
        """Verifica se n é maior que zero"""
        if value <= 0:
            raise ValueError("É esperado um número positivo.")
        return value
    