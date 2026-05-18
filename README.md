# API RESTful de Tarefas com FastAPI

Projeto baseado em uma API Flask, reimplementado com FastAPI.

## Como executar no PyCharm

1. Abra esta pasta no PyCharm.
2. Abra o terminal do PyCharm.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a API com Uvicorn:

```bash
uvicorn main:app --reload
```

5. Acesse no navegador:

```text
http://127.0.0.1:8000
```

## Rotas da API

### Listar tarefas

```http
GET /api/tasks
```

### Buscar tarefa por ID

```http
GET /api/tasks/1
```

### Criar tarefa

```http
POST /api/tasks
```

Exemplo de JSON:

```json
{
  "titulo": "Estudar FastAPI",
  "status": "Pendente"
}
```

### Atualizar tarefa

```http
PUT /api/tasks/1
```

Exemplo de JSON:

```json
{
  "titulo": "Aprender FastAPI",
  "status": "Concluído"
}
```

### Remover tarefa

```http
DELETE /api/tasks/1
```

## Documentação automática

Acesse:

```text
http://127.0.0.1:8000/docs
```

## Prints para entrega

Inclua no trabalho:

1. Print do PyCharm com o terminal executando:

```bash
uvicorn main:app --reload
```

2. Print do navegador acessando:

```text
http://127.0.0.1:8000
```

3. Print do navegador acessando:

```text
http://127.0.0.1:8000/api/tasks
```

ou:

```text
http://127.0.0.1:8000/docs
```

## Subir no GitHub

```bash
git init
git add .
git commit -m "API RESTful com FastAPI"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/api-fastapi-tarefas.git
git push -u origin main
```
