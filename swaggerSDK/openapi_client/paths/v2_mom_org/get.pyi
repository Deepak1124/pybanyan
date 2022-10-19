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
NameSchema = schemas.StrSchema
CustomerIdSchema = schemas.StrSchema
TypeSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
SkipSchema = schemas.IntSchema
# header params
AuthorizationSchema = schemas.StrSchema
ContentTypeSchema = schemas.StrSchema


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
                                org_name = schemas.StrSchema
                                org_id = schemas.StrSchema
                                last_updated_at = schemas.IntSchema
                                last_updated_by = schemas.StrSchema
                                edition = schemas.StrSchema
                                created_at = schemas.IntSchema
                                created_by = schemas.StrSchema
                                type = schemas.StrSchema
                                status = schemas.StrSchema
                                customer_id = schemas.StrSchema
                                archived = schemas.BoolSchema
                                global_edge = schemas.BoolSchema
                                private_edge = schemas.BoolSchema
                                
                                
                                class provision_status(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            access_tier = schemas.StrSchema
                                            connector = schemas.StrSchema
                                            org_data = schemas.StrSchema
                                            invite_code = schemas.StrSchema
                                            user_pool_domain = schemas.StrSchema
                                            user_pool = schemas.StrSchema
                                            user = schemas.StrSchema
                                            registered_domain = schemas.StrSchema
                                            shield = schemas.StrSchema
                                            default_groups_user = schemas.StrSchema
                                            user_pool_client = schemas.StrSchema
                                            default_groups_user_pool = schemas.StrSchema
                                            update_user_pool = schemas.StrSchema
                                            __annotations__ = {
                                                "access_tier": access_tier,
                                                "connector": connector,
                                                "org_data": org_data,
                                                "invite_code": invite_code,
                                                "user_pool_domain": user_pool_domain,
                                                "user_pool": user_pool,
                                                "user": user,
                                                "registered_domain": registered_domain,
                                                "shield": shield,
                                                "default_groups_user": default_groups_user,
                                                "user_pool_client": user_pool_client,
                                                "default_groups_user_pool": default_groups_user_pool,
                                                "update_user_pool": update_user_pool,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["access_tier"]) -> MetaOapg.properties.access_tier: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["connector"]) -> MetaOapg.properties.connector: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["org_data"]) -> MetaOapg.properties.org_data: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["invite_code"]) -> MetaOapg.properties.invite_code: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["user_pool_domain"]) -> MetaOapg.properties.user_pool_domain: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["user_pool"]) -> MetaOapg.properties.user_pool: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["registered_domain"]) -> MetaOapg.properties.registered_domain: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["shield"]) -> MetaOapg.properties.shield: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["default_groups_user"]) -> MetaOapg.properties.default_groups_user: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["user_pool_client"]) -> MetaOapg.properties.user_pool_client: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["default_groups_user_pool"]) -> MetaOapg.properties.default_groups_user_pool: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["update_user_pool"]) -> MetaOapg.properties.update_user_pool: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_tier", "connector", "org_data", "invite_code", "user_pool_domain", "user_pool", "user", "registered_domain", "shield", "default_groups_user", "user_pool_client", "default_groups_user_pool", "update_user_pool", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["access_tier"]) -> typing.Union[MetaOapg.properties.access_tier, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["connector"]) -> typing.Union[MetaOapg.properties.connector, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["org_data"]) -> typing.Union[MetaOapg.properties.org_data, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["invite_code"]) -> typing.Union[MetaOapg.properties.invite_code, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["user_pool_domain"]) -> typing.Union[MetaOapg.properties.user_pool_domain, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["user_pool"]) -> typing.Union[MetaOapg.properties.user_pool, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["registered_domain"]) -> typing.Union[MetaOapg.properties.registered_domain, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["shield"]) -> typing.Union[MetaOapg.properties.shield, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["default_groups_user"]) -> typing.Union[MetaOapg.properties.default_groups_user, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["user_pool_client"]) -> typing.Union[MetaOapg.properties.user_pool_client, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["default_groups_user_pool"]) -> typing.Union[MetaOapg.properties.default_groups_user_pool, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["update_user_pool"]) -> typing.Union[MetaOapg.properties.update_user_pool, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_tier", "connector", "org_data", "invite_code", "user_pool_domain", "user_pool", "user", "registered_domain", "shield", "default_groups_user", "user_pool_client", "default_groups_user_pool", "update_user_pool", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        access_tier: typing.Union[MetaOapg.properties.access_tier, str, schemas.Unset] = schemas.unset,
                                        connector: typing.Union[MetaOapg.properties.connector, str, schemas.Unset] = schemas.unset,
                                        org_data: typing.Union[MetaOapg.properties.org_data, str, schemas.Unset] = schemas.unset,
                                        invite_code: typing.Union[MetaOapg.properties.invite_code, str, schemas.Unset] = schemas.unset,
                                        user_pool_domain: typing.Union[MetaOapg.properties.user_pool_domain, str, schemas.Unset] = schemas.unset,
                                        user_pool: typing.Union[MetaOapg.properties.user_pool, str, schemas.Unset] = schemas.unset,
                                        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
                                        registered_domain: typing.Union[MetaOapg.properties.registered_domain, str, schemas.Unset] = schemas.unset,
                                        shield: typing.Union[MetaOapg.properties.shield, str, schemas.Unset] = schemas.unset,
                                        default_groups_user: typing.Union[MetaOapg.properties.default_groups_user, str, schemas.Unset] = schemas.unset,
                                        user_pool_client: typing.Union[MetaOapg.properties.user_pool_client, str, schemas.Unset] = schemas.unset,
                                        default_groups_user_pool: typing.Union[MetaOapg.properties.default_groups_user_pool, str, schemas.Unset] = schemas.unset,
                                        update_user_pool: typing.Union[MetaOapg.properties.update_user_pool, str, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'provision_status':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            access_tier=access_tier,
                                            connector=connector,
                                            org_data=org_data,
                                            invite_code=invite_code,
                                            user_pool_domain=user_pool_domain,
                                            user_pool=user_pool,
                                            user=user,
                                            registered_domain=registered_domain,
                                            shield=shield,
                                            default_groups_user=default_groups_user,
                                            user_pool_client=user_pool_client,
                                            default_groups_user_pool=default_groups_user_pool,
                                            update_user_pool=update_user_pool,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "org_name": org_name,
                                    "org_id": org_id,
                                    "last_updated_at": last_updated_at,
                                    "last_updated_by": last_updated_by,
                                    "edition": edition,
                                    "created_at": created_at,
                                    "created_by": created_by,
                                    "type": type,
                                    "status": status,
                                    "customer_id": customer_id,
                                    "archived": archived,
                                    "global_edge": global_edge,
                                    "private_edge": private_edge,
                                    "provision_status": provision_status,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["org_name"]) -> MetaOapg.properties.org_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_updated_at"]) -> MetaOapg.properties.last_updated_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_updated_by"]) -> MetaOapg.properties.last_updated_by: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["edition"]) -> MetaOapg.properties.edition: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["customer_id"]) -> MetaOapg.properties.customer_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["global_edge"]) -> MetaOapg.properties.global_edge: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["private_edge"]) -> MetaOapg.properties.private_edge: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["provision_status"]) -> MetaOapg.properties.provision_status: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["org_name", "org_id", "last_updated_at", "last_updated_by", "edition", "created_at", "created_by", "type", "status", "customer_id", "archived", "global_edge", "private_edge", "provision_status", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["org_name"]) -> typing.Union[MetaOapg.properties.org_name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_updated_at"]) -> typing.Union[MetaOapg.properties.last_updated_at, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_updated_by"]) -> typing.Union[MetaOapg.properties.last_updated_by, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["edition"]) -> typing.Union[MetaOapg.properties.edition, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["customer_id"]) -> typing.Union[MetaOapg.properties.customer_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["global_edge"]) -> typing.Union[MetaOapg.properties.global_edge, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["private_edge"]) -> typing.Union[MetaOapg.properties.private_edge, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["provision_status"]) -> typing.Union[MetaOapg.properties.provision_status, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["org_name", "org_id", "last_updated_at", "last_updated_by", "edition", "created_at", "created_by", "type", "status", "customer_id", "archived", "global_edge", "private_edge", "provision_status", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            org_name: typing.Union[MetaOapg.properties.org_name, str, schemas.Unset] = schemas.unset,
                            org_id: typing.Union[MetaOapg.properties.org_id, str, schemas.Unset] = schemas.unset,
                            last_updated_at: typing.Union[MetaOapg.properties.last_updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            last_updated_by: typing.Union[MetaOapg.properties.last_updated_by, str, schemas.Unset] = schemas.unset,
                            edition: typing.Union[MetaOapg.properties.edition, str, schemas.Unset] = schemas.unset,
                            created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            created_by: typing.Union[MetaOapg.properties.created_by, str, schemas.Unset] = schemas.unset,
                            type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                            status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                            customer_id: typing.Union[MetaOapg.properties.customer_id, str, schemas.Unset] = schemas.unset,
                            archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
                            global_edge: typing.Union[MetaOapg.properties.global_edge, bool, schemas.Unset] = schemas.unset,
                            private_edge: typing.Union[MetaOapg.properties.private_edge, bool, schemas.Unset] = schemas.unset,
                            provision_status: typing.Union[MetaOapg.properties.provision_status, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                org_name=org_name,
                                org_id=org_id,
                                last_updated_at=last_updated_at,
                                last_updated_by=last_updated_by,
                                edition=edition,
                                created_at=created_at,
                                created_by=created_by,
                                type=type,
                                status=status,
                                customer_id=customer_id,
                                archived=archived,
                                global_edge=global_edge,
                                private_edge=private_edge,
                                provision_status=provision_status,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _v2_mom_org_get_oapg(
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
         Get list of all Orgs
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_customer_id,
            request_query_type,
            request_query_limit,
            request_query_skip,
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


class V2MomOrgGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def v2_mom_org_get(
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
        return self._v2_mom_org_get_oapg(
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
        return self._v2_mom_org_get_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


