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

    def prioritize_tasks(self):
        return sorted(self.tasks, key=lambda task: task.importance.value, reverse=True)

    def save_tasks(self, filename: str):
        tasks_data = [{"name": task.name, "importance": task.importance.name} for task in self.tasks]
        with open(filename, "w") as file:
            json.dump(tasks_data, file)

    def load_tasks(self, filename: str):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["name"], ImportanceLevel[task["importance"]]) for task in tasks_data]
        except FileNotFoundError:
            pass

def main():
    task_tide = TaskTide()
    while True:
        print("1. Add task")
        print("2. Prioritize tasks")
        print("3. Save tasks")
        print("4. Load tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter task name: ")
            importance = input("Enter importance level (LOW, MEDIUM, HIGH): ")
            task = Task(name, ImportanceLevel[importance])
            task_tide.add_task(task)
        elif choice == "2":
            prioritized_tasks = task_tide.prioritize_tasks()
            for i, task in enumerate(prioritized_tasks):
                print(f"{i+1}. {task.name} ({task.importance.name})")
        elif choice == "3":
            filename = input("Enter filename: ")
            task_tide.save_tasks(filename)
        elif choice == "4":
            filename = input("Enter filename: ")
            task_tide.load_tasks(filename)
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
