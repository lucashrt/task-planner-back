from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
def get_tasks():
    return {"message": "Retrieving all tasks"}

@router.post("/")
def create_task():
    return {"message": "Creating a new task"}

@router.put("/{task_id}")
def update_task(task_id: int):
    return {"message": f"Updating task with id {task_id}"}

@router.delete("/{task_id}")
def delete_task(task_id: int):
    return {"message": f"Deleting task with id {task_id}"}