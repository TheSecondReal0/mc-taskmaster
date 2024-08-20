from ..models.get_tasks200_response import GetTasks200Response
from ..models.create_task_request import CreateTaskRequest
from ..models.task import Task
from ..models.category import Category

from .. import db

from ..database import models

from .responses import *
from .mappers import *
from .helpers import *

def get_tasks() -> GetTasks200Response:
    tasks = models.Task.query.all()

    mapped = map_db_tasks_to_tasks(tasks)
    
    return GetTasks200Response(
        mapped,
        len(mapped)
    )

def get_task(task_id) -> Task:
    if not (validate_uuid(task_id)):
        return invalid_uuid(task_id)

    task = models.Task.query.get(task_id)
    if not task:
        return task_not_found(task_id)
    
    return map_db_task_to_task(task)

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
    if not (validate_uuid(task_id)):
        return invalid_uuid(task_id)

    to_update = models.Task.query.get(task_id)
    if not to_update:
        return task_not_found(task_id)
    
    to_update.description = create_task_request.description
    to_update.points = create_task_request.points
    to_update.min_session = create_task_request.min_session
    to_update.max_session = create_task_request.max_session

    db.session.commit()

    return map_db_task_to_task(to_update)

def delete_task(task_id):
    if not (validate_uuid(task_id)):
        return invalid_uuid(task_id)

    task = models.Task.query.get(task_id)
    if not task:
        return task_not_found(task_id)
    
    db.session.delete(task)
    db.session.commit()
