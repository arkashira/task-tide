import json
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int

class Tutorial:
    def __init__(self):
        self.tasks = [
            Task("High Priority Task", 1),
            Task("Medium Priority Task", 2),
            Task("Low Priority Task", 3)
        ]

    def display_tutorial(self):
        print("Welcome to the task prioritization tutorial!")
        print("The prioritization framework is based on the following rules:")
        print("1. High priority tasks are those that are urgent and important.")
        print("2. Medium priority tasks are those that are important but not urgent.")
        print("3. Low priority tasks are those that are not urgent or important.")
        print("Examples of task prioritization:")
        for task in self.tasks:
            print(f"Task: {task.name}, Priority: {task.priority}")

    def get_tutorial_data(self):
        return json.dumps([task.__dict__ for task in self.tasks])

def main():
    tutorial = Tutorial()
    tutorial.display_tutorial()

if __name__ == "__main__":
    main()
