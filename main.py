from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API RESTful de Tarefas",
    description="API baseada no exemplo em Flask, implementada com FastAPI.",
    version="1.0.0"
)

tasks = [
    {"id": 1, "titulo": "Aprender Flask", "status": "Em progresso"},
    {"id": 2, "titulo": "Criar API REST", "status": "Pendente"}
]


class TaskCreate(BaseModel):
    titulo: str
    status: Optional[str] = "Pendente"


class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    status: Optional[str] = None


@app.get("/")
def home():
    return {
        "mensagem": "API RESTful de Tarefas com FastAPI",
        "rotas": {
            "listar_tarefas": "/api/tasks",
            "documentacao": "/docs"
        }
    }


@app.get("/api/tasks", status_code=status.HTTP_200_OK)
def get_tasks():
    return {"tasks": tasks}


@app.get("/api/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    task = next((item for item in tasks if item["id"] == task_id), None)

    if task:
        return task

    return JSONResponse(
        content={"erro": "Tarefa não encontrada"},
        status_code=status.HTTP_404_NOT_FOUND
    )


@app.post("/api/tasks", status_code=status.HTTP_201_CREATED)
def create_task(dados: TaskCreate):
    nova_tarefa = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "titulo": dados.titulo,
        "status": dados.status
    }

    tasks.append(nova_tarefa)
    return nova_tarefa


@app.put("/api/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, dados: TaskUpdate):
    task = next((item for item in tasks if item["id"] == task_id), None)

    if not task:
        return JSONResponse(
            content={"erro": "Tarefa não encontrada"},
            status_code=status.HTTP_404_NOT_FOUND
        )

    if dados.titulo is not None:
        task["titulo"] = dados.titulo

    if dados.status is not None:
        task["status"] = dados.status

    return task


@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    global tasks

    task = next((item for item in tasks if item["id"] == task_id), None)

    if not task:
        return JSONResponse(
            content={"erro": "Tarefa não encontrada"},
            status_code=status.HTTP_404_NOT_FOUND
        )

    tasks = [item for item in tasks if item["id"] != task_id]

    return {"mensagem": "Tarefa removida com sucesso"}