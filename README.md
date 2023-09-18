# API Fibonacci

Esta é uma API FastAPI que fornece a sequência de Fibonacci.

## Instalação

1. Clone este repositório:

2. Crie um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate (use o script de activate de acordo com seu sistema operacional. Para Windows usar o Activate.ps1 no PowerShell)


3. Instale as dependências:
pip install -r requirements.txt


## Uso

### Executando a API localmente

Para iniciar o servidor da API, você pode usar o Uvicorn:
uvicorn src.main:app --reload



A API estará disponível em no caminho que aparecerá no seu terminal (normalmente http://127.0.0.1:8000).
O Swagger estará nesse caminho /docs

### Usando a imagem Docker
Você pode usar a imagem Docker desta API para executá-la em um contêiner. Certifique-se de ter o Docker instalado.
1) Execute o comando de compose para construir e iniciar o contâiner:
docker compose up --build

A API estará disponível em http://localhost:8000 dentro do contâiner (http://localhost:8000/docs para acessar o Swagger)
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