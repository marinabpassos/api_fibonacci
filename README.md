# API Fibonacci

Esta é uma API FastAPI que fornece a sequência de Fibonacci. Ela foi feita como exercício para code review.

## Instalação

1. Clone este repositório:


## Uso

### Usando a imagem Docker
Você pode usar a imagem Docker desta API para executá-la em um contêiner. Certifique-se de ter o Docker instalado. Esse é o jeito mais simples de usar a API!

1) Execute o comando de compose para construir e iniciar o contâiner:  
(O docker deve já estar instalado em sua máquina)
docker compose up --build

A API estará disponível em http://localhost:8000 dentro do contâiner (http://localhost:8000/docs para acessar o Swagger)

Para desativar o uvicorn a qualquer momento, use Ctrl + C

### Executando a API localmente
1. Ative ambiente virtual (recomendado):  
.venv/bin/activate 
(use o script de activate de acordo com seu sistema operacional. Para Windows usar o .venv\Scripts\Activate.ps1 no PowerShell)

2. Instale as dependências:
pip install -r requirements.txt

Para iniciar o servidor da API, você pode usar o Uvicorn:  
uvicorn src.main:app --reload

A API estará disponível em no caminho que aparecerá no seu terminal (normalmente http://127.0.0.1:8000).
O Swagger estará nesse caminho /docs

### Executando teste
Com o venv ativado use o comando
pytest tests/test_fibonaccy.py

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
