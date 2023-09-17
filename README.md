# API Fibonacci

Esta é uma API FastAPI que fornece a sequência de Fibonacci.

## Instalação

1. Clone este repositório:

2. Crie um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate


3. Instale as dependências:
pip install -r requirements.txt


## Uso

### Executando a API

Para iniciar o servidor da API, você pode usar o Uvicorn:
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload



A API estará disponível em `http://localhost:8000`.

### Rota Fibonacci

- **URL**: `api/fibonacci`
- **Método**: POST
- **Descrição**: Calcula a sequência de Fibonacci com base no número fornecido.
- **Parâmetros do corpo (JSON)**:
  - `n` (int): Número de elementos desejados na sequência de Fibonacci. Deve ser um número positivo maior que zero.
- **Exemplo de solicitação**:
  ```json
  {"n": 5}
- **Exemplo de resposta**:
[0, 1, 1, 2, 3]



### Rota Health Check
- **URL**: `api/health`
- **Método**: GET
- **Descrição**:Verifica se a API está saudável e pronta para uso.
- **Exemplo de resposta**:
{"status": "API está saudável"}


### Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.