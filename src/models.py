"""Modelo de domínio e repositório de tarefas (armazenamento em memória)."""
from dataclasses import dataclass, asdict

from .validators import validate_title, validate_status


@dataclass
class Task:
    """Uma tarefa do quadro Kanban."""
    id: int
    title: str
    description: str = ""
    status: str = "todo"

    def to_dict(self):
        return asdict(self)


class TaskRepository:
    """Operações CRUD de tarefas."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def create(self, title, description="", status="todo"):
        """Create: cria e armazena uma nova tarefa."""
        task = Task(
            id=self._next_id,
            title=validate_title(title),
            description=description or "",
            status=validate_status(status),
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id):
        """Read: devolve uma tarefa ou None."""
        return self._tasks.get(task_id)

    def list(self):
        """Read: lista todas as tarefas por ordem de criação."""
        return list(self._tasks.values())

    def update(self, task_id, **fields):
        """Update: altera campos de uma tarefa existente (None se não existir)."""
        task = self._tasks.get(task_id)
        if task is None:
            return None
        if "title" in fields:
            task.title = validate_title(fields["title"])
        if "description" in fields:
            task.description = fields["description"] or ""
        if "status" in fields:
            task.status = validate_status(fields["status"])
        return task

    def delete(self, task_id):
        """Delete: remove a tarefa. Retorna True se existia."""
        return self._tasks.pop(task_id, None) is not None
