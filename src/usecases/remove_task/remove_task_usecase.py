from repositories.task_repository import TaskRepository
from usecases.remove_task.remove_task_dtos import RemoveTaskRequestDto


class RemoveTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.__task_repository = task_repository

    def execute(self, request: RemoveTaskRequestDto):
        task_id = request["task_id"]
        task = self.__task_repository.find_by_id(task_id)

        self.__task_repository.remove(task)
