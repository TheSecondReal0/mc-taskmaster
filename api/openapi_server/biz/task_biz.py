from ..models.get_tasks200_response import GetTasks200Response
from ..models.create_task_request import CreateTaskRequest
from ..models.task import Task
from ..models.category import Category

# from .. import db

from ..database import models

def get_tasks() -> GetTasks200Response:
    print(models.Task)
    tasks = models.Task.query.all()

    mapped = []
    for task in tasks:
        mapped.append(Task(
            task.id,
            task.description,
            task.points,
            task.min_session,
            task.max_session,
            task.enabled,
            task.categories
        ))
    
    return GetTasks200Response(
        mapped,
        len(mapped)
    )

def create_task(create_task_request: CreateTaskRequest) -> Task:
    pass