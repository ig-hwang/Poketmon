tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    return tasks

def remove_task(index):
    try:
        tasks.pop(index)
    except IndexError:
        print("유효하지 않은 인덱스입니다.")