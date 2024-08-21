import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.category import Category  # noqa: E501
from openapi_server.models.create_category_request import CreateCategoryRequest  # noqa: E501
from openapi_server.models.create_task_request import CreateTaskRequest  # noqa: E501
from openapi_server.models.get_categories200_response import GetCategories200Response  # noqa: E501
from openapi_server.models.get_players200_response import GetPlayers200Response  # noqa: E501
from openapi_server.models.get_tasks200_response import GetTasks200Response  # noqa: E501
from openapi_server.models.player import Player  # noqa: E501
from openapi_server.models.task import Task  # noqa: E501
from openapi_server.models.update_player_request import UpdatePlayerRequest  # noqa: E501
from openapi_server import util

from ..biz import task_biz
from ..biz import category_biz
from ..biz import player_biz


def add_category_to_player(player_id, category_id):  # noqa: E501
    """add_category_to_player

    Add a category to a player # noqa: E501

    :param player_id: 
    :type player_id: str
    :param category_id: 
    :type category_id: str

    :rtype: Union[Player, Tuple[Player, int], Tuple[Player, int, Dict[str, str]]
    """
    return player_biz.add_category_to_player(player_id, category_id)


def add_category_to_task(task_id, category_id):  # noqa: E501
    """add_category_to_task

    Add a category to a task # noqa: E501

    :param task_id: 
    :type task_id: str
    :param category_id: 
    :type category_id: str

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    return task_biz.add_category_to_task(task_id, category_id)


def create_category():  # noqa: E501
    """create_category

     # noqa: E501

    :param create_category_request: Create a new category
    :type create_category_request: dict | bytes

    :rtype: Union[Category, Tuple[Category, int], Tuple[Category, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_category_request = CreateCategoryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return category_biz.create_category(create_category_request)


def create_task():  # noqa: E501
    """create_task

     # noqa: E501

    :param create_task_request: Create a new task
    :type create_task_request: dict | bytes

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_task_request = CreateTaskRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return task_biz.create_task(create_task_request)


def delete_category(category_id):  # noqa: E501
    """delete_category

     # noqa: E501

    :param category_id: 
    :type category_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return category_biz.delete_category(category_id)


def delete_task(task_id):  # noqa: E501
    """delete_task

     # noqa: E501

    :param task_id: 
    :type task_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    task_biz.delete_task(task_id)


def get_categories():  # noqa: E501
    """get_categories

     # noqa: E501


    :rtype: Union[GetCategories200Response, Tuple[GetCategories200Response, int], Tuple[GetCategories200Response, int, Dict[str, str]]
    """
    return category_biz.get_categories()


def get_category(category_id):  # noqa: E501
    """get_category

     # noqa: E501

    :param category_id: 
    :type category_id: str

    :rtype: Union[Category, Tuple[Category, int], Tuple[Category, int, Dict[str, str]]
    """
    return category_biz.get_category(category_id)


def get_player_by_discord_id(discord_id):  # noqa: E501
    """get_player_by_discord_id

    Get player data corresponding to discord id, if player doesn&#39;t exist create # noqa: E501

    :param discord_id: 
    :type discord_id: str

    :rtype: Union[Player, Tuple[Player, int], Tuple[Player, int, Dict[str, str]]
    """
    return player_biz.get_player_by_discord_id(discord_id)


def get_players():  # noqa: E501
    """get_players

     # noqa: E501


    :rtype: Union[GetPlayers200Response, Tuple[GetPlayers200Response, int], Tuple[GetPlayers200Response, int, Dict[str, str]]
    """
    return player_biz.get_players()


def get_task(task_id):  # noqa: E501
    """get_task

     # noqa: E501

    :param task_id: 
    :type task_id: str

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    return task_biz.get_task(task_id)


def get_tasks():  # noqa: E501
    """get_tasks

     # noqa: E501


    :rtype: Union[GetTasks200Response, Tuple[GetTasks200Response, int], Tuple[GetTasks200Response, int, Dict[str, str]]
    """
    return task_biz.get_tasks()


def remove_category_from_player(player_id, category_id):  # noqa: E501
    """remove_category_from_player

    Remove a category from a player # noqa: E501

    :param player_id: 
    :type player_id: str
    :param category_id: 
    :type category_id: str

    :rtype: Union[Player, Tuple[Player, int], Tuple[Player, int, Dict[str, str]]
    """
    return player_biz.remove_category_from_player(player_id, category_id)


def remove_category_from_task(task_id, category_id):  # noqa: E501
    """remove_category_from_task

    Remove a category from a task # noqa: E501

    :param task_id: 
    :type task_id: str
    :param category_id: 
    :type category_id: str

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    return task_biz.remove_category_from_task(task_id, category_id)


def update_category(category_id):  # noqa: E501
    """update_category

     # noqa: E501

    :param category_id: 
    :type category_id: str
    :param create_category_request: 
    :type create_category_request: dict | bytes

    :rtype: Union[Category, Tuple[Category, int], Tuple[Category, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_category_request = CreateCategoryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return category_biz.update_category(category_id, create_category_request)


def update_player(player_id):  # noqa: E501
    """update_player

    Update data corresponding to player with given id # noqa: E501

    :param player_id: 
    :type player_id: str
    :param update_player_request: 
    :type update_player_request: dict | bytes

    :rtype: Union[Player, Tuple[Player, int], Tuple[Player, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_player_request = UpdatePlayerRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return player_biz.update_player(player_id, update_player_request)


def update_task(task_id):  # noqa: E501
    """update_task

     # noqa: E501

    :param task_id: 
    :type task_id: str
    :param create_task_request: 
    :type create_task_request: dict | bytes

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_task_request = CreateTaskRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return task_biz.update_task(task_id, create_task_request)
