from tutorial import Tutorial, Task
import json

def test_tutorial_display():
    tutorial = Tutorial()
    tutorial.display_tutorial()

def test_tutorial_data():
    tutorial = Tutorial()
    data = tutorial.get_tutorial_data()
    tasks = json.loads(data)
    assert len(tasks) == 3
    assert tasks[0]["name"] == "High Priority Task"
    assert tasks[0]["priority"] == 1
    assert tasks[1]["name"] == "Medium Priority Task"
    assert tasks[1]["priority"] == 2
    assert tasks[2]["name"] == "Low Priority Task"
    assert tasks[2]["priority"] == 3

def test_task_init():
    task = Task("Test Task", 1)
    assert task.name == "Test Task"
    assert task.priority == 1
