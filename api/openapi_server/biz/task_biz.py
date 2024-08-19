from ..models.get_tasks200_response import GetTasks200Response
from ..models.create_task_request import CreateTaskRequest
from ..models.task import Task
from ..models.category import Category

from .. import db

from ..database import models

def get_tasks() -> GetTasks200Response:
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
    to_insert: models.Task = models.Task(
        description = create_task_request.description,
        points = create_task_request.points,
        min_session = create_task_request.min_session,
        max_session = create_task_request.max_session
        )

    db.session.add(to_insert)
    db.session.commit()

    return map_db_task_to_task(to_insert)

def update_task(task_id, create_task_request: CreateTaskRequest) -> Task:
    to_update = models.Task.query.get(task_id)
    to_update.description = create_task_request.description
    to_update.points = create_task_request.points
    to_update.min_session = create_task_request.min_session
    to_update.max_session = create_task_request.max_session

    db.session.commit()

    return map_db_task_to_task(to_update)

def map_db_task_to_task(db_task: models.Task) -> Task:
    return Task(
        db_task.id,
        db_task.description,
        db_task.points,
        db_task.min_session,
        db_task.max_session,
        db_task.enabled,
        db_task.categories
    )