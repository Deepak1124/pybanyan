# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from . import path

# query params
ClusterNameSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'ClusterName': typing.Union[ClusterNameSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_cluster_name = api_client.QueryParameter(
    name="ClusterName",
    style=api_client.ParameterStyle.FORM,
    schema=ClusterNameSchema,
    explode=True,
)
# header params
AuthorizationSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Authorization': typing.Union[AuthorizationSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_authorization = api_client.HeaderParameter(
    name="Authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
_auth = [
    'bearerAuthToken',
]


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _v1_delete_shield_cluster_delete_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
         Delete a cluster and all associated data
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_cluster_name,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='delete'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class V1DeleteShieldClusterDelete(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_delete_shield_cluster_delete(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_delete_shield_cluster_delete_oapg(
            query_params=query_params,
            header_params=header_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def delete(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_delete_shield_cluster_delete_oapg(
            query_params=query_params,
            header_params=header_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


