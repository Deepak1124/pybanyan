# coding: utf-8

"""
    Banyan Rest APIs

    This swagger spec contains list of all Banyan APIs.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.v2_api_key.get import V2ApiKeyGet
from openapi_client.paths.v2_api_key_id.delete import V2ApiKeyIdDelete
from openapi_client.paths.v2_api_key_id.get import V2ApiKeyIdGet
from openapi_client.paths.v2_api_key_id.put import V2ApiKeyIdPut
from openapi_client.paths.v2_api_key.post import V2ApiKeyPost
from openapi_client.paths.v2_api_key_scope.get import V2ApiKeyScopeGet


class ApiKeyApi(
    V2ApiKeyGet,
    V2ApiKeyIdDelete,
    V2ApiKeyIdGet,
    V2ApiKeyIdPut,
    V2ApiKeyPost,
    V2ApiKeyScopeGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
