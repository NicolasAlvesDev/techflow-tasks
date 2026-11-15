"""API REST + página web do sistema de tarefas (Flask)."""
from flask import Flask, jsonify, request, render_template

from .models import TaskRepository
from .validators import ValidationError


def create_app(repository=None):
    """Fábrica da aplicação; recebe um repositório para facilitar os testes."""
    app = Flask(__name__)
    repo = repository or TaskRepository()

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify(error=str(error)), 400

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/tasks")
    def list_tasks():
        return jsonify([t.to_dict() for t in repo.list()])

    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        task = repo.create(
            data.get("title"),
            data.get("description", ""),
            data.get("status", "todo"),
            data.get("priority", "medium"),
        )
        return jsonify(task.to_dict()), 201

    @app.get("/api/stats")
    def stats():
        return jsonify(repo.stats())

    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id):
        task = repo.get(task_id)
        if task is None:
            return jsonify(error="Tarefa não encontrada."), 404
        return jsonify(task.to_dict())

    @app.put("/api/tasks/<int:task_id>")
    def update_task(task_id):
        data = request.get_json(silent=True) or {}
        task = repo.update(task_id, **data)
        if task is None:
            return jsonify(error="Tarefa não encontrada."), 404
        return jsonify(task.to_dict())

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        if not repo.delete(task_id):
            return jsonify(error="Tarefa não encontrada."), 404
        return "", 204

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
