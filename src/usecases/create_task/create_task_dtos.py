from typing import TypedDict


class CreateTaskRequestDto(TypedDict):
    description: str
    done: bool


class CreateTaskResponseDto(TypedDict):
    task_id: str
    description: str
    done: bool
