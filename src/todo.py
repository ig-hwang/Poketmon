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
    print("❌ 해당 ID의 작업을 찾을 수 없습니다.")
    return False

def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["is_done"] = True
            return True
    print("❌ 해당 ID의 작업을 찾을 수 없습니다.")
    return False

# 🎯 직접 실행 시 테스트용 코드
if __name__ == "__main__":
    print("✅ 작업 2개 추가")
    add_task("데이터 보고서 작성", "2025-07-31")
    add_task("운동하기")

    print("\n📋 현재 작업 목록:")
    print(list_tasks())

    target_id = tasks[0]["id"]
    print(f"\n✅ 작업 완료 처리: ID {target_id}")
    mark_done(target_id)

    print("\n📋 작업 목록 (완료 반영):")
    print(list_tasks())

    print(f"\n🗑️ 작업 삭제: ID {target_id}")
    remove_task(target_id)

    print("\n📋 작업 목록 (삭제 반영):")
    print(list_tasks())