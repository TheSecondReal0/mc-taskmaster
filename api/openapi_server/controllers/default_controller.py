import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.get_tasks200_response import GetTasks200Response  # noqa: E501
from openapi_server import util


def get_tasks():  # noqa: E501
    """get_tasks

     # noqa: E501


    :rtype: Union[GetTasks200Response, Tuple[GetTasks200Response, int], Tuple[GetTasks200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
