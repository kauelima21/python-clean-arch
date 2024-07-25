import os
import uuid

import boto3
from dotenv import load_dotenv

from entities.task import Task
from repositories.task_repository import TaskRepository

load_dotenv()


class BotoTaskRepository(TaskRepository):
    def __init__(self):
        self.__table_name = "tasks"
        local_db = None
        if os.environ.get("LOCAL_DB"):
            local_db = os.environ.get("LOCAL_DB")
        self.__table = boto3.resource(
            "dynamodb", endpoint_url=local_db).Table(self.__table_name)

    def create(self, task: Task) -> Task:
        try:
            generated_id = str(uuid.uuid4())
            self.__table.put_item(
                Item={
                    "task_id": generated_id,
                    "description": task.description,
                    "done": task.done,
                }
            )
            return Task(task.description, task.done, generated_id)
        except Exception as err:
            raise Exception("CREATE_TASK_ERROR" + str(err))

    def list(self) -> list[Task]:
        try:
            response = self.__table.scan()
            return [
                Task(
                    task.get("description"),
                    task.get("done"),
                    task.get("task_id")
                ) for task in response["Items"]
            ]
        except Exception as err:
            raise Exception("CREATE_TASK_ERROR" + str(err))

    def find_by_id(self, task_id: str) -> Task:
        try:
            response = self.__table.get_item(
                TableName=self.__table_name,
                Key={
                    "task_id": task_id,
                }
            )["Item"]
            return Task(response["description"], response["done"], response[
                "task_id"])
        except Exception as err:
            raise Exception("CREATE_TASK_ERROR" + str(err))

    def toggle(self, task: Task):
        try:
            self.__table.put_item(
                Item={
                    "task_id": task.task_id,
                    "description": task.description,
                    "done": not task.done,
                }
            )
        except Exception as err:
            raise Exception("CREATE_TASK_ERROR" + str(err))

    def remove(self, task: Task):
        try:
            self.__table.delete_item(
                TableName=self.__table_name,
                Key={
                    "task_id": task.task_id,
                }
            )
        except Exception as err:
            raise Exception("CREATE_TASK_ERROR" + str(err))
