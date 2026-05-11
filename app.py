from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {'id': 1, 'titulo': 'Aprender Flask', 'status': 'Em progresso'},
    {'id': 2, 'titulo': 'Criar API REST', 'status': 'Pendente'}
]


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((item for item in tasks if item['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404


@app.route('/api/tasks', methods=['POST'])
def create_task():
    dados = request.get_json()

    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'O campo titulo é obrigatório'}), 400

    nova_tarefa = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'titulo': dados.get('titulo'),
        'status': dados.get('status', 'Pendente')
    }
    tasks.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((item for item in tasks if item['id'] == task_id), None)
    if not task:
        return jsonify({'erro': 'Tarefa não encontrada'}), 404

    dados = request.get_json()
    task['titulo'] = dados.get('titulo', task['titulo'])
    task['status'] = dados.get('status', task['status'])

    return jsonify(task), 200


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((item for item in tasks if item['id'] == task_id), None)
    if not task:
        return jsonify({'erro': 'Tarefa não encontrada'}), 404

    tasks = [item for item in tasks if item['id'] != task_id]
    return jsonify({'mensagem': 'Tarefa removida com sucesso'}), 200


if __name__ == '__main__':
    app.run(debug=True)