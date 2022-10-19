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
OrgidSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'orgid': typing.Union[OrgidSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_orgid = api_client.QueryParameter(
    name="orgid",
    style=api_client.ParameterStyle.FORM,
    schema=OrgidSchema,
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
            OrgID = schemas.StrSchema
            OrgName = schemas.StrSchema
            MetadataURL = schemas.StrSchema
            IDPIssuerURL = schemas.StrSchema
            CallbackURL = schemas.StrSchema
            RawMetadata = schemas.StrSchema
            SPMetadataURL = schemas.StrSchema
            
            
            class SPCertificateInfo(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        Expires = schemas.IntSchema
                        Issuer = schemas.StrSchema
                        Certificate = schemas.StrSchema
                        SPIssuer = schemas.StrSchema
                        __annotations__ = {
                            "Expires": Expires,
                            "Issuer": Issuer,
                            "Certificate": Certificate,
                            "SPIssuer": SPIssuer,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Expires"]) -> MetaOapg.properties.Expires: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Issuer"]) -> MetaOapg.properties.Issuer: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Certificate"]) -> MetaOapg.properties.Certificate: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["SPIssuer"]) -> MetaOapg.properties.SPIssuer: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["Expires", "Issuer", "Certificate", "SPIssuer", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Expires"]) -> typing.Union[MetaOapg.properties.Expires, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Issuer"]) -> typing.Union[MetaOapg.properties.Issuer, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Certificate"]) -> typing.Union[MetaOapg.properties.Certificate, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["SPIssuer"]) -> typing.Union[MetaOapg.properties.SPIssuer, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Expires", "Issuer", "Certificate", "SPIssuer", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    Expires: typing.Union[MetaOapg.properties.Expires, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    Issuer: typing.Union[MetaOapg.properties.Issuer, str, schemas.Unset] = schemas.unset,
                    Certificate: typing.Union[MetaOapg.properties.Certificate, str, schemas.Unset] = schemas.unset,
                    SPIssuer: typing.Union[MetaOapg.properties.SPIssuer, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'SPCertificateInfo':
                    return super().__new__(
                        cls,
                        *args,
                        Expires=Expires,
                        Issuer=Issuer,
                        Certificate=Certificate,
                        SPIssuer=SPIssuer,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "OrgID": OrgID,
                "OrgName": OrgName,
                "MetadataURL": MetadataURL,
                "IDPIssuerURL": IDPIssuerURL,
                "CallbackURL": CallbackURL,
                "RawMetadata": RawMetadata,
                "SPMetadataURL": SPMetadataURL,
                "SPCertificateInfo": SPCertificateInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgID"]) -> MetaOapg.properties.OrgID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgName"]) -> MetaOapg.properties.OrgName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MetadataURL"]) -> MetaOapg.properties.MetadataURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IDPIssuerURL"]) -> MetaOapg.properties.IDPIssuerURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CallbackURL"]) -> MetaOapg.properties.CallbackURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RawMetadata"]) -> MetaOapg.properties.RawMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SPMetadataURL"]) -> MetaOapg.properties.SPMetadataURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SPCertificateInfo"]) -> MetaOapg.properties.SPCertificateInfo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OrgID", "OrgName", "MetadataURL", "IDPIssuerURL", "CallbackURL", "RawMetadata", "SPMetadataURL", "SPCertificateInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgID"]) -> typing.Union[MetaOapg.properties.OrgID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgName"]) -> typing.Union[MetaOapg.properties.OrgName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MetadataURL"]) -> typing.Union[MetaOapg.properties.MetadataURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IDPIssuerURL"]) -> typing.Union[MetaOapg.properties.IDPIssuerURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CallbackURL"]) -> typing.Union[MetaOapg.properties.CallbackURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RawMetadata"]) -> typing.Union[MetaOapg.properties.RawMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SPMetadataURL"]) -> typing.Union[MetaOapg.properties.SPMetadataURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SPCertificateInfo"]) -> typing.Union[MetaOapg.properties.SPCertificateInfo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OrgID", "OrgName", "MetadataURL", "IDPIssuerURL", "CallbackURL", "RawMetadata", "SPMetadataURL", "SPCertificateInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        OrgID: typing.Union[MetaOapg.properties.OrgID, str, schemas.Unset] = schemas.unset,
        OrgName: typing.Union[MetaOapg.properties.OrgName, str, schemas.Unset] = schemas.unset,
        MetadataURL: typing.Union[MetaOapg.properties.MetadataURL, str, schemas.Unset] = schemas.unset,
        IDPIssuerURL: typing.Union[MetaOapg.properties.IDPIssuerURL, str, schemas.Unset] = schemas.unset,
        CallbackURL: typing.Union[MetaOapg.properties.CallbackURL, str, schemas.Unset] = schemas.unset,
        RawMetadata: typing.Union[MetaOapg.properties.RawMetadata, str, schemas.Unset] = schemas.unset,
        SPMetadataURL: typing.Union[MetaOapg.properties.SPMetadataURL, str, schemas.Unset] = schemas.unset,
        SPCertificateInfo: typing.Union[MetaOapg.properties.SPCertificateInfo, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            OrgID=OrgID,
            OrgName=OrgName,
            MetadataURL=MetadataURL,
            IDPIssuerURL=IDPIssuerURL,
            CallbackURL=CallbackURL,
            RawMetadata=RawMetadata,
            SPMetadataURL=SPMetadataURL,
            SPCertificateInfo=SPCertificateInfo,
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
    '400': _response_for_400,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v1_api_v1_admin_saml_get_oapg(
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
         Get the admin SAML Sign-on Settings for an organization
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_orgid,
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


class V1ApiV1AdminSamlGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v1_api_v1_admin_saml_get(
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
        return self._v1_api_v1_admin_saml_get_oapg(
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
        return self._v1_api_v1_admin_saml_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


