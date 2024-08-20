
from ..models.task import Task
from ..models.category import Category

from ..database import models


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