
from ..models.task import Task
from ..models.category import Category

from ..database import models


def map_db_tasks_to_tasks(db_tasks: list[models.Task]) -> list[Task]:
    return list(map(lambda x: map_db_category_to_category(x), db_tasks))

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

def map_db_categories_to_categories(db_categories: list[models.Category]) -> list[Category]:
    return list(map(lambda x: map_db_category_to_category(x), db_categories))

def map_db_category_to_category(db_category: models.Category) -> Category:
    return Category(
        db_category.id,
        db_category.name
    )