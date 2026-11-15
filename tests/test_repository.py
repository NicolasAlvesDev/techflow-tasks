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


def test_default_priority_is_medium():
    assert TaskRepository().create("A").priority == "medium"


def test_stats_counts_and_completion_rate():
    repo = TaskRepository()
    repo.create("A", priority="critical")
    repo.create("B", status="done")
    repo.create("C", status="doing", priority="critical")
    repo.create("D", status="done", priority="critical")
    stats = repo.stats()
    assert stats["total"] == 4
    assert stats["by_status"] == {"todo": 1, "doing": 1, "done": 2}
    assert stats["completion_rate"] == 50.0
    assert stats["open_critical"] == 2


def test_stats_empty_repository():
    assert TaskRepository().stats()["completion_rate"] == 0.0
