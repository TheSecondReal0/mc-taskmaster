import unittest

from flask import json

from openapi_server.models.get_tasks200_response import GetTasks200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_tasks(self):
        """Test case for get_tasks

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/tasks',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
