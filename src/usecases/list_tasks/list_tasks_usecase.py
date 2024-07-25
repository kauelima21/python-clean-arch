from repositories.task_repository import TaskRepository
from usecases.list_tasks.list_tasks_dtos import ListTasksResponseDto


class ListTasksUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.__task_repository = task_repository

    def execute(self) -> list[ListTasksResponseDto]:
        tasks = self.__task_repository.list()
        result = [
            {
                "task_id": task.task_id,
                "description": task.description,
                "done": task.done
            } for task
            in tasks
        ]

        return result
