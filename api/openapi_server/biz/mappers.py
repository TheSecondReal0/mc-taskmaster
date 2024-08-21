from ..models.task import Task
from ..models.category import Category
from ..models.player import Player
from ..models.player_lite import PlayerLite

from ..database import models


def map_db_tasks_to_tasks(db_tasks: list[models.Task]) -> list[Task]:
    if db_tasks is None:
        return None
    return list(map(lambda x: map_db_task_to_task(x), db_tasks))

def map_db_task_to_task(db_task: models.Task) -> Task:
    return Task(
        db_task.id,
        db_task.description,
        db_task.points,
        db_task.min_session,
        db_task.max_session,
        db_task.enabled,
        map_db_categories_to_categories(db_task.categories)
    )

def map_db_categories_to_categories(db_categories: list[models.Category]) -> list[Category]:
    if db_categories is None:
        return None
    return list(map(lambda x: map_db_category_to_category(x), db_categories))

def map_db_category_to_category(db_category: models.Category) -> Category:
    return Category(
        db_category.id,
        db_category.name,
        db_category.description
    )

def map_db_player_to_player(db_player: models.Player) -> Player:
    return Player(
        db_player.id,
        db_player.discord_id,
        db_player.score,
        map_db_categories_to_categories(db_player.categories),
        map_db_tasks_to_tasks(db_player.tasks)
    )

def map_db_players_to_player_lites(db_players: list[models.Player]) -> list[PlayerLite]:
    if db_players is None:
        return None
    return list(map(lambda x: map_db_player_to_player_lite(x), db_players))

def map_db_player_to_player_lite(db_player: models.Player) -> PlayerLite:
    return PlayerLite(
        db_player.id,
        db_player.discord_id,
        db_player.score,
        map_db_categories_to_categories(db_player.categories)
    )