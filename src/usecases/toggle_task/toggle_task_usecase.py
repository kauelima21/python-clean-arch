from repositories.task_repository import TaskRepository
from usecases.toggle_task.toggle_task_dtos import ToggleTaskRequestDto


class ToggleTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.__task_repository = task_repository

    def execute(self, request: ToggleTaskRequestDto):
        task_id = request["task_id"]
        task = self.__task_repository.find_by_id(task_id)

        self.__task_repository.toggle(task)
