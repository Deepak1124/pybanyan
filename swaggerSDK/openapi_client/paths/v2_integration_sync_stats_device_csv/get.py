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
    'bearerAuthToken',
]


class SchemaFor200ResponseBodyTextCsv(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            integration_sync_status = schemas.StrSchema
            device_name = schemas.StrSchema
            Users = schemas.StrSchema
            Trustscore = schemas.IntSchema
            last_login = schemas.IntSchema
            device_status = schemas.StrSchema
            serial_number = schemas.StrSchema
            Platform = schemas.StrSchema
            Architecture = schemas.StrSchema
            OS = schemas.StrSchema
            signal1_name = schemas.StrSchema
            signal2_name = schemas.StrSchema
            signal_n_name = schemas.StrSchema
            __annotations__ = {
                "Integration Sync Status": integration_sync_status,
                "Device Name": device_name,
                "Users": Users,
                "Trustscore": Trustscore,
                "last login": last_login,
                "Device Status": device_status,
                "Serial Number": serial_number,
                "Platform": Platform,
                "Architecture": Architecture,
                "OS": OS,
                "<signal1 name>": signal1_name,
                "<signal2 name>": signal2_name,
                "<signalN name>": signal_n_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Integration Sync Status"]) -> MetaOapg.properties.integration_sync_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Device Name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Users"]) -> MetaOapg.properties.Users: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Trustscore"]) -> MetaOapg.properties.Trustscore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last login"]) -> MetaOapg.properties.last_login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Device Status"]) -> MetaOapg.properties.device_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Serial Number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Platform"]) -> MetaOapg.properties.Platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Architecture"]) -> MetaOapg.properties.Architecture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OS"]) -> MetaOapg.properties.OS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["<signal1 name>"]) -> MetaOapg.properties.signal1_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["<signal2 name>"]) -> MetaOapg.properties.signal2_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["<signalN name>"]) -> MetaOapg.properties.signal_n_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Integration Sync Status", "Device Name", "Users", "Trustscore", "last login", "Device Status", "Serial Number", "Platform", "Architecture", "OS", "<signal1 name>", "<signal2 name>", "<signalN name>", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Integration Sync Status"]) -> typing.Union[MetaOapg.properties.integration_sync_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Device Name"]) -> typing.Union[MetaOapg.properties.device_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Users"]) -> typing.Union[MetaOapg.properties.Users, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Trustscore"]) -> typing.Union[MetaOapg.properties.Trustscore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last login"]) -> typing.Union[MetaOapg.properties.last_login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Device Status"]) -> typing.Union[MetaOapg.properties.device_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Serial Number"]) -> typing.Union[MetaOapg.properties.serial_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Platform"]) -> typing.Union[MetaOapg.properties.Platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Architecture"]) -> typing.Union[MetaOapg.properties.Architecture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OS"]) -> typing.Union[MetaOapg.properties.OS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["<signal1 name>"]) -> typing.Union[MetaOapg.properties.signal1_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["<signal2 name>"]) -> typing.Union[MetaOapg.properties.signal2_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["<signalN name>"]) -> typing.Union[MetaOapg.properties.signal_n_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Integration Sync Status", "Device Name", "Users", "Trustscore", "last login", "Device Status", "Serial Number", "Platform", "Architecture", "OS", "<signal1 name>", "<signal2 name>", "<signalN name>", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Users: typing.Union[MetaOapg.properties.Users, str, schemas.Unset] = schemas.unset,
        Trustscore: typing.Union[MetaOapg.properties.Trustscore, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Platform: typing.Union[MetaOapg.properties.Platform, str, schemas.Unset] = schemas.unset,
        Architecture: typing.Union[MetaOapg.properties.Architecture, str, schemas.Unset] = schemas.unset,
        OS: typing.Union[MetaOapg.properties.OS, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyTextCsv':
        return super().__new__(
            cls,
            *args,
            Users=Users,
            Trustscore=Trustscore,
            Platform=Platform,
            Architecture=Architecture,
            OS=OS,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextCsv,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/csv': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextCsv),
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
    '500': _response_for_500,
}
_all_accept_content_types = (
    'text/csv',
)


class BaseApi(api_client.Api):

    def _v2_integration_sync_stats_device_csv_get_oapg(
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
         Get the integration sync stats in CSV format
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


class V2IntegrationSyncStatsDeviceCsvGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v2_integration_sync_stats_device_csv_get(
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
        return self._v2_integration_sync_stats_device_csv_get_oapg(
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
        return self._v2_integration_sync_stats_device_csv_get_oapg(
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


