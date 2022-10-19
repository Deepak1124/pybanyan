# coding: utf-8

"""
    Banyan Rest APIs

    This swagger spec contains list of all Banyan APIs.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.v2_tunnel_cidr.get import V2TunnelCidrGet
from openapi_client.paths.v2_tunnel_cidr_id.delete import V2TunnelCidrIdDelete
from openapi_client.paths.v2_tunnel_cidr.post import V2TunnelCidrPost


class TunnelCidrApi(
    V2TunnelCidrGet,
    V2TunnelCidrIdDelete,
    V2TunnelCidrPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
