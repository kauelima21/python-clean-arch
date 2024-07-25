import json
import logging

from repositories.boto_task_repository import BotoTaskRepository
from usecases.create_task.create_task_usecase import CreateTaskUseCase
from usecases.list_tasks.list_tasks_usecase import ListTasksUseCase
from usecases.remove_task.remove_task_usecase import RemoveTaskUseCase
from usecases.toggle_task.toggle_task_usecase import ToggleTaskUseCase
from utils.event import http_response

logging.getLogger().setLevel(logging.INFO)

task_repository = BotoTaskRepository()
create_task_usecase = CreateTaskUseCase(task_repository)
list_tasks_usecase = ListTasksUseCase(task_repository)
toggle_task_usecase = ToggleTaskUseCase(task_repository)
remove_task_usecase = RemoveTaskUseCase(task_repository)


def create(event, _):
    logging.info(f"event -> {event}")

    try:
        body = json.loads(event["body"])
        request = {"description": body["description"], "done": False}
        created_task = create_task_usecase.execute(request)

        return http_response(created_task, 201)
    except Exception as err:
        return http_response({"error": str(err)}, 400)


def list_tasks(event, _):
    logging.info(f"event -> {event}")

    try:
        tasks = list_tasks_usecase.execute()
        return http_response({"data": tasks})
    except Exception as err:
        return http_response({"error": str(err)}, 400)


def toggle(event, _):
    logging.info(f"event -> {event}")

    try:
        task_id = event["pathParameters"]["task_id"]
        request = {"task_id": task_id}
        toggle_task_usecase.execute(request)

        return http_response(None, 204)
    except Exception as err:
        return http_response({"error": str(err)}, 400)


def remove(event, _):
    logging.info(f"event -> {event}")

    try:
        task_id = event["pathParameters"]["task_id"]
        request = {"task_id": task_id}
        remove_task_usecase.execute(request)

        return http_response(None, 204)
    except Exception as err:
        return http_response({"error": str(err)}, 400)
