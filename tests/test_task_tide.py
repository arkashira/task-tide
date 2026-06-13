from task_tide import Task, TaskTide, ImportanceLevel

def test_task_creation():
    task = Task("Test task", ImportanceLevel.HIGH)
    assert task.name == "Test task"
    assert task.importance == ImportanceLevel.HIGH

def test_task_tide_add_task():
    task_tide = TaskTide()
    task = Task("Test task", ImportanceLevel.HIGH)
    task_tide.add_task(task)
    assert len(task_tide.tasks) == 1

def test_task_tide_prioritize_tasks():
    task_tide = TaskTide()
    task1 = Task("Test task 1", ImportanceLevel.HIGH)
    task2 = Task("Test task 2", ImportanceLevel.MEDIUM)
    task3 = Task("Test task 3", ImportanceLevel.LOW)
    task_tide.add_task(task1)
    task_tide.add_task(task2)
    task_tide.add_task(task3)
    prioritized_tasks = task_tide.prioritize_tasks()
    assert prioritized_tasks[0].importance == ImportanceLevel.HIGH
    assert prioritized_tasks[1].importance == ImportanceLevel.MEDIUM
    assert prioritized_tasks[2].importance == ImportanceLevel.LOW

def test_task_tide_save_tasks():
    task_tide = TaskTide()
    task1 = Task("Test task 1", ImportanceLevel.HIGH)
    task2 = Task("Test task 2", ImportanceLevel.MEDIUM)
    task_tide.add_task(task1)
    task_tide.add_task(task2)
    task_tide.save_tasks("tasks.json")
    with open("tasks.json", "r") as file:
        tasks_data = file.read()
        assert tasks_data == '[{"name": "Test task 1", "importance": "HIGH"}, {"name": "Test task 2", "importance": "MEDIUM"}]'

def test_task_tide_load_tasks():
    task_tide = TaskTide()
    task_tide.load_tasks("tasks.json")
    assert len(task_tide.tasks) == 2
    assert task_tide.tasks[0].name == "Test task 1"
    assert task_tide.tasks[0].importance == ImportanceLevel.HIGH
    assert task_tide.tasks[1].name == "Test task 2"
    assert task_tide.tasks[1].importance == ImportanceLevel.MEDIUM
