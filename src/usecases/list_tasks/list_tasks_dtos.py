from typing import TypedDict


class ListTasksResponseDto(TypedDict):
    task_id: str
    description: str
    done: bool
