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
GroupNameSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'group_name': typing.Union[GroupNameSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_group_name = api_client.QueryParameter(
    name="group_name",
    style=api_client.ParameterStyle.FORM,
    schema=GroupNameSchema,
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
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        NextToken = schemas.IntSchema
                        
                        
                        class Users(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            
                                            
                                            class Attributes(
                                                schemas.ListSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    
                                                    
                                                    class items(
                                                        schemas.DictSchema
                                                    ):
                                                    
                                                    
                                                        class MetaOapg:
                                                            
                                                            class properties:
                                                                Name = schemas.StrSchema
                                                                Value = schemas.StrSchema
                                                                Enabled = schemas.IntSchema
                                                                MFAOptions = schemas.IntSchema
                                                                UserCreateDate = schemas.StrSchema
                                                                UserLastModifiedDate = schemas.StrSchema
                                                                UserStatus = schemas.StrSchema
                                                                Username = schemas.StrSchema
                                                                __annotations__ = {
                                                                    "Name": Name,
                                                                    "Value": Value,
                                                                    "Enabled": Enabled,
                                                                    "MFAOptions": MFAOptions,
                                                                    "UserCreateDate": UserCreateDate,
                                                                    "UserLastModifiedDate": UserLastModifiedDate,
                                                                    "UserStatus": UserStatus,
                                                                    "Username": Username,
                                                                }
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["Enabled"]) -> MetaOapg.properties.Enabled: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["MFAOptions"]) -> MetaOapg.properties.MFAOptions: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["UserCreateDate"]) -> MetaOapg.properties.UserCreateDate: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["UserLastModifiedDate"]) -> MetaOapg.properties.UserLastModifiedDate: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["UserStatus"]) -> MetaOapg.properties.UserStatus: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: typing_extensions.Literal["Username"]) -> MetaOapg.properties.Username: ...
                                                        
                                                        @typing.overload
                                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                                        
                                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name", "Value", "Enabled", "MFAOptions", "UserCreateDate", "UserLastModifiedDate", "UserStatus", "Username", ], str]):
                                                            # dict_instance[name] accessor
                                                            return super().__getitem__(name)
                                                        
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["Enabled"]) -> typing.Union[MetaOapg.properties.Enabled, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["MFAOptions"]) -> typing.Union[MetaOapg.properties.MFAOptions, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["UserCreateDate"]) -> typing.Union[MetaOapg.properties.UserCreateDate, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["UserLastModifiedDate"]) -> typing.Union[MetaOapg.properties.UserLastModifiedDate, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["UserStatus"]) -> typing.Union[MetaOapg.properties.UserStatus, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: typing_extensions.Literal["Username"]) -> typing.Union[MetaOapg.properties.Username, schemas.Unset]: ...
                                                        
                                                        @typing.overload
                                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                                        
                                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name", "Value", "Enabled", "MFAOptions", "UserCreateDate", "UserLastModifiedDate", "UserStatus", "Username", ], str]):
                                                            return super().get_item_oapg(name)
                                                        
                                                    
                                                        def __new__(
                                                            cls,
                                                            *args: typing.Union[dict, frozendict.frozendict, ],
                                                            Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
                                                            Value: typing.Union[MetaOapg.properties.Value, str, schemas.Unset] = schemas.unset,
                                                            Enabled: typing.Union[MetaOapg.properties.Enabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                                            MFAOptions: typing.Union[MetaOapg.properties.MFAOptions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                                            UserCreateDate: typing.Union[MetaOapg.properties.UserCreateDate, str, schemas.Unset] = schemas.unset,
                                                            UserLastModifiedDate: typing.Union[MetaOapg.properties.UserLastModifiedDate, str, schemas.Unset] = schemas.unset,
                                                            UserStatus: typing.Union[MetaOapg.properties.UserStatus, str, schemas.Unset] = schemas.unset,
                                                            Username: typing.Union[MetaOapg.properties.Username, str, schemas.Unset] = schemas.unset,
                                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                                        ) -> 'items':
                                                            return super().__new__(
                                                                cls,
                                                                *args,
                                                                Name=Name,
                                                                Value=Value,
                                                                Enabled=Enabled,
                                                                MFAOptions=MFAOptions,
                                                                UserCreateDate=UserCreateDate,
                                                                UserLastModifiedDate=UserLastModifiedDate,
                                                                UserStatus=UserStatus,
                                                                Username=Username,
                                                                _configuration=_configuration,
                                                                **kwargs,
                                                            )
                                            
                                                def __new__(
                                                    cls,
                                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                ) -> 'Attributes':
                                                    return super().__new__(
                                                        cls,
                                                        arg,
                                                        _configuration=_configuration,
                                                    )
                                            
                                                def __getitem__(self, i: int) -> MetaOapg.items:
                                                    return super().__getitem__(i)
                                            __annotations__ = {
                                                "Attributes": Attributes,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Attributes"]) -> MetaOapg.properties.Attributes: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Attributes", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Attributes"]) -> typing.Union[MetaOapg.properties.Attributes, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Attributes", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        Attributes: typing.Union[MetaOapg.properties.Attributes, list, tuple, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'items':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            Attributes=Attributes,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'Users':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "NextToken": NextToken,
                            "Users": Users,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["NextToken"]) -> MetaOapg.properties.NextToken: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Users"]) -> MetaOapg.properties.Users: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["NextToken", "Users", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["NextToken"]) -> typing.Union[MetaOapg.properties.NextToken, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Users"]) -> typing.Union[MetaOapg.properties.Users, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["NextToken", "Users", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    NextToken: typing.Union[MetaOapg.properties.NextToken, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    Users: typing.Union[MetaOapg.properties.Users, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *args,
                        NextToken=NextToken,
                        Users=Users,
                        _configuration=_configuration,
                        **kwargs,
                    )
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
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
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
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_banyanidp_admin_group_user_get_oapg(
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
         Get users in a group
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_group_name,
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


class V1BanyanidpAdminGroupUserGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_banyanidp_admin_group_user_get(
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
        return self._v1_banyanidp_admin_group_user_get_oapg(
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
        return self._v1_banyanidp_admin_group_user_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


