class Task:
    def __init__(self, description: str, done: bool, task_id: str = None):
        if not self.__isDescriptionValid(description):
            raise Exception("INVALID_TASK_DESCRIPTION")

        self.__description = description
        self.__done = done
        self.__task_id = task_id

    @property
    def description(self):
        return self.__description

    @property
    def done(self):
        return self.__done

    @property
    def task_id(self):
        return self.__task_id

    @staticmethod
    def __isDescriptionValid(description: str) -> bool:
        return 120 > len(description) > 3
