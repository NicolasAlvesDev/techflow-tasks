import pytest

from src.app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_crud_flow(client):
    res = client.post("/api/tasks", json={"title": "Entrega rastreada"})
    assert res.status_code == 201
    task_id = res.get_json()["id"]

    assert client.get(f"/api/tasks/{task_id}").status_code == 200
    assert len(client.get("/api/tasks").get_json()) == 1

    res = client.put(f"/api/tasks/{task_id}", json={"status": "doing"})
    assert res.get_json()["status"] == "doing"

    assert client.delete(f"/api/tasks/{task_id}").status_code == 204
    assert client.get(f"/api/tasks/{task_id}").status_code == 404


def test_create_without_title_returns_400(client):
    res = client.post("/api/tasks", json={})
    assert res.status_code == 400
    assert "título" in res.get_json()["error"].lower()


def test_index_page(client):
    assert client.get("/").status_code == 200


def test_stats_endpoint(client):
    client.post("/api/tasks", json={"title": "A", "priority": "critical"})
    client.post("/api/tasks", json={"title": "B", "status": "done"})
    data = client.get("/api/stats").get_json()
    assert data["total"] == 2
    assert data["open_critical"] == 1
    assert data["completion_rate"] == 50.0


def test_invalid_priority_returns_400(client):
    res = client.post("/api/tasks", json={"title": "A", "priority": "xyz"})
    assert res.status_code == 400
