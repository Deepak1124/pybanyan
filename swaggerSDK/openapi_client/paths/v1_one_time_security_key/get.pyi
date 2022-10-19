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

# query params
ClusterNameSchema = schemas.StrSchema
# header params
AuthorizationSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            OneTimeKey = schemas.StrSchema
            OTKExpiryTime = schemas.StrSchema
            PublicAddr = schemas.StrSchema
            OTKEnabled = schemas.StrSchema
            __annotations__ = {
                "OneTimeKey": OneTimeKey,
                "OTKExpiryTime": OTKExpiryTime,
                "PublicAddr": PublicAddr,
                "OTKEnabled": OTKEnabled,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OneTimeKey"]) -> MetaOapg.properties.OneTimeKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OTKExpiryTime"]) -> MetaOapg.properties.OTKExpiryTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PublicAddr"]) -> MetaOapg.properties.PublicAddr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OTKEnabled"]) -> MetaOapg.properties.OTKEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OneTimeKey", "OTKExpiryTime", "PublicAddr", "OTKEnabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OneTimeKey"]) -> typing.Union[MetaOapg.properties.OneTimeKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OTKExpiryTime"]) -> typing.Union[MetaOapg.properties.OTKExpiryTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PublicAddr"]) -> typing.Union[MetaOapg.properties.PublicAddr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OTKEnabled"]) -> typing.Union[MetaOapg.properties.OTKEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OneTimeKey", "OTKExpiryTime", "PublicAddr", "OTKEnabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        OneTimeKey: typing.Union[MetaOapg.properties.OneTimeKey, str, schemas.Unset] = schemas.unset,
        OTKExpiryTime: typing.Union[MetaOapg.properties.OTKExpiryTime, str, schemas.Unset] = schemas.unset,
        PublicAddr: typing.Union[MetaOapg.properties.PublicAddr, str, schemas.Unset] = schemas.unset,
        OTKEnabled: typing.Union[MetaOapg.properties.OTKEnabled, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            OneTimeKey=OneTimeKey,
            OTKExpiryTime=OTKExpiryTime,
            PublicAddr=PublicAddr,
            OTKEnabled=OTKEnabled,
            _configuration=_configuration,
            **kwargs,
        )
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_one_time_security_key_get_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
         Obtain one time key
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
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


class V1OneTimeSecurityKeyGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_one_time_security_key_get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_one_time_security_key_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_one_time_security_key_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


