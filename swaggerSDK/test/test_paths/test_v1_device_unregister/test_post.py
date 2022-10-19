# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.v1_device_unregister import post  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1DeviceUnregister(ApiTestMixin, unittest.TestCase):
    """
    V1DeviceUnregister unit test stubs
         Unregister an enduser device  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
