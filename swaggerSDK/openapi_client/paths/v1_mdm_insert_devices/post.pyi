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
Model2ContentTypeSchema = schemas.StrSchema
Model3XServerLocationSchema = schemas.StrSchema
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class EndUserDevices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                Name = schemas.StrSchema
                                Email = schemas.StrSchema
                                SerialNumber = schemas.StrSchema
                                Model = schemas.StrSchema
                                Ownership = schemas.StrSchema
                                Platform = schemas.StrSchema
                                Architecture = schemas.StrSchema
                                __annotations__ = {
                                    "Name": Name,
                                    "Email": Email,
                                    "SerialNumber": SerialNumber,
                                    "Model": Model,
                                    "Ownership": Ownership,
                                    "Platform": Platform,
                                    "Architecture": Architecture,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["SerialNumber"]) -> MetaOapg.properties.SerialNumber: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Model"]) -> MetaOapg.properties.Model: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Ownership"]) -> MetaOapg.properties.Ownership: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Platform"]) -> MetaOapg.properties.Platform: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Architecture"]) -> MetaOapg.properties.Architecture: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name", "Email", "SerialNumber", "Model", "Ownership", "Platform", "Architecture", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["SerialNumber"]) -> typing.Union[MetaOapg.properties.SerialNumber, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Model"]) -> typing.Union[MetaOapg.properties.Model, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Ownership"]) -> typing.Union[MetaOapg.properties.Ownership, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Platform"]) -> typing.Union[MetaOapg.properties.Platform, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Architecture"]) -> typing.Union[MetaOapg.properties.Architecture, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name", "Email", "SerialNumber", "Model", "Ownership", "Platform", "Architecture", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
                            Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
                            SerialNumber: typing.Union[MetaOapg.properties.SerialNumber, str, schemas.Unset] = schemas.unset,
                            Model: typing.Union[MetaOapg.properties.Model, str, schemas.Unset] = schemas.unset,
                            Ownership: typing.Union[MetaOapg.properties.Ownership, str, schemas.Unset] = schemas.unset,
                            Platform: typing.Union[MetaOapg.properties.Platform, str, schemas.Unset] = schemas.unset,
                            Architecture: typing.Union[MetaOapg.properties.Architecture, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                Name=Name,
                                Email=Email,
                                SerialNumber=SerialNumber,
                                Model=Model,
                                Ownership=Ownership,
                                Platform=Platform,
                                Architecture=Architecture,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EndUserDevices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "EndUserDevices": EndUserDevices,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndUserDevices"]) -> MetaOapg.properties.EndUserDevices: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EndUserDevices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndUserDevices"]) -> typing.Union[MetaOapg.properties.EndUserDevices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EndUserDevices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        EndUserDevices: typing.Union[MetaOapg.properties.EndUserDevices, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            EndUserDevices=EndUserDevices,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            Message = schemas.StrSchema
            __annotations__ = {
                "Message": Message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Message"]) -> typing.Union[MetaOapg.properties.Message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Message: typing.Union[MetaOapg.properties.Message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            Message=Message,
            _configuration=_configuration,
            **kwargs,
        )
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_mdm_insert_devices_post_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, ],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
         Insert End User Devices
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
            request_header__2__content_type,
            request_header__3__x_server_location,
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

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_any_type.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
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


class V1MdmInsertDevicesPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_mdm_insert_devices_post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, ],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_mdm_insert_devices_post_oapg(
            body=body,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, ],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._v1_mdm_insert_devices_post_oapg(
            body=body,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


