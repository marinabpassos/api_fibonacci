from pydantic import BaseModel, validator

class FibonacciRequest(BaseModel):
    """Modelo para o request do post da sequência de Fibonacci
    O número n deve ser um inteiro maior que 0. """
    n: int

    @validator("n")
    @classmethod
    def check_positive(cls,value):
        """Verifica se n é maior que zero"""
        if value <= 0:
            raise ValueError("É esperado um número maior que 0.")
        return value
    
    def calculate_fibonacci(self):
        n = self.n
        sequence = [0,1]
        if n <= 2:
            return sequence[:n]
        else:
            while len(sequence) < n:
                sequence.append(sequence[-1] + sequence[-2])
            return sequence[:n]