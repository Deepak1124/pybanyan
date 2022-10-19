# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.v1_security_roles_enduser_devices import get  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1SecurityRolesEnduserDevices(ApiTestMixin, unittest.TestCase):
    """
    V1SecurityRolesEnduserDevices unit test stubs
         List Enduser and Device pairs for given role id  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
