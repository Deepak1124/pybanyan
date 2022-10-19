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
LimitSchema = schemas.IntSchema
SkipSchema = schemas.IntSchema
SecurityRoleIdSchema = schemas.StrSchema
EmailSchema = schemas.StrSchema
SerialnumberSchema = schemas.StrSchema
ExactEmailSchema = schemas.StrSchema
ExactSerialNumberSchema = schemas.StrSchema
# header params
AuthorizationSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class enduserdevices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class enduser(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            ID = schemas.StrSchema
                                            OrgID = schemas.StrSchema
                                            Email = schemas.StrSchema
                                            Name = schemas.StrSchema
                                            CreatedAt = schemas.IntSchema
                                            __annotations__ = {
                                                "ID": ID,
                                                "OrgID": OrgID,
                                                "Email": Email,
                                                "Name": Name,
                                                "CreatedAt": CreatedAt,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["OrgID"]) -> MetaOapg.properties.OrgID: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["CreatedAt"]) -> MetaOapg.properties.CreatedAt: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ID", "OrgID", "Email", "Name", "CreatedAt", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> typing.Union[MetaOapg.properties.ID, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["OrgID"]) -> typing.Union[MetaOapg.properties.OrgID, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["CreatedAt"]) -> typing.Union[MetaOapg.properties.CreatedAt, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ID", "OrgID", "Email", "Name", "CreatedAt", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        ID: typing.Union[MetaOapg.properties.ID, str, schemas.Unset] = schemas.unset,
                                        OrgID: typing.Union[MetaOapg.properties.OrgID, str, schemas.Unset] = schemas.unset,
                                        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
                                        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
                                        CreatedAt: typing.Union[MetaOapg.properties.CreatedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'enduser':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            ID=ID,
                                            OrgID=OrgID,
                                            Email=Email,
                                            Name=Name,
                                            CreatedAt=CreatedAt,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class device(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            ID = schemas.StrSchema
                                            OrgID = schemas.StrSchema
                                            SerialNumber = schemas.StrSchema
                                            Name = schemas.StrSchema
                                            Model = schemas.StrSchema
                                            Ownership = schemas.StrSchema
                                            Platform = schemas.StrSchema
                                            Architecture = schemas.StrSchema
                                            Source = schemas.StrSchema
                                            Banned = schemas.IntSchema
                                            OS = schemas.StrSchema
                                            MDMPresent = schemas.IntSchema
                                            MDMVendorName = schemas.StrSchema
                                            MDMVendorUDID = schemas.StrSchema
                                            LastMDMDataSyncedAt = schemas.IntSchema
                                            MDMCompliant = schemas.StrSchema
                                            AppVersion = schemas.StrSchema
                                            CreatedAt = schemas.IntSchema
                                            __annotations__ = {
                                                "ID": ID,
                                                "OrgID": OrgID,
                                                "SerialNumber": SerialNumber,
                                                "Name": Name,
                                                "Model": Model,
                                                "Ownership": Ownership,
                                                "Platform": Platform,
                                                "Architecture": Architecture,
                                                "Source": Source,
                                                "Banned": Banned,
                                                "OS": OS,
                                                "MDMPresent": MDMPresent,
                                                "MDMVendorName": MDMVendorName,
                                                "MDMVendorUDID": MDMVendorUDID,
                                                "LastMDMDataSyncedAt": LastMDMDataSyncedAt,
                                                "MDMCompliant": MDMCompliant,
                                                "AppVersion": AppVersion,
                                                "CreatedAt": CreatedAt,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["OrgID"]) -> MetaOapg.properties.OrgID: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["SerialNumber"]) -> MetaOapg.properties.SerialNumber: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Model"]) -> MetaOapg.properties.Model: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Ownership"]) -> MetaOapg.properties.Ownership: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Platform"]) -> MetaOapg.properties.Platform: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Architecture"]) -> MetaOapg.properties.Architecture: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Source"]) -> MetaOapg.properties.Source: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Banned"]) -> MetaOapg.properties.Banned: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["OS"]) -> MetaOapg.properties.OS: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["MDMPresent"]) -> MetaOapg.properties.MDMPresent: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["MDMVendorName"]) -> MetaOapg.properties.MDMVendorName: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["MDMVendorUDID"]) -> MetaOapg.properties.MDMVendorUDID: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["LastMDMDataSyncedAt"]) -> MetaOapg.properties.LastMDMDataSyncedAt: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["MDMCompliant"]) -> MetaOapg.properties.MDMCompliant: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["AppVersion"]) -> MetaOapg.properties.AppVersion: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["CreatedAt"]) -> MetaOapg.properties.CreatedAt: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ID", "OrgID", "SerialNumber", "Name", "Model", "Ownership", "Platform", "Architecture", "Source", "Banned", "OS", "MDMPresent", "MDMVendorName", "MDMVendorUDID", "LastMDMDataSyncedAt", "MDMCompliant", "AppVersion", "CreatedAt", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> typing.Union[MetaOapg.properties.ID, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["OrgID"]) -> typing.Union[MetaOapg.properties.OrgID, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["SerialNumber"]) -> typing.Union[MetaOapg.properties.SerialNumber, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Model"]) -> typing.Union[MetaOapg.properties.Model, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Ownership"]) -> typing.Union[MetaOapg.properties.Ownership, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Platform"]) -> typing.Union[MetaOapg.properties.Platform, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Architecture"]) -> typing.Union[MetaOapg.properties.Architecture, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Source"]) -> typing.Union[MetaOapg.properties.Source, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Banned"]) -> typing.Union[MetaOapg.properties.Banned, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["OS"]) -> typing.Union[MetaOapg.properties.OS, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["MDMPresent"]) -> typing.Union[MetaOapg.properties.MDMPresent, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["MDMVendorName"]) -> typing.Union[MetaOapg.properties.MDMVendorName, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["MDMVendorUDID"]) -> typing.Union[MetaOapg.properties.MDMVendorUDID, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["LastMDMDataSyncedAt"]) -> typing.Union[MetaOapg.properties.LastMDMDataSyncedAt, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["MDMCompliant"]) -> typing.Union[MetaOapg.properties.MDMCompliant, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["AppVersion"]) -> typing.Union[MetaOapg.properties.AppVersion, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["CreatedAt"]) -> typing.Union[MetaOapg.properties.CreatedAt, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ID", "OrgID", "SerialNumber", "Name", "Model", "Ownership", "Platform", "Architecture", "Source", "Banned", "OS", "MDMPresent", "MDMVendorName", "MDMVendorUDID", "LastMDMDataSyncedAt", "MDMCompliant", "AppVersion", "CreatedAt", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        ID: typing.Union[MetaOapg.properties.ID, str, schemas.Unset] = schemas.unset,
                                        OrgID: typing.Union[MetaOapg.properties.OrgID, str, schemas.Unset] = schemas.unset,
                                        SerialNumber: typing.Union[MetaOapg.properties.SerialNumber, str, schemas.Unset] = schemas.unset,
                                        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
                                        Model: typing.Union[MetaOapg.properties.Model, str, schemas.Unset] = schemas.unset,
                                        Ownership: typing.Union[MetaOapg.properties.Ownership, str, schemas.Unset] = schemas.unset,
                                        Platform: typing.Union[MetaOapg.properties.Platform, str, schemas.Unset] = schemas.unset,
                                        Architecture: typing.Union[MetaOapg.properties.Architecture, str, schemas.Unset] = schemas.unset,
                                        Source: typing.Union[MetaOapg.properties.Source, str, schemas.Unset] = schemas.unset,
                                        Banned: typing.Union[MetaOapg.properties.Banned, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                        OS: typing.Union[MetaOapg.properties.OS, str, schemas.Unset] = schemas.unset,
                                        MDMPresent: typing.Union[MetaOapg.properties.MDMPresent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                        MDMVendorName: typing.Union[MetaOapg.properties.MDMVendorName, str, schemas.Unset] = schemas.unset,
                                        MDMVendorUDID: typing.Union[MetaOapg.properties.MDMVendorUDID, str, schemas.Unset] = schemas.unset,
                                        LastMDMDataSyncedAt: typing.Union[MetaOapg.properties.LastMDMDataSyncedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                        MDMCompliant: typing.Union[MetaOapg.properties.MDMCompliant, str, schemas.Unset] = schemas.unset,
                                        AppVersion: typing.Union[MetaOapg.properties.AppVersion, str, schemas.Unset] = schemas.unset,
                                        CreatedAt: typing.Union[MetaOapg.properties.CreatedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'device':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            ID=ID,
                                            OrgID=OrgID,
                                            SerialNumber=SerialNumber,
                                            Name=Name,
                                            Model=Model,
                                            Ownership=Ownership,
                                            Platform=Platform,
                                            Architecture=Architecture,
                                            Source=Source,
                                            Banned=Banned,
                                            OS=OS,
                                            MDMPresent=MDMPresent,
                                            MDMVendorName=MDMVendorName,
                                            MDMVendorUDID=MDMVendorUDID,
                                            LastMDMDataSyncedAt=LastMDMDataSyncedAt,
                                            MDMCompliant=MDMCompliant,
                                            AppVersion=AppVersion,
                                            CreatedAt=CreatedAt,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "enduser": enduser,
                                    "device": device,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["enduser"]) -> MetaOapg.properties.enduser: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["device"]) -> MetaOapg.properties.device: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["enduser", "device", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["enduser"]) -> typing.Union[MetaOapg.properties.enduser, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["device"]) -> typing.Union[MetaOapg.properties.device, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enduser", "device", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            enduser: typing.Union[MetaOapg.properties.enduser, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            device: typing.Union[MetaOapg.properties.device, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                enduser=enduser,
                                device=device,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enduserdevices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            count = schemas.IntSchema
            __annotations__ = {
                "enduserdevices": enduserdevices,
                "count": count,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enduserdevices"]) -> MetaOapg.properties.enduserdevices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enduserdevices", "count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enduserdevices"]) -> typing.Union[MetaOapg.properties.enduserdevices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enduserdevices", "count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        enduserdevices: typing.Union[MetaOapg.properties.enduserdevices, list, tuple, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            enduserdevices=enduserdevices,
            count=count,
            _configuration=_configuration,
            **kwargs,
        )
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_security_roles_enduser_devices_get_oapg(
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
         List Enduser and Device pairs for given role id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_skip,
            request_query_security_role_id,
            request_query_email,
            request_query_serialnumber,
            request_query_exact_email,
            request_query_exact_serial_number,
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


class V1SecurityRolesEnduserDevicesGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_security_roles_enduser_devices_get(
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
        return self._v1_security_roles_enduser_devices_get_oapg(
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
        return self._v1_security_roles_enduser_devices_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


