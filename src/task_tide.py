import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class ImportanceLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class Task:
    name: str
    importance: ImportanceLevel

class TaskTide:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_prioritized_tasks(self) -> List[Task]:
        return sorted(self.tasks, key=lambda task: task.importance.value, reverse=True)

    def save_to_json(self, filename: str):
        tasks_json = [{"name": task.name, "importance": task.importance.name} for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(tasks_json, f)

    @classmethod
    def load_from_json(cls, filename: str):
        task_tide = cls()
        with open(filename, "r") as f:
            tasks_json = json.load(f)
        for task_json in tasks_json:
            task = Task(task_json["name"], ImportanceLevel[task_json["importance"]])
            task_tide.add_task(task)
        return task_tide
