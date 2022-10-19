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
ContentTypeSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Authorization': typing.Union[AuthorizationSchema, str, ],
        'Content-Type': typing.Union[ContentTypeSchema, str, ],
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
request_header_content_type = api_client.HeaderParameter(
    name="Content-Type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentTypeSchema,
)
_auth = [
    'bearerAuthToken',
]


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            OrgName = schemas.StrSchema
            OrgID = schemas.StrSchema
            MDMName = schemas.StrSchema
            MDMConfig = schemas.StrSchema
            IDPName = schemas.StrSchema
            IDPConfig = schemas.StrSchema
            DNSName = schemas.StrSchema
            DNSConfig = schemas.StrSchema
            TrustConfig = schemas.StrSchema
            
            
            class CACerts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CACerts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            CAChain = schemas.StrSchema
            CloakExceptions = schemas.StrSchema
            AsyncAuthEnabled = schemas.IntSchema
            IsTestDrive = schemas.IntSchema
            IsTunnelEnabled = schemas.IntSchema
            Edition = schemas.StrSchema
            ZoneID = schemas.StrSchema
            IsZTCertUpdateEnabled = schemas.IntSchema
            EnduserInactivityThresholdDays = schemas.IntSchema
            IsAutoRenewCertsEnabled = schemas.IntSchema
            IsZTUpnCertEnabled = schemas.IntSchema
            AutoRenewCertExpiryWindowDays = schemas.IntSchema
            CreatedAt = schemas.IntSchema
            
            
            class OnboardingState(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        state = schemas.StrSchema
                        type = schemas.StrSchema
                        connectorId = schemas.StrSchema
                        serviceId = schemas.StrSchema
                        __annotations__ = {
                            "state": state,
                            "type": type,
                            "connectorId": connectorId,
                            "serviceId": serviceId,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["connectorId"]) -> MetaOapg.properties.connectorId: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["serviceId"]) -> MetaOapg.properties.serviceId: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["state", "type", "connectorId", "serviceId", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["connectorId"]) -> typing.Union[MetaOapg.properties.connectorId, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["serviceId"]) -> typing.Union[MetaOapg.properties.serviceId, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["state", "type", "connectorId", "serviceId", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    connectorId: typing.Union[MetaOapg.properties.connectorId, str, schemas.Unset] = schemas.unset,
                    serviceId: typing.Union[MetaOapg.properties.serviceId, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'OnboardingState':
                    return super().__new__(
                        cls,
                        *args,
                        state=state,
                        type=type,
                        connectorId=connectorId,
                        serviceId=serviceId,
                        _configuration=_configuration,
                        **kwargs,
                    )
            SupportMessage = schemas.StrSchema
            SupportLinkTitle = schemas.StrSchema
            SupportLinkUrl = schemas.StrSchema
            __annotations__ = {
                "OrgName": OrgName,
                "OrgID": OrgID,
                "MDMName": MDMName,
                "MDMConfig": MDMConfig,
                "IDPName": IDPName,
                "IDPConfig": IDPConfig,
                "DNSName": DNSName,
                "DNSConfig": DNSConfig,
                "TrustConfig": TrustConfig,
                "CACerts": CACerts,
                "CAChain": CAChain,
                "CloakExceptions": CloakExceptions,
                "AsyncAuthEnabled": AsyncAuthEnabled,
                "IsTestDrive": IsTestDrive,
                "IsTunnelEnabled": IsTunnelEnabled,
                "Edition": Edition,
                "ZoneID": ZoneID,
                "IsZTCertUpdateEnabled": IsZTCertUpdateEnabled,
                "EnduserInactivityThresholdDays": EnduserInactivityThresholdDays,
                "IsAutoRenewCertsEnabled": IsAutoRenewCertsEnabled,
                "IsZTUpnCertEnabled": IsZTUpnCertEnabled,
                "AutoRenewCertExpiryWindowDays": AutoRenewCertExpiryWindowDays,
                "CreatedAt": CreatedAt,
                "OnboardingState": OnboardingState,
                "SupportMessage": SupportMessage,
                "SupportLinkTitle": SupportLinkTitle,
                "SupportLinkUrl": SupportLinkUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgName"]) -> MetaOapg.properties.OrgName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgID"]) -> MetaOapg.properties.OrgID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MDMName"]) -> MetaOapg.properties.MDMName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MDMConfig"]) -> MetaOapg.properties.MDMConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IDPName"]) -> MetaOapg.properties.IDPName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IDPConfig"]) -> MetaOapg.properties.IDPConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DNSName"]) -> MetaOapg.properties.DNSName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DNSConfig"]) -> MetaOapg.properties.DNSConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrustConfig"]) -> MetaOapg.properties.TrustConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CACerts"]) -> MetaOapg.properties.CACerts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CAChain"]) -> MetaOapg.properties.CAChain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CloakExceptions"]) -> MetaOapg.properties.CloakExceptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AsyncAuthEnabled"]) -> MetaOapg.properties.AsyncAuthEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsTestDrive"]) -> MetaOapg.properties.IsTestDrive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsTunnelEnabled"]) -> MetaOapg.properties.IsTunnelEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Edition"]) -> MetaOapg.properties.Edition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ZoneID"]) -> MetaOapg.properties.ZoneID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsZTCertUpdateEnabled"]) -> MetaOapg.properties.IsZTCertUpdateEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnduserInactivityThresholdDays"]) -> MetaOapg.properties.EnduserInactivityThresholdDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsAutoRenewCertsEnabled"]) -> MetaOapg.properties.IsAutoRenewCertsEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsZTUpnCertEnabled"]) -> MetaOapg.properties.IsZTUpnCertEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AutoRenewCertExpiryWindowDays"]) -> MetaOapg.properties.AutoRenewCertExpiryWindowDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedAt"]) -> MetaOapg.properties.CreatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OnboardingState"]) -> MetaOapg.properties.OnboardingState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupportMessage"]) -> MetaOapg.properties.SupportMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupportLinkTitle"]) -> MetaOapg.properties.SupportLinkTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupportLinkUrl"]) -> MetaOapg.properties.SupportLinkUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OrgName", "OrgID", "MDMName", "MDMConfig", "IDPName", "IDPConfig", "DNSName", "DNSConfig", "TrustConfig", "CACerts", "CAChain", "CloakExceptions", "AsyncAuthEnabled", "IsTestDrive", "IsTunnelEnabled", "Edition", "ZoneID", "IsZTCertUpdateEnabled", "EnduserInactivityThresholdDays", "IsAutoRenewCertsEnabled", "IsZTUpnCertEnabled", "AutoRenewCertExpiryWindowDays", "CreatedAt", "OnboardingState", "SupportMessage", "SupportLinkTitle", "SupportLinkUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgName"]) -> typing.Union[MetaOapg.properties.OrgName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgID"]) -> typing.Union[MetaOapg.properties.OrgID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MDMName"]) -> typing.Union[MetaOapg.properties.MDMName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MDMConfig"]) -> typing.Union[MetaOapg.properties.MDMConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IDPName"]) -> typing.Union[MetaOapg.properties.IDPName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IDPConfig"]) -> typing.Union[MetaOapg.properties.IDPConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DNSName"]) -> typing.Union[MetaOapg.properties.DNSName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DNSConfig"]) -> typing.Union[MetaOapg.properties.DNSConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrustConfig"]) -> typing.Union[MetaOapg.properties.TrustConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CACerts"]) -> typing.Union[MetaOapg.properties.CACerts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CAChain"]) -> typing.Union[MetaOapg.properties.CAChain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CloakExceptions"]) -> typing.Union[MetaOapg.properties.CloakExceptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AsyncAuthEnabled"]) -> typing.Union[MetaOapg.properties.AsyncAuthEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsTestDrive"]) -> typing.Union[MetaOapg.properties.IsTestDrive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsTunnelEnabled"]) -> typing.Union[MetaOapg.properties.IsTunnelEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Edition"]) -> typing.Union[MetaOapg.properties.Edition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ZoneID"]) -> typing.Union[MetaOapg.properties.ZoneID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsZTCertUpdateEnabled"]) -> typing.Union[MetaOapg.properties.IsZTCertUpdateEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnduserInactivityThresholdDays"]) -> typing.Union[MetaOapg.properties.EnduserInactivityThresholdDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsAutoRenewCertsEnabled"]) -> typing.Union[MetaOapg.properties.IsAutoRenewCertsEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsZTUpnCertEnabled"]) -> typing.Union[MetaOapg.properties.IsZTUpnCertEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AutoRenewCertExpiryWindowDays"]) -> typing.Union[MetaOapg.properties.AutoRenewCertExpiryWindowDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedAt"]) -> typing.Union[MetaOapg.properties.CreatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OnboardingState"]) -> typing.Union[MetaOapg.properties.OnboardingState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupportMessage"]) -> typing.Union[MetaOapg.properties.SupportMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupportLinkTitle"]) -> typing.Union[MetaOapg.properties.SupportLinkTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupportLinkUrl"]) -> typing.Union[MetaOapg.properties.SupportLinkUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OrgName", "OrgID", "MDMName", "MDMConfig", "IDPName", "IDPConfig", "DNSName", "DNSConfig", "TrustConfig", "CACerts", "CAChain", "CloakExceptions", "AsyncAuthEnabled", "IsTestDrive", "IsTunnelEnabled", "Edition", "ZoneID", "IsZTCertUpdateEnabled", "EnduserInactivityThresholdDays", "IsAutoRenewCertsEnabled", "IsZTUpnCertEnabled", "AutoRenewCertExpiryWindowDays", "CreatedAt", "OnboardingState", "SupportMessage", "SupportLinkTitle", "SupportLinkUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        OrgName: typing.Union[MetaOapg.properties.OrgName, str, schemas.Unset] = schemas.unset,
        OrgID: typing.Union[MetaOapg.properties.OrgID, str, schemas.Unset] = schemas.unset,
        MDMName: typing.Union[MetaOapg.properties.MDMName, str, schemas.Unset] = schemas.unset,
        MDMConfig: typing.Union[MetaOapg.properties.MDMConfig, str, schemas.Unset] = schemas.unset,
        IDPName: typing.Union[MetaOapg.properties.IDPName, str, schemas.Unset] = schemas.unset,
        IDPConfig: typing.Union[MetaOapg.properties.IDPConfig, str, schemas.Unset] = schemas.unset,
        DNSName: typing.Union[MetaOapg.properties.DNSName, str, schemas.Unset] = schemas.unset,
        DNSConfig: typing.Union[MetaOapg.properties.DNSConfig, str, schemas.Unset] = schemas.unset,
        TrustConfig: typing.Union[MetaOapg.properties.TrustConfig, str, schemas.Unset] = schemas.unset,
        CACerts: typing.Union[MetaOapg.properties.CACerts, list, tuple, schemas.Unset] = schemas.unset,
        CAChain: typing.Union[MetaOapg.properties.CAChain, str, schemas.Unset] = schemas.unset,
        CloakExceptions: typing.Union[MetaOapg.properties.CloakExceptions, str, schemas.Unset] = schemas.unset,
        AsyncAuthEnabled: typing.Union[MetaOapg.properties.AsyncAuthEnabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsTestDrive: typing.Union[MetaOapg.properties.IsTestDrive, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsTunnelEnabled: typing.Union[MetaOapg.properties.IsTunnelEnabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Edition: typing.Union[MetaOapg.properties.Edition, str, schemas.Unset] = schemas.unset,
        ZoneID: typing.Union[MetaOapg.properties.ZoneID, str, schemas.Unset] = schemas.unset,
        IsZTCertUpdateEnabled: typing.Union[MetaOapg.properties.IsZTCertUpdateEnabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        EnduserInactivityThresholdDays: typing.Union[MetaOapg.properties.EnduserInactivityThresholdDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsAutoRenewCertsEnabled: typing.Union[MetaOapg.properties.IsAutoRenewCertsEnabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsZTUpnCertEnabled: typing.Union[MetaOapg.properties.IsZTUpnCertEnabled, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        AutoRenewCertExpiryWindowDays: typing.Union[MetaOapg.properties.AutoRenewCertExpiryWindowDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CreatedAt: typing.Union[MetaOapg.properties.CreatedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        OnboardingState: typing.Union[MetaOapg.properties.OnboardingState, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        SupportMessage: typing.Union[MetaOapg.properties.SupportMessage, str, schemas.Unset] = schemas.unset,
        SupportLinkTitle: typing.Union[MetaOapg.properties.SupportLinkTitle, str, schemas.Unset] = schemas.unset,
        SupportLinkUrl: typing.Union[MetaOapg.properties.SupportLinkUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            OrgName=OrgName,
            OrgID=OrgID,
            MDMName=MDMName,
            MDMConfig=MDMConfig,
            IDPName=IDPName,
            IDPConfig=IDPConfig,
            DNSName=DNSName,
            DNSConfig=DNSConfig,
            TrustConfig=TrustConfig,
            CACerts=CACerts,
            CAChain=CAChain,
            CloakExceptions=CloakExceptions,
            AsyncAuthEnabled=AsyncAuthEnabled,
            IsTestDrive=IsTestDrive,
            IsTunnelEnabled=IsTunnelEnabled,
            Edition=Edition,
            ZoneID=ZoneID,
            IsZTCertUpdateEnabled=IsZTCertUpdateEnabled,
            EnduserInactivityThresholdDays=EnduserInactivityThresholdDays,
            IsAutoRenewCertsEnabled=IsAutoRenewCertsEnabled,
            IsZTUpnCertEnabled=IsZTUpnCertEnabled,
            AutoRenewCertExpiryWindowDays=AutoRenewCertExpiryWindowDays,
            CreatedAt=CreatedAt,
            OnboardingState=OnboardingState,
            SupportMessage=SupportMessage,
            SupportLinkTitle=SupportLinkTitle,
            SupportLinkUrl=SupportLinkUrl,
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

    def _v1_org_details_get_oapg(
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


class V1OrgDetailsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_org_details_get(
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
        return self._v1_org_details_get_oapg(
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
        return self._v1_org_details_get_oapg(
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


