# coding: utf-8

"""
    Banyan Rest APIs

    This swagger spec contains list of all Banyan APIs.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.v2_cloud_resource_service.get import V2CloudResourceServiceGet
from openapi_client.paths.v2_cloud_resource_service_id.get import V2CloudResourceServiceIdGet
from openapi_client.paths.v2_cloud_resource_service.post import V2CloudResourceServicePost


class CloudResourceServiceApi(
    V2CloudResourceServiceGet,
    V2CloudResourceServiceIdGet,
    V2CloudResourceServicePost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
