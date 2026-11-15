from src.models import TaskRepository


def test_create_and_get():
    repo = TaskRepository()
    task = repo.create("Planejar sprint")
    assert task.id == 1
    assert repo.get(1).title == "Planejar sprint"
    assert task.status == "todo"


def test_list_keeps_creation_order():
    repo = TaskRepository()
    repo.create("A")
    repo.create("B")
    assert [t.title for t in repo.list()] == ["A", "B"]


def test_update_status():
    repo = TaskRepository()
    repo.create("A")
    assert repo.update(1, status="done").status == "done"


def test_update_missing_returns_none():
    assert TaskRepository().update(99, title="X") is None


def test_delete():
    repo = TaskRepository()
    repo.create("A")
    assert repo.delete(1) is True
    assert repo.delete(1) is False
