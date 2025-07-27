import uuid
from datetime import datetime

tasks = []

def add_task(description, due_date=None):
    task = {
        "id": str(uuid.uuid4())[:8],
        "description": description,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "is_done": False
    }
    tasks.append(task)

def list_tasks():
    if not tasks:
        return "등록된 작업이 없습니다."
    lines = []
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["is_done"] else "⬜️"
        line = f"{i}. {status} {task['description']} (ID: {task['id']})"
        if task["due_date"]:
            line += f" - 마감일: {task['due_date']}"
        lines.append(line)
    return "\n".join(lines)

def remove_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return True
    print("해당 ID의 작업을 찾을 수 없습니다.")
    return False

def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["is_done"] = True
            return True
    print("해당 ID의 작업을 찾을 수 없습니다.")
    return False