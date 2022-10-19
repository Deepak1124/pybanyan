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
# path params
AttachedToTypeSchema = schemas.StrSchema
AttachedToIDSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    PolicyID = schemas.StrSchema
                    PolicyName = schemas.StrSchema
                    AttachedToID = schemas.StrSchema
                    AttachedToName = schemas.StrSchema
                    AttachedToType = schemas.StrSchema
                    Enabled = schemas.StrSchema
                    AttachedAt = schemas.IntSchema
                    AttachedBy = schemas.StrSchema
                    AttachedToFriendlyName = schemas.StrSchema
                    __annotations__ = {
                        "PolicyID": PolicyID,
                        "PolicyName": PolicyName,
                        "AttachedToID": AttachedToID,
                        "AttachedToName": AttachedToName,
                        "AttachedToType": AttachedToType,
                        "Enabled": Enabled,
                        "AttachedAt": AttachedAt,
                        "AttachedBy": AttachedBy,
                        "AttachedToFriendlyName": AttachedToFriendlyName,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["PolicyID"]) -> MetaOapg.properties.PolicyID: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["PolicyName"]) -> MetaOapg.properties.PolicyName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedToID"]) -> MetaOapg.properties.AttachedToID: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedToName"]) -> MetaOapg.properties.AttachedToName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedToType"]) -> MetaOapg.properties.AttachedToType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Enabled"]) -> MetaOapg.properties.Enabled: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedAt"]) -> MetaOapg.properties.AttachedAt: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedBy"]) -> MetaOapg.properties.AttachedBy: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AttachedToFriendlyName"]) -> MetaOapg.properties.AttachedToFriendlyName: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["PolicyID", "PolicyName", "AttachedToID", "AttachedToName", "AttachedToType", "Enabled", "AttachedAt", "AttachedBy", "AttachedToFriendlyName", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["PolicyID"]) -> typing.Union[MetaOapg.properties.PolicyID, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["PolicyName"]) -> typing.Union[MetaOapg.properties.PolicyName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedToID"]) -> typing.Union[MetaOapg.properties.AttachedToID, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedToName"]) -> typing.Union[MetaOapg.properties.AttachedToName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedToType"]) -> typing.Union[MetaOapg.properties.AttachedToType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Enabled"]) -> typing.Union[MetaOapg.properties.Enabled, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedAt"]) -> typing.Union[MetaOapg.properties.AttachedAt, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedBy"]) -> typing.Union[MetaOapg.properties.AttachedBy, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AttachedToFriendlyName"]) -> typing.Union[MetaOapg.properties.AttachedToFriendlyName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["PolicyID", "PolicyName", "AttachedToID", "AttachedToName", "AttachedToType", "Enabled", "AttachedAt", "AttachedBy", "AttachedToFriendlyName", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                PolicyID: typing.Union[MetaOapg.properties.PolicyID, str, schemas.Unset] = schemas.unset,
                PolicyName: typing.Union[MetaOapg.properties.PolicyName, str, schemas.Unset] = schemas.unset,
                AttachedToID: typing.Union[MetaOapg.properties.AttachedToID, str, schemas.Unset] = schemas.unset,
                AttachedToName: typing.Union[MetaOapg.properties.AttachedToName, str, schemas.Unset] = schemas.unset,
                AttachedToType: typing.Union[MetaOapg.properties.AttachedToType, str, schemas.Unset] = schemas.unset,
                Enabled: typing.Union[MetaOapg.properties.Enabled, str, schemas.Unset] = schemas.unset,
                AttachedAt: typing.Union[MetaOapg.properties.AttachedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                AttachedBy: typing.Union[MetaOapg.properties.AttachedBy, str, schemas.Unset] = schemas.unset,
                AttachedToFriendlyName: typing.Union[MetaOapg.properties.AttachedToFriendlyName, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    PolicyID=PolicyID,
                    PolicyName=PolicyName,
                    AttachedToID=AttachedToID,
                    AttachedToName=AttachedToName,
                    AttachedToType=AttachedToType,
                    Enabled=Enabled,
                    AttachedAt=AttachedAt,
                    AttachedBy=AttachedBy,
                    AttachedToFriendlyName=AttachedToFriendlyName,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_policy_attachment_attached_to_type_attached_to_id_get_oapg(
        self: api_client.Api,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
         Gets all attachments for an org by type and id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_attached_to_type,
            request_path_attached_to_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

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


class V1PolicyAttachmentAttachedToTypeAttachedToIdGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_policy_attachment_attached_to_type_attached_to_id_get(
        self: BaseApi,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_policy_attachment_attached_to_type_attached_to_id_get_oapg(
            header_params=header_params,
            path_params=path_params,
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_policy_attachment_attached_to_type_attached_to_id_get_oapg(
            header_params=header_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


