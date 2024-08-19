from ..models.get_tasks200_response import GetTasks200Response
from ..models.task import Task
from ..models.category import Category

def get_tasks() -> GetTasks200Response:
    return GetTasks200Response([
        Task("1234", None, "do 7 things", 10, None, None, True, []),
        Task("12345", None, "do 100 things", 11, 2, 7, True, []),
        Task("3", None, "do fun things", 11, 2, 7, True, [Category(1, "fun")]),
        Task("4", None, "do pvp things", 11, 2, 7, True, [Category(2, "pvp")])
    ],
    4)