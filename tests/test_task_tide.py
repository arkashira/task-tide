from task_tide import TaskTide, Task, ImportanceLevel
import json
import pytest

def test_add_task():
    task_tide = TaskTide()
    task = Task("Test Task", ImportanceLevel.HIGH)
    task_tide.add_task(task)
    assert task in task_tide.tasks

def test_get_prioritized_tasks():
    task_tide = TaskTide()
    task1 = Task("Task 1", ImportanceLevel.HIGH)
    task2 = Task("Task 2", ImportanceLevel.MEDIUM)
    task3 = Task("Task 3", ImportanceLevel.LOW)
    task_tide.add_task(task1)
    task_tide.add_task(task2)
    task_tide.add_task(task3)
    prioritized_tasks = task_tide.get_prioritized_tasks()
    assert prioritized_tasks[0].importance == ImportanceLevel.HIGH
    assert prioritized_tasks[1].importance == ImportanceLevel.MEDIUM
    assert prioritized_tasks[2].importance == ImportanceLevel.LOW

def test_save_to_json():
    task_tide = TaskTide()
    task = Task("Test Task", ImportanceLevel.HIGH)
    task_tide.add_task(task)
    task_tide.save_to_json("tasks.json")
    with open("tasks.json", "r") as f:
        tasks_json = json.load(f)
    assert len(tasks_json) == 1
    assert tasks_json[0]["name"] == "Test Task"
    assert tasks_json[0]["importance"] == "HIGH"

def test_load_from_json():
    task_tide = TaskTide()
    task = Task("Test Task", ImportanceLevel.HIGH)
    task_tide.add_task(task)
    task_tide.save_to_json("tasks.json")
    loaded_task_tide = TaskTide.load_from_json("tasks.json")
    assert len(loaded_task_tide.tasks) == 1
    assert loaded_task_tide.tasks[0].name == "Test Task"
    assert loaded_task_tide.tasks[0].importance == ImportanceLevel.HIGH

def test_edge_case_empty_task_list():
    task_tide = TaskTide()
    assert task_tide.get_prioritized_tasks() == []
