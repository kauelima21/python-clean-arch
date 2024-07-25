from typing import Protocol
from entities.task import Task


class TaskRepository(Protocol):
    def create(self, task: Task) -> Task:
        ...

    def list(self) -> list[Task]:
        ...

    def find_by_id(self, task_id: str) -> Task:
        ...

    def toggle(self, task: Task):
        ...

    def remove(self, task: Task):
        ...
