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
ContentTypeSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            command_center_url = schemas.StrSchema
            trust_provider_url = schemas.StrSchema
            registration_trust_provider_url = schemas.StrSchema
            login_client_id = schemas.StrSchema
            registration_client_id = schemas.StrSchema
            reporting_client_id = schemas.StrSchema
            org_id = schemas.StrSchema
            org_name = schemas.StrSchema
            shield_uuid = schemas.StrSchema
            renewal_client_id = schemas.StrSchema
            external_client_id = schemas.StrSchema
            __annotations__ = {
                "command_center_url": command_center_url,
                "trust_provider_url": trust_provider_url,
                "registration_trust_provider_url": registration_trust_provider_url,
                "login_client_id": login_client_id,
                "registration_client_id": registration_client_id,
                "reporting_client_id": reporting_client_id,
                "org_id": org_id,
                "org_name": org_name,
                "shield_uuid": shield_uuid,
                "renewal_client_id": renewal_client_id,
                "external_client_id": external_client_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["command_center_url"]) -> MetaOapg.properties.command_center_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trust_provider_url"]) -> MetaOapg.properties.trust_provider_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_trust_provider_url"]) -> MetaOapg.properties.registration_trust_provider_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_client_id"]) -> MetaOapg.properties.login_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_client_id"]) -> MetaOapg.properties.registration_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reporting_client_id"]) -> MetaOapg.properties.reporting_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_name"]) -> MetaOapg.properties.org_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shield_uuid"]) -> MetaOapg.properties.shield_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renewal_client_id"]) -> MetaOapg.properties.renewal_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_client_id"]) -> MetaOapg.properties.external_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["command_center_url", "trust_provider_url", "registration_trust_provider_url", "login_client_id", "registration_client_id", "reporting_client_id", "org_id", "org_name", "shield_uuid", "renewal_client_id", "external_client_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["command_center_url"]) -> typing.Union[MetaOapg.properties.command_center_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trust_provider_url"]) -> typing.Union[MetaOapg.properties.trust_provider_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_trust_provider_url"]) -> typing.Union[MetaOapg.properties.registration_trust_provider_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_client_id"]) -> typing.Union[MetaOapg.properties.login_client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_client_id"]) -> typing.Union[MetaOapg.properties.registration_client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reporting_client_id"]) -> typing.Union[MetaOapg.properties.reporting_client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_name"]) -> typing.Union[MetaOapg.properties.org_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shield_uuid"]) -> typing.Union[MetaOapg.properties.shield_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renewal_client_id"]) -> typing.Union[MetaOapg.properties.renewal_client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_client_id"]) -> typing.Union[MetaOapg.properties.external_client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["command_center_url", "trust_provider_url", "registration_trust_provider_url", "login_client_id", "registration_client_id", "reporting_client_id", "org_id", "org_name", "shield_uuid", "renewal_client_id", "external_client_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        command_center_url: typing.Union[MetaOapg.properties.command_center_url, str, schemas.Unset] = schemas.unset,
        trust_provider_url: typing.Union[MetaOapg.properties.trust_provider_url, str, schemas.Unset] = schemas.unset,
        registration_trust_provider_url: typing.Union[MetaOapg.properties.registration_trust_provider_url, str, schemas.Unset] = schemas.unset,
        login_client_id: typing.Union[MetaOapg.properties.login_client_id, str, schemas.Unset] = schemas.unset,
        registration_client_id: typing.Union[MetaOapg.properties.registration_client_id, str, schemas.Unset] = schemas.unset,
        reporting_client_id: typing.Union[MetaOapg.properties.reporting_client_id, str, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, str, schemas.Unset] = schemas.unset,
        org_name: typing.Union[MetaOapg.properties.org_name, str, schemas.Unset] = schemas.unset,
        shield_uuid: typing.Union[MetaOapg.properties.shield_uuid, str, schemas.Unset] = schemas.unset,
        renewal_client_id: typing.Union[MetaOapg.properties.renewal_client_id, str, schemas.Unset] = schemas.unset,
        external_client_id: typing.Union[MetaOapg.properties.external_client_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            command_center_url=command_center_url,
            trust_provider_url=trust_provider_url,
            registration_trust_provider_url=registration_trust_provider_url,
            login_client_id=login_client_id,
            registration_client_id=registration_client_id,
            reporting_client_id=reporting_client_id,
            org_id=org_id,
            org_name=org_name,
            shield_uuid=shield_uuid,
            renewal_client_id=renewal_client_id,
            external_client_id=external_client_id,
            _configuration=_configuration,
            **kwargs,
        )
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_enduser_facing_org_details_get_oapg(
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
         Get org details  
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
            request_header_content_type,
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


class V1EnduserFacingOrgDetailsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_enduser_facing_org_details_get(
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
        return self._v1_enduser_facing_org_details_get_oapg(
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
        return self._v1_enduser_facing_org_details_get_oapg(
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


