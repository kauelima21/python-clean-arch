from entities.task import Task
from repositories.task_repository import TaskRepository
from usecases.create_task.create_task_dtos import CreateTaskRequestDto, \
    CreateTaskResponseDto


class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.__task_repository = task_repository

    def execute(self, request: CreateTaskRequestDto) -> CreateTaskResponseDto:
        description = request["description"]
        done = request["done"]
        task = Task(description, done)
        result = self.__task_repository.create(task)

        return {
            "task_id": result.task_id,
            "description": result.description,
            "done": result.done
        }
