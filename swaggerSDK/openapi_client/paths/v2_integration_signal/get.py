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
IntegrationIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'integration_id': typing.Union[IntegrationIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_integration_id = api_client.QueryParameter(
    name="integration_id",
    style=api_client.ParameterStyle.FORM,
    schema=IntegrationIdSchema,
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


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            request_id = schemas.StrSchema
            error_code = schemas.IntSchema
            error_description = schemas.StrSchema
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                id = schemas.StrSchema
                                org_id = schemas.StrSchema
                                integration_id = schemas.StrSchema
                                name = schemas.StrSchema
                                type = schemas.StrSchema
                                signal_min_threshold = schemas.IntSchema
                                signal_value_match = schemas.StrSchema
                                signal_not_satisfied_message = schemas.StrSchema
                                signal_not_satisfied_trustlevel = schemas.StrSchema
                                active = schemas.IntSchema
                                windows_remediation_description = schemas.StrSchema
                                macos_remediation_description = schemas.StrSchema
                                linux_remediation_description = schemas.StrSchema
                                ios_remediation_description = schemas.StrSchema
                                android_remediation_description = schemas.StrSchema
                                created_at = schemas.IntSchema
                                updated_at = schemas.IntSchema
                                __annotations__ = {
                                    "id": id,
                                    "org_id": org_id,
                                    "integration_id": integration_id,
                                    "name": name,
                                    "type": type,
                                    "signal_min_threshold": signal_min_threshold,
                                    "signal_value_match": signal_value_match,
                                    "signal_not_satisfied_message": signal_not_satisfied_message,
                                    "signal_not_satisfied_trustlevel": signal_not_satisfied_trustlevel,
                                    "active": active,
                                    "windows_remediation_description": windows_remediation_description,
                                    "macos_remediation_description": macos_remediation_description,
                                    "linux_remediation_description": linux_remediation_description,
                                    "ios_remediation_description": ios_remediation_description,
                                    "android_remediation_description": android_remediation_description,
                                    "created_at": created_at,
                                    "updated_at": updated_at,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["integration_id"]) -> MetaOapg.properties.integration_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["signal_min_threshold"]) -> MetaOapg.properties.signal_min_threshold: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["signal_value_match"]) -> MetaOapg.properties.signal_value_match: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["signal_not_satisfied_message"]) -> MetaOapg.properties.signal_not_satisfied_message: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["signal_not_satisfied_trustlevel"]) -> MetaOapg.properties.signal_not_satisfied_trustlevel: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["windows_remediation_description"]) -> MetaOapg.properties.windows_remediation_description: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["macos_remediation_description"]) -> MetaOapg.properties.macos_remediation_description: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["linux_remediation_description"]) -> MetaOapg.properties.linux_remediation_description: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ios_remediation_description"]) -> MetaOapg.properties.ios_remediation_description: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["android_remediation_description"]) -> MetaOapg.properties.android_remediation_description: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "integration_id", "name", "type", "signal_min_threshold", "signal_value_match", "signal_not_satisfied_message", "signal_not_satisfied_trustlevel", "active", "windows_remediation_description", "macos_remediation_description", "linux_remediation_description", "ios_remediation_description", "android_remediation_description", "created_at", "updated_at", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["integration_id"]) -> typing.Union[MetaOapg.properties.integration_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["signal_min_threshold"]) -> typing.Union[MetaOapg.properties.signal_min_threshold, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["signal_value_match"]) -> typing.Union[MetaOapg.properties.signal_value_match, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["signal_not_satisfied_message"]) -> typing.Union[MetaOapg.properties.signal_not_satisfied_message, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["signal_not_satisfied_trustlevel"]) -> typing.Union[MetaOapg.properties.signal_not_satisfied_trustlevel, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["windows_remediation_description"]) -> typing.Union[MetaOapg.properties.windows_remediation_description, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["macos_remediation_description"]) -> typing.Union[MetaOapg.properties.macos_remediation_description, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["linux_remediation_description"]) -> typing.Union[MetaOapg.properties.linux_remediation_description, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ios_remediation_description"]) -> typing.Union[MetaOapg.properties.ios_remediation_description, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["android_remediation_description"]) -> typing.Union[MetaOapg.properties.android_remediation_description, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "integration_id", "name", "type", "signal_min_threshold", "signal_value_match", "signal_not_satisfied_message", "signal_not_satisfied_trustlevel", "active", "windows_remediation_description", "macos_remediation_description", "linux_remediation_description", "ios_remediation_description", "android_remediation_description", "created_at", "updated_at", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            org_id: typing.Union[MetaOapg.properties.org_id, str, schemas.Unset] = schemas.unset,
                            integration_id: typing.Union[MetaOapg.properties.integration_id, str, schemas.Unset] = schemas.unset,
                            name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                            type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                            signal_min_threshold: typing.Union[MetaOapg.properties.signal_min_threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            signal_value_match: typing.Union[MetaOapg.properties.signal_value_match, str, schemas.Unset] = schemas.unset,
                            signal_not_satisfied_message: typing.Union[MetaOapg.properties.signal_not_satisfied_message, str, schemas.Unset] = schemas.unset,
                            signal_not_satisfied_trustlevel: typing.Union[MetaOapg.properties.signal_not_satisfied_trustlevel, str, schemas.Unset] = schemas.unset,
                            active: typing.Union[MetaOapg.properties.active, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            windows_remediation_description: typing.Union[MetaOapg.properties.windows_remediation_description, str, schemas.Unset] = schemas.unset,
                            macos_remediation_description: typing.Union[MetaOapg.properties.macos_remediation_description, str, schemas.Unset] = schemas.unset,
                            linux_remediation_description: typing.Union[MetaOapg.properties.linux_remediation_description, str, schemas.Unset] = schemas.unset,
                            ios_remediation_description: typing.Union[MetaOapg.properties.ios_remediation_description, str, schemas.Unset] = schemas.unset,
                            android_remediation_description: typing.Union[MetaOapg.properties.android_remediation_description, str, schemas.Unset] = schemas.unset,
                            created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                id=id,
                                org_id=org_id,
                                integration_id=integration_id,
                                name=name,
                                type=type,
                                signal_min_threshold=signal_min_threshold,
                                signal_value_match=signal_value_match,
                                signal_not_satisfied_message=signal_not_satisfied_message,
                                signal_not_satisfied_trustlevel=signal_not_satisfied_trustlevel,
                                active=active,
                                windows_remediation_description=windows_remediation_description,
                                macos_remediation_description=macos_remediation_description,
                                linux_remediation_description=linux_remediation_description,
                                ios_remediation_description=ios_remediation_description,
                                android_remediation_description=android_remediation_description,
                                created_at=created_at,
                                updated_at=updated_at,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "request_id": request_id,
                "error_code": error_code,
                "error_description": error_description,
                "data": data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_description"]) -> MetaOapg.properties.error_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["request_id", "error_code", "error_description", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> typing.Union[MetaOapg.properties.request_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> typing.Union[MetaOapg.properties.error_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_description"]) -> typing.Union[MetaOapg.properties.error_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["request_id", "error_code", "error_description", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, schemas.Unset] = schemas.unset,
        error_code: typing.Union[MetaOapg.properties.error_code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        error_description: typing.Union[MetaOapg.properties.error_description, str, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            request_id=request_id,
            error_code=error_code,
            error_description=error_description,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v2_integration_signal_get_oapg(
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
         GET integration signal
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_integration_id,
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


class V2IntegrationSignalGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v2_integration_signal_get(
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
        return self._v2_integration_signal_get_oapg(
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
        return self._v2_integration_signal_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


