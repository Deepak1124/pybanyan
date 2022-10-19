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
DeviceIDSchema = schemas.StrSchema
EmailSchema = schemas.StrSchema
ServiceIDSchema = schemas.StrSchema
StartTimeSchema = schemas.StrSchema
# header params
AuthorizationSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    ServiceID = schemas.StrSchema
                    ServiceName = schemas.StrSchema
                    Name = schemas.StrSchema
                    Email = schemas.StrSchema
                    DeviceID = schemas.StrSchema
                    SerialNumber = schemas.StrSchema
                    Model = schemas.StrSchema
                    Roles = schemas.IntSchema
                    
                    
                    class LastAuthorizedEvent(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                Timestamp = schemas.IntSchema
                                EventType = schemas.StrSchema
                                EventAction = schemas.StrSchema
                                ServiceID = schemas.StrSchema
                                ServiceName = schemas.StrSchema
                                ClusterID = schemas.StrSchema
                                ClusterName = schemas.StrSchema
                                EventJSON = schemas.StrSchema
                                __annotations__ = {
                                    "Timestamp": Timestamp,
                                    "EventType": EventType,
                                    "EventAction": EventAction,
                                    "ServiceID": ServiceID,
                                    "ServiceName": ServiceName,
                                    "ClusterID": ClusterID,
                                    "ClusterName": ClusterName,
                                    "EventJSON": EventJSON,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Timestamp"]) -> MetaOapg.properties.Timestamp: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventType"]) -> MetaOapg.properties.EventType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventAction"]) -> MetaOapg.properties.EventAction: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceID"]) -> MetaOapg.properties.ServiceID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceName"]) -> MetaOapg.properties.ServiceName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ClusterID"]) -> MetaOapg.properties.ClusterID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ClusterName"]) -> MetaOapg.properties.ClusterName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventJSON"]) -> MetaOapg.properties.EventJSON: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["Timestamp", "EventType", "EventAction", "ServiceID", "ServiceName", "ClusterID", "ClusterName", "EventJSON", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Timestamp"]) -> typing.Union[MetaOapg.properties.Timestamp, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventType"]) -> typing.Union[MetaOapg.properties.EventType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventAction"]) -> typing.Union[MetaOapg.properties.EventAction, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceID"]) -> typing.Union[MetaOapg.properties.ServiceID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceName"]) -> typing.Union[MetaOapg.properties.ServiceName, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ClusterID"]) -> typing.Union[MetaOapg.properties.ClusterID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ClusterName"]) -> typing.Union[MetaOapg.properties.ClusterName, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventJSON"]) -> typing.Union[MetaOapg.properties.EventJSON, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Timestamp", "EventType", "EventAction", "ServiceID", "ServiceName", "ClusterID", "ClusterName", "EventJSON", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            Timestamp: typing.Union[MetaOapg.properties.Timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            EventType: typing.Union[MetaOapg.properties.EventType, str, schemas.Unset] = schemas.unset,
                            EventAction: typing.Union[MetaOapg.properties.EventAction, str, schemas.Unset] = schemas.unset,
                            ServiceID: typing.Union[MetaOapg.properties.ServiceID, str, schemas.Unset] = schemas.unset,
                            ServiceName: typing.Union[MetaOapg.properties.ServiceName, str, schemas.Unset] = schemas.unset,
                            ClusterID: typing.Union[MetaOapg.properties.ClusterID, str, schemas.Unset] = schemas.unset,
                            ClusterName: typing.Union[MetaOapg.properties.ClusterName, str, schemas.Unset] = schemas.unset,
                            EventJSON: typing.Union[MetaOapg.properties.EventJSON, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'LastAuthorizedEvent':
                            return super().__new__(
                                cls,
                                *args,
                                Timestamp=Timestamp,
                                EventType=EventType,
                                EventAction=EventAction,
                                ServiceID=ServiceID,
                                ServiceName=ServiceName,
                                ClusterID=ClusterID,
                                ClusterName=ClusterName,
                                EventJSON=EventJSON,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class LastUnauthorizedEvent(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                Timestamp = schemas.IntSchema
                                EventType = schemas.StrSchema
                                EventAction = schemas.StrSchema
                                ServiceID = schemas.StrSchema
                                ServiceName = schemas.StrSchema
                                ClusterID = schemas.StrSchema
                                ClusterName = schemas.StrSchema
                                EventJSON = schemas.StrSchema
                                __annotations__ = {
                                    "Timestamp": Timestamp,
                                    "EventType": EventType,
                                    "EventAction": EventAction,
                                    "ServiceID": ServiceID,
                                    "ServiceName": ServiceName,
                                    "ClusterID": ClusterID,
                                    "ClusterName": ClusterName,
                                    "EventJSON": EventJSON,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Timestamp"]) -> MetaOapg.properties.Timestamp: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventType"]) -> MetaOapg.properties.EventType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventAction"]) -> MetaOapg.properties.EventAction: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceID"]) -> MetaOapg.properties.ServiceID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ServiceName"]) -> MetaOapg.properties.ServiceName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ClusterID"]) -> MetaOapg.properties.ClusterID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ClusterName"]) -> MetaOapg.properties.ClusterName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["EventJSON"]) -> MetaOapg.properties.EventJSON: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["Timestamp", "EventType", "EventAction", "ServiceID", "ServiceName", "ClusterID", "ClusterName", "EventJSON", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Timestamp"]) -> typing.Union[MetaOapg.properties.Timestamp, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventType"]) -> typing.Union[MetaOapg.properties.EventType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventAction"]) -> typing.Union[MetaOapg.properties.EventAction, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceID"]) -> typing.Union[MetaOapg.properties.ServiceID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ServiceName"]) -> typing.Union[MetaOapg.properties.ServiceName, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ClusterID"]) -> typing.Union[MetaOapg.properties.ClusterID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ClusterName"]) -> typing.Union[MetaOapg.properties.ClusterName, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["EventJSON"]) -> typing.Union[MetaOapg.properties.EventJSON, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Timestamp", "EventType", "EventAction", "ServiceID", "ServiceName", "ClusterID", "ClusterName", "EventJSON", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            Timestamp: typing.Union[MetaOapg.properties.Timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            EventType: typing.Union[MetaOapg.properties.EventType, str, schemas.Unset] = schemas.unset,
                            EventAction: typing.Union[MetaOapg.properties.EventAction, str, schemas.Unset] = schemas.unset,
                            ServiceID: typing.Union[MetaOapg.properties.ServiceID, str, schemas.Unset] = schemas.unset,
                            ServiceName: typing.Union[MetaOapg.properties.ServiceName, str, schemas.Unset] = schemas.unset,
                            ClusterID: typing.Union[MetaOapg.properties.ClusterID, str, schemas.Unset] = schemas.unset,
                            ClusterName: typing.Union[MetaOapg.properties.ClusterName, str, schemas.Unset] = schemas.unset,
                            EventJSON: typing.Union[MetaOapg.properties.EventJSON, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'LastUnauthorizedEvent':
                            return super().__new__(
                                cls,
                                *args,
                                Timestamp=Timestamp,
                                EventType=EventType,
                                EventAction=EventAction,
                                ServiceID=ServiceID,
                                ServiceName=ServiceName,
                                ClusterID=ClusterID,
                                ClusterName=ClusterName,
                                EventJSON=EventJSON,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "ServiceID": ServiceID,
                        "ServiceName": ServiceName,
                        "Name": Name,
                        "Email": Email,
                        "DeviceID": DeviceID,
                        "SerialNumber": SerialNumber,
                        "Model": Model,
                        "Roles": Roles,
                        "LastAuthorizedEvent": LastAuthorizedEvent,
                        "LastUnauthorizedEvent": LastUnauthorizedEvent,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ServiceID"]) -> MetaOapg.properties.ServiceID: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ServiceName"]) -> MetaOapg.properties.ServiceName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DeviceID"]) -> MetaOapg.properties.DeviceID: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["SerialNumber"]) -> MetaOapg.properties.SerialNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Model"]) -> MetaOapg.properties.Model: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Roles"]) -> MetaOapg.properties.Roles: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["LastAuthorizedEvent"]) -> MetaOapg.properties.LastAuthorizedEvent: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["LastUnauthorizedEvent"]) -> MetaOapg.properties.LastUnauthorizedEvent: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["ServiceID", "ServiceName", "Name", "Email", "DeviceID", "SerialNumber", "Model", "Roles", "LastAuthorizedEvent", "LastUnauthorizedEvent", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ServiceID"]) -> typing.Union[MetaOapg.properties.ServiceID, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ServiceName"]) -> typing.Union[MetaOapg.properties.ServiceName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DeviceID"]) -> typing.Union[MetaOapg.properties.DeviceID, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["SerialNumber"]) -> typing.Union[MetaOapg.properties.SerialNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Model"]) -> typing.Union[MetaOapg.properties.Model, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Roles"]) -> typing.Union[MetaOapg.properties.Roles, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["LastAuthorizedEvent"]) -> typing.Union[MetaOapg.properties.LastAuthorizedEvent, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["LastUnauthorizedEvent"]) -> typing.Union[MetaOapg.properties.LastUnauthorizedEvent, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ServiceID", "ServiceName", "Name", "Email", "DeviceID", "SerialNumber", "Model", "Roles", "LastAuthorizedEvent", "LastUnauthorizedEvent", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                ServiceID: typing.Union[MetaOapg.properties.ServiceID, str, schemas.Unset] = schemas.unset,
                ServiceName: typing.Union[MetaOapg.properties.ServiceName, str, schemas.Unset] = schemas.unset,
                Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
                Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
                DeviceID: typing.Union[MetaOapg.properties.DeviceID, str, schemas.Unset] = schemas.unset,
                SerialNumber: typing.Union[MetaOapg.properties.SerialNumber, str, schemas.Unset] = schemas.unset,
                Model: typing.Union[MetaOapg.properties.Model, str, schemas.Unset] = schemas.unset,
                Roles: typing.Union[MetaOapg.properties.Roles, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                LastAuthorizedEvent: typing.Union[MetaOapg.properties.LastAuthorizedEvent, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                LastUnauthorizedEvent: typing.Union[MetaOapg.properties.LastUnauthorizedEvent, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    ServiceID=ServiceID,
                    ServiceName=ServiceName,
                    Name=Name,
                    Email=Email,
                    DeviceID=DeviceID,
                    SerialNumber=SerialNumber,
                    Model=Model,
                    Roles=Roles,
                    LastAuthorizedEvent=LastAuthorizedEvent,
                    LastUnauthorizedEvent=LastUnauthorizedEvent,
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

    def _v1_access_activity_get_oapg(
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
         Returns data for all access activities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_device_id,
            request_query_email,
            request_query_service_id,
            request_query_start_time,
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


class V1AccessActivityGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_access_activity_get(
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
        return self._v1_access_activity_get_oapg(
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
        return self._v1_access_activity_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


