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

# header params
AuthorizationSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            total = schemas.IntSchema
            
            
            class trust_level(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        high = schemas.IntSchema
                        medium = schemas.IntSchema
                        low = schemas.IntSchema
                        always_allow = schemas.IntSchema
                        always_deny = schemas.IntSchema
                        unknown = schemas.IntSchema
                        __annotations__ = {
                            "high": high,
                            "medium": medium,
                            "low": low,
                            "always_allow": always_allow,
                            "always_deny": always_deny,
                            "unknown": unknown,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["high"]) -> MetaOapg.properties.high: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["medium"]) -> MetaOapg.properties.medium: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["low"]) -> MetaOapg.properties.low: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["always_allow"]) -> MetaOapg.properties.always_allow: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["always_deny"]) -> MetaOapg.properties.always_deny: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["unknown"]) -> MetaOapg.properties.unknown: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["high", "medium", "low", "always_allow", "always_deny", "unknown", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["high"]) -> typing.Union[MetaOapg.properties.high, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["medium"]) -> typing.Union[MetaOapg.properties.medium, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["low"]) -> typing.Union[MetaOapg.properties.low, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["always_allow"]) -> typing.Union[MetaOapg.properties.always_allow, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["always_deny"]) -> typing.Union[MetaOapg.properties.always_deny, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["unknown"]) -> typing.Union[MetaOapg.properties.unknown, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["high", "medium", "low", "always_allow", "always_deny", "unknown", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    high: typing.Union[MetaOapg.properties.high, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    medium: typing.Union[MetaOapg.properties.medium, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    low: typing.Union[MetaOapg.properties.low, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    always_allow: typing.Union[MetaOapg.properties.always_allow, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    always_deny: typing.Union[MetaOapg.properties.always_deny, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    unknown: typing.Union[MetaOapg.properties.unknown, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'trust_level':
                    return super().__new__(
                        cls,
                        *args,
                        high=high,
                        medium=medium,
                        low=low,
                        always_allow=always_allow,
                        always_deny=always_deny,
                        unknown=unknown,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class os(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        macOS = schemas.IntSchema
                        linux = schemas.IntSchema
                        windows = schemas.IntSchema
                        iOS = schemas.IntSchema
                        unknown = schemas.IntSchema
                        __annotations__ = {
                            "macOS": macOS,
                            "linux": linux,
                            "windows": windows,
                            "iOS": iOS,
                            "unknown": unknown,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["macOS"]) -> MetaOapg.properties.macOS: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["linux"]) -> MetaOapg.properties.linux: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["windows"]) -> MetaOapg.properties.windows: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["iOS"]) -> MetaOapg.properties.iOS: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["unknown"]) -> MetaOapg.properties.unknown: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["macOS", "linux", "windows", "iOS", "unknown", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["macOS"]) -> typing.Union[MetaOapg.properties.macOS, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["linux"]) -> typing.Union[MetaOapg.properties.linux, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["windows"]) -> typing.Union[MetaOapg.properties.windows, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["iOS"]) -> typing.Union[MetaOapg.properties.iOS, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["unknown"]) -> typing.Union[MetaOapg.properties.unknown, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["macOS", "linux", "windows", "iOS", "unknown", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    macOS: typing.Union[MetaOapg.properties.macOS, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    linux: typing.Union[MetaOapg.properties.linux, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    windows: typing.Union[MetaOapg.properties.windows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    iOS: typing.Union[MetaOapg.properties.iOS, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    unknown: typing.Union[MetaOapg.properties.unknown, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'os':
                    return super().__new__(
                        cls,
                        *args,
                        macOS=macOS,
                        linux=linux,
                        windows=windows,
                        iOS=iOS,
                        unknown=unknown,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "total": total,
                "trust_level": trust_level,
                "os": os,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trust_level"]) -> MetaOapg.properties.trust_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "trust_level", "os", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trust_level"]) -> typing.Union[MetaOapg.properties.trust_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> typing.Union[MetaOapg.properties.os, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "trust_level", "os", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trust_level: typing.Union[MetaOapg.properties.trust_level, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        os: typing.Union[MetaOapg.properties.os, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            total=total,
            trust_level=trust_level,
            os=os,
            _configuration=_configuration,
            **kwargs,
        )
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_devices_stats_get_oapg(
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
         Get the devices statistics for an org
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


class V1DevicesStatsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_devices_stats_get(
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
        return self._v1_devices_stats_get_oapg(
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
        return self._v1_devices_stats_get_oapg(
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


