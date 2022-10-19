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
    'bearerLoginToken',
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
                                ServiceID = schemas.StrSchema
                                ServiceType = schemas.StrSchema
                                
                                
                                class Metadata(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            name = schemas.StrSchema
                                            description = schemas.StrSchema
                                            cluster = schemas.StrSchema
                                            
                                            
                                            class tags(
                                                schemas.DictSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    
                                                    class properties:
                                                        template = schemas.StrSchema
                                                        user_facing = schemas.StrSchema
                                                        protocol = schemas.StrSchema
                                                        domain = schemas.StrSchema
                                                        port = schemas.IntSchema
                                                        icon = schemas.StrSchema
                                                        service_app_type = schemas.StrSchema
                                                        banyanproxy_mode = schemas.StrSchema
                                                        app_listen_port = schemas.StrSchema
                                                        allow_user_override = schemas.IntSchema
                                                        kube_cluster_name = schemas.StrSchema
                                                        kube_ca_key = schemas.StrSchema
                                                        __annotations__ = {
                                                            "template": template,
                                                            "user_facing": user_facing,
                                                            "protocol": protocol,
                                                            "domain": domain,
                                                            "port": port,
                                                            "icon": icon,
                                                            "service_app_type": service_app_type,
                                                            "banyanproxy_mode": banyanproxy_mode,
                                                            "app_listen_port": app_listen_port,
                                                            "allow_user_override": allow_user_override,
                                                            "kube_cluster_name": kube_cluster_name,
                                                            "kube_ca_key": kube_ca_key,
                                                        }
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["user_facing"]) -> MetaOapg.properties.user_facing: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["service_app_type"]) -> MetaOapg.properties.service_app_type: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["banyanproxy_mode"]) -> MetaOapg.properties.banyanproxy_mode: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["app_listen_port"]) -> MetaOapg.properties.app_listen_port: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["allow_user_override"]) -> MetaOapg.properties.allow_user_override: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["kube_cluster_name"]) -> MetaOapg.properties.kube_cluster_name: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["kube_ca_key"]) -> MetaOapg.properties.kube_ca_key: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                                
                                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["template", "user_facing", "protocol", "domain", "port", "icon", "service_app_type", "banyanproxy_mode", "app_listen_port", "allow_user_override", "kube_cluster_name", "kube_ca_key", ], str]):
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)
                                                
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["user_facing"]) -> typing.Union[MetaOapg.properties.user_facing, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["service_app_type"]) -> typing.Union[MetaOapg.properties.service_app_type, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["banyanproxy_mode"]) -> typing.Union[MetaOapg.properties.banyanproxy_mode, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["app_listen_port"]) -> typing.Union[MetaOapg.properties.app_listen_port, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["allow_user_override"]) -> typing.Union[MetaOapg.properties.allow_user_override, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["kube_cluster_name"]) -> typing.Union[MetaOapg.properties.kube_cluster_name, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["kube_ca_key"]) -> typing.Union[MetaOapg.properties.kube_ca_key, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                                
                                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["template", "user_facing", "protocol", "domain", "port", "icon", "service_app_type", "banyanproxy_mode", "app_listen_port", "allow_user_override", "kube_cluster_name", "kube_ca_key", ], str]):
                                                    return super().get_item_oapg(name)
                                                
                                            
                                                def __new__(
                                                    cls,
                                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                                    template: typing.Union[MetaOapg.properties.template, str, schemas.Unset] = schemas.unset,
                                                    user_facing: typing.Union[MetaOapg.properties.user_facing, str, schemas.Unset] = schemas.unset,
                                                    protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
                                                    domain: typing.Union[MetaOapg.properties.domain, str, schemas.Unset] = schemas.unset,
                                                    port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                                    icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
                                                    service_app_type: typing.Union[MetaOapg.properties.service_app_type, str, schemas.Unset] = schemas.unset,
                                                    banyanproxy_mode: typing.Union[MetaOapg.properties.banyanproxy_mode, str, schemas.Unset] = schemas.unset,
                                                    app_listen_port: typing.Union[MetaOapg.properties.app_listen_port, str, schemas.Unset] = schemas.unset,
                                                    allow_user_override: typing.Union[MetaOapg.properties.allow_user_override, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                                    kube_cluster_name: typing.Union[MetaOapg.properties.kube_cluster_name, str, schemas.Unset] = schemas.unset,
                                                    kube_ca_key: typing.Union[MetaOapg.properties.kube_ca_key, str, schemas.Unset] = schemas.unset,
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                                ) -> 'tags':
                                                    return super().__new__(
                                                        cls,
                                                        *args,
                                                        template=template,
                                                        user_facing=user_facing,
                                                        protocol=protocol,
                                                        domain=domain,
                                                        port=port,
                                                        icon=icon,
                                                        service_app_type=service_app_type,
                                                        banyanproxy_mode=banyanproxy_mode,
                                                        app_listen_port=app_listen_port,
                                                        allow_user_override=allow_user_override,
                                                        kube_cluster_name=kube_cluster_name,
                                                        kube_ca_key=kube_ca_key,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )
                                            __annotations__ = {
                                                "name": name,
                                                "description": description,
                                                "cluster": cluster,
                                                "tags": tags,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["cluster"]) -> MetaOapg.properties.cluster: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "cluster", "tags", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["cluster"]) -> typing.Union[MetaOapg.properties.cluster, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "cluster", "tags", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                                        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                                        cluster: typing.Union[MetaOapg.properties.cluster, str, schemas.Unset] = schemas.unset,
                                        tags: typing.Union[MetaOapg.properties.tags, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'Metadata':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            name=name,
                                            description=description,
                                            cluster=cluster,
                                            tags=tags,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "ServiceID": ServiceID,
                                    "ServiceType": ServiceType,
                                    "Metadata": Metadata,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceID"]) -> MetaOapg.properties.ServiceID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceType"]) -> MetaOapg.properties.ServiceType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Metadata"]) -> MetaOapg.properties.Metadata: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["ServiceID", "ServiceType", "Metadata", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceID"]) -> typing.Union[MetaOapg.properties.ServiceID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceType"]) -> typing.Union[MetaOapg.properties.ServiceType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Metadata"]) -> typing.Union[MetaOapg.properties.Metadata, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ServiceID", "ServiceType", "Metadata", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            ServiceID: typing.Union[MetaOapg.properties.ServiceID, str, schemas.Unset] = schemas.unset,
                            ServiceType: typing.Union[MetaOapg.properties.ServiceType, str, schemas.Unset] = schemas.unset,
                            Metadata: typing.Union[MetaOapg.properties.Metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                ServiceID=ServiceID,
                                ServiceType=ServiceType,
                                Metadata=Metadata,
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
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v2_enduser_facing_login_services_get_oapg(
        self: api_client.Api,
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
         GET to return the list of services visible using a login token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

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


class V2EnduserFacingLoginServicesGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v2_enduser_facing_login_services_get(
        self: BaseApi,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v2_enduser_facing_login_services_get_oapg(
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
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v2_enduser_facing_login_services_get_oapg(
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


