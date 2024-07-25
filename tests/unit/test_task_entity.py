import pytest

from entities.task import Task


def test_it_should_be_able_to_create_a_task_entity():
    data = {
        "description": "study japanese",
        "done": False
    }
    task = Task(data["description"], data["done"])
    assert task
    assert task.description == data["description"]


def test_it_should_not_be_able_to_create_a_task_entity():
    data = {
        "description": "aj",
        "done": False
    }
    with pytest.raises(Exception) as err:
        task = Task(data["description"], data["done"])
    assert "INVALID_TASK_DESCRIPTION" == str(err.value)


if __name__ == "__main__":
    pytest.main()
