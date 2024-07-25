import json

import pytest

from handlers.task_handler import create, toggle, remove, list_tasks
from repositories.boto_task_repository import BotoTaskRepository
from usecases.create_task.create_task_usecase import CreateTaskUseCase
from usecases.remove_task.remove_task_usecase import RemoveTaskUseCase

task_repository = BotoTaskRepository()
create_task_usecase = CreateTaskUseCase(task_repository)
remove_task_usecase = RemoveTaskUseCase(task_repository)


def test_it_should_be_able_to_create_a_task():
    event = {
        "body": json.dumps({
            "description": "study japanese",
        })
    }
    response = create(event, None)
    assert response.get("statusCode") == 201
    remove_task_usecase.execute({
        "task_id": json.loads(response["body"])["task_id"]
    })


def test_it_should_be_able_to_list_tasks():
    created_task = create_task_usecase.execute({
        "description": "work out", "done": False
    })
    response = list_tasks({}, None)
    assert response.get("statusCode") == 200

    loaded_body = json.loads(response.get("body"))
    assert len(loaded_body["data"]) == 1
    remove_task_usecase.execute({"task_id": created_task["task_id"]})


def test_it_should_be_able_to_toggle_a_task():
    created_task = create_task_usecase.execute({
        "description": "work out", "done": False
    })
    event = {
        "pathParameters": {
            "task_id": created_task["task_id"],
        }
    }
    response = toggle(event, None)
    assert response.get("statusCode") == 204
    remove_task_usecase.execute({"task_id": created_task["task_id"]})


def test_it_should_be_able_to_remove_a_task():
    created_task = create_task_usecase.execute({
        "description": "work out", "done": False
    })
    event = {
        "pathParameters": {
            "task_id": created_task["task_id"],
        }
    }
    response = remove(event, None)
    assert response.get("statusCode") == 204


if __name__ == "__main__":
    pytest.main()
