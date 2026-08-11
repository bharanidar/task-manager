from app import app


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "assigned_role": "Developer"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test task"
    assert data["assigned_role"] == "Developer"
    assert data["status"] == "pending"


def test_update_task():
    client = app.test_client()

    create_response = client.post(
        "/tasks",
        json={
            "title": "Task to update",
            "assigned_role": "Tester"
        }
    )

    task_id = create_response.get_json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"status": "completed"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "completed"