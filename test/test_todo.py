from src.todo import add_task, list_tasks, remove_task

def test_todo_workflow():
    add_task("책 읽기")
    add_task("운동하기")
    assert list_tasks() == ["책 읽기", "운동하기"]
    remove_task(0)
    assert list_tasks() == ["운동하기"]