# Exercício 10.4 — FastAPI, Docker e Deploy

Este projeto consiste em uma API RESTful desenvolvida com **FastAPI**, containerizada com **Docker** e publicada na nuvem utilizando **Azure App Service**.  
Também foi configurado um pipeline de **CI/CD com GitHub Actions** para realizar o deploy automático a partir do GitHub.

## Link da aplicação

https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/

## Documentação da API

https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/docs

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Docker
- Azure App Service
- GitHub Actions
- Postman

## Funcionalidades da API

A API permite realizar operações CRUD de tarefas:

- Listar tarefas
- Buscar tarefa por ID
- Criar nova tarefa
- Atualizar tarefa existente
- Remover tarefa

## Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Página inicial da API |
| GET | `/api/tasks` | Lista todas as tarefas |
| GET | `/api/tasks/{task_id}` | Busca uma tarefa pelo ID |
| POST | `/api/tasks` | Cria uma nova tarefa |
| PUT | `/api/tasks/{task_id}` | Atualiza uma tarefa existente |
| DELETE | `/api/tasks/{task_id}` | Remove uma tarefa |

## Exemplo de requisição POST

Endpoint:

```http
POST /api/tasks

Body JSON:

{
  "titulo": "Testar API na nuvem",
  "status": "Pendente"
}

Resposta esperada:

{
  "id": 3,
  "titulo": "Testar API na nuvem",
  "status": "Pendente"
}
Como executar localmente

Instale as dependências:

pip install -r requirements.txt

Execute a aplicação:

uvicorn main:app --reload

Acesse no navegador:

http://localhost:8000

Documentação local:

http://localhost:8000/docs
Como executar com Docker

Crie a imagem Docker:

docker build -t api-fastapi-104 .

Execute o container:

docker run -d -p 8000:8000 --name container-api-104 api-fastapi-104

Acesse:

http://localhost:8000

Documentação:

http://localhost:8000/docs
Estrutura do projeto
.
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
Deploy

A aplicação foi publicada no Azure App Service.

O deploy automático foi configurado utilizando GitHub Actions, permitindo que alterações enviadas para a branch principal do repositório sejam implantadas automaticamente na aplicação hospedada na nuvem.

Testes com Postman

A API foi testada utilizando o Postman com os seguintes endpoints:

GET https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/
GET https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/api/tasks
GET https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/api/tasks/1
POST https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/api/tasks
PUT https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/api/tasks/1
DELETE https://exercicio104-fastapi-duapexfhh4cqb0df.eastus-01.azurewebsites.net/api/tasks/1
