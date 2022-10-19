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
IdSchema = schemas.StrSchema
ResourceNameSchema = schemas.StrSchema
ResourceTypeSchema = schemas.StrSchema
PrivateIpSchema = schemas.StrSchema
PublicIpSchema = schemas.StrSchema
PrivateDnsNameSchema = schemas.StrSchema
PublicDnsNameSchema = schemas.StrSchema
OrderBySchema = schemas.StrSchema
SortSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
SkipSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'id': typing.Union[IdSchema, str, ],
        'resource_name': typing.Union[ResourceNameSchema, str, ],
        'resource_type': typing.Union[ResourceTypeSchema, str, ],
        'private_ip': typing.Union[PrivateIpSchema, str, ],
        'public_ip': typing.Union[PublicIpSchema, str, ],
        'private_dns_name': typing.Union[PrivateDnsNameSchema, str, ],
        'public_dns_name': typing.Union[PublicDnsNameSchema, str, ],
        'order_by': typing.Union[OrderBySchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'skip': typing.Union[SkipSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_resource_name = api_client.QueryParameter(
    name="resource_name",
    style=api_client.ParameterStyle.FORM,
    schema=ResourceNameSchema,
    explode=True,
)
request_query_resource_type = api_client.QueryParameter(
    name="resource_type",
    style=api_client.ParameterStyle.FORM,
    schema=ResourceTypeSchema,
    explode=True,
)
request_query_private_ip = api_client.QueryParameter(
    name="private_ip",
    style=api_client.ParameterStyle.FORM,
    schema=PrivateIpSchema,
    explode=True,
)
request_query_public_ip = api_client.QueryParameter(
    name="public_ip",
    style=api_client.ParameterStyle.FORM,
    schema=PublicIpSchema,
    explode=True,
)
request_query_private_dns_name = api_client.QueryParameter(
    name="private_dns_name",
    style=api_client.ParameterStyle.FORM,
    schema=PrivateDnsNameSchema,
    explode=True,
)
request_query_public_dns_name = api_client.QueryParameter(
    name="public_dns_name",
    style=api_client.ParameterStyle.FORM,
    schema=PublicDnsNameSchema,
    explode=True,
)
request_query_order_by = api_client.QueryParameter(
    name="order_by",
    style=api_client.ParameterStyle.FORM,
    schema=OrderBySchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_skip = api_client.QueryParameter(
    name="skip",
    style=api_client.ParameterStyle.FORM,
    schema=SkipSchema,
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
                        
                        
                        class result(
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
                                            resource_id = schemas.StrSchema
                                            resource_name = schemas.StrSchema
                                            resource_type = schemas.StrSchema
                                            parent_id = schemas.StrSchema
                                            public_dns_name = schemas.StrSchema
                                            private_dns_name = schemas.StrSchema
                                            public_ip = schemas.StrSchema
                                            private_ip = schemas.StrSchema
                                            region = schemas.StrSchema
                                            service_id = schemas.StrSchema
                                            status = schemas.StrSchema
                                            cloud_provider = schemas.StrSchema
                                            created_at = schemas.IntSchema
                                            updated_at = schemas.IntSchema
                                            __annotations__ = {
                                                "id": id,
                                                "org_id": org_id,
                                                "resource_id": resource_id,
                                                "resource_name": resource_name,
                                                "resource_type": resource_type,
                                                "parent_id": parent_id,
                                                "public_dns_name": public_dns_name,
                                                "private_dns_name": private_dns_name,
                                                "public_ip": public_ip,
                                                "private_ip": private_ip,
                                                "region": region,
                                                "service_id": service_id,
                                                "status": status,
                                                "cloud_provider": cloud_provider,
                                                "created_at": created_at,
                                                "updated_at": updated_at,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["resource_id"]) -> MetaOapg.properties.resource_id: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["resource_name"]) -> MetaOapg.properties.resource_name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["public_dns_name"]) -> MetaOapg.properties.public_dns_name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["private_dns_name"]) -> MetaOapg.properties.private_dns_name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["public_ip"]) -> MetaOapg.properties.public_ip: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["private_ip"]) -> MetaOapg.properties.private_ip: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["service_id"]) -> MetaOapg.properties.service_id: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["cloud_provider"]) -> MetaOapg.properties.cloud_provider: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "resource_id", "resource_name", "resource_type", "parent_id", "public_dns_name", "private_dns_name", "public_ip", "private_ip", "region", "service_id", "status", "cloud_provider", "created_at", "updated_at", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["resource_id"]) -> typing.Union[MetaOapg.properties.resource_id, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["resource_name"]) -> typing.Union[MetaOapg.properties.resource_name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> typing.Union[MetaOapg.properties.resource_type, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["public_dns_name"]) -> typing.Union[MetaOapg.properties.public_dns_name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["private_dns_name"]) -> typing.Union[MetaOapg.properties.private_dns_name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["public_ip"]) -> typing.Union[MetaOapg.properties.public_ip, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["private_ip"]) -> typing.Union[MetaOapg.properties.private_ip, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["service_id"]) -> typing.Union[MetaOapg.properties.service_id, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["cloud_provider"]) -> typing.Union[MetaOapg.properties.cloud_provider, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "resource_id", "resource_name", "resource_type", "parent_id", "public_dns_name", "private_dns_name", "public_ip", "private_ip", "region", "service_id", "status", "cloud_provider", "created_at", "updated_at", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                                        org_id: typing.Union[MetaOapg.properties.org_id, str, schemas.Unset] = schemas.unset,
                                        resource_id: typing.Union[MetaOapg.properties.resource_id, str, schemas.Unset] = schemas.unset,
                                        resource_name: typing.Union[MetaOapg.properties.resource_name, str, schemas.Unset] = schemas.unset,
                                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, schemas.Unset] = schemas.unset,
                                        parent_id: typing.Union[MetaOapg.properties.parent_id, str, schemas.Unset] = schemas.unset,
                                        public_dns_name: typing.Union[MetaOapg.properties.public_dns_name, str, schemas.Unset] = schemas.unset,
                                        private_dns_name: typing.Union[MetaOapg.properties.private_dns_name, str, schemas.Unset] = schemas.unset,
                                        public_ip: typing.Union[MetaOapg.properties.public_ip, str, schemas.Unset] = schemas.unset,
                                        private_ip: typing.Union[MetaOapg.properties.private_ip, str, schemas.Unset] = schemas.unset,
                                        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
                                        service_id: typing.Union[MetaOapg.properties.service_id, str, schemas.Unset] = schemas.unset,
                                        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                                        cloud_provider: typing.Union[MetaOapg.properties.cloud_provider, str, schemas.Unset] = schemas.unset,
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
                                            resource_id=resource_id,
                                            resource_name=resource_name,
                                            resource_type=resource_type,
                                            parent_id=parent_id,
                                            public_dns_name=public_dns_name,
                                            private_dns_name=private_dns_name,
                                            public_ip=public_ip,
                                            private_ip=private_ip,
                                            region=region,
                                            service_id=service_id,
                                            status=status,
                                            cloud_provider=cloud_provider,
                                            created_at=created_at,
                                            updated_at=updated_at,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'result':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        count = schemas.IntSchema
                        __annotations__ = {
                            "result": result,
                            "count": count,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["result", "count", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["result", "count", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    result: typing.Union[MetaOapg.properties.result, list, tuple, schemas.Unset] = schemas.unset,
                    count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *args,
                        result=result,
                        count=count,
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
    '401': _response_for_401,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v2_cloud_resource_get_oapg(
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
         List Cloud Resources
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_id,
            request_query_resource_name,
            request_query_resource_type,
            request_query_private_ip,
            request_query_public_ip,
            request_query_private_dns_name,
            request_query_public_dns_name,
            request_query_order_by,
            request_query_sort,
            request_query_limit,
            request_query_skip,
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


class V2CloudResourceGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v2_cloud_resource_get(
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
        return self._v2_cloud_resource_get_oapg(
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
        return self._v2_cloud_resource_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


