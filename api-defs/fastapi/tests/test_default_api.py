# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.get_tasks200_response import GetTasks200Response  # noqa: F401


def test_get_tasks(client: TestClient):
    """Test case for get_tasks

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tasks",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

