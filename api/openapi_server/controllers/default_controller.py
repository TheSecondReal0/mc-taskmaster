import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_task_request import CreateTaskRequest  # noqa: E501
from openapi_server.models.get_tasks200_response import GetTasks200Response  # noqa: E501
from openapi_server.models.task import Task  # noqa: E501
from openapi_server import util

from ..biz import task_biz


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


def delete_task(task_id):  # noqa: E501
    """delete_task

     # noqa: E501

    :param task_id: 
    :type task_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    task_biz.delete_task(task_id)


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
