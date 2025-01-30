# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.scim_authentication_scheme import ScimAuthenticationScheme
from eZmaxApi.models.scim_service_provider_config_bulk import ScimServiceProviderConfigBulk
from eZmaxApi.models.scim_service_provider_config_change_password import ScimServiceProviderConfigChangePassword
from eZmaxApi.models.scim_service_provider_config_etag import ScimServiceProviderConfigEtag
from eZmaxApi.models.scim_service_provider_config_filter import ScimServiceProviderConfigFilter
from eZmaxApi.models.scim_service_provider_config_patch import ScimServiceProviderConfigPatch
from eZmaxApi.models.scim_service_provider_config_sort import ScimServiceProviderConfigSort
from typing import Optional, Set
from typing_extensions import Self

class ScimServiceProviderConfig(BaseModel):
    """
    ScimServiceProviderConfig
    """ # noqa: E501
    authentication_schemes: List[ScimAuthenticationScheme] = Field(description="A multi-valued complex type that specifies supported authentication scheme properties.", alias="authenticationSchemes")
    bulk: ScimServiceProviderConfigBulk
    change_password: ScimServiceProviderConfigChangePassword = Field(alias="changePassword")
    documentation_uri: StrictStr = Field(description="An HTTP-addressable URL pointing to the service provider's human-consumable help documentation", alias="documentationUri")
    etag: ScimServiceProviderConfigEtag
    filter: ScimServiceProviderConfigFilter
    patch: ScimServiceProviderConfigPatch
    sort: ScimServiceProviderConfigSort
    __properties: ClassVar[List[str]] = ["authenticationSchemes", "bulk", "changePassword", "documentationUri", "etag", "filter", "patch", "sort"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScimServiceProviderConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in authentication_schemes (list)
        _items = []
        if self.authentication_schemes:
            for _item_authentication_schemes in self.authentication_schemes:
                if _item_authentication_schemes:
                    _items.append(_item_authentication_schemes.to_dict())
            _dict['authenticationSchemes'] = _items
        # override the default output from pydantic by calling `to_dict()` of bulk
        if self.bulk:
            _dict['bulk'] = self.bulk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_password
        if self.change_password:
            _dict['changePassword'] = self.change_password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of etag
        if self.etag:
            _dict['etag'] = self.etag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of patch
        if self.patch:
            _dict['patch'] = self.patch.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScimServiceProviderConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authenticationSchemes": [ScimAuthenticationScheme.from_dict(_item) for _item in obj["authenticationSchemes"]] if obj.get("authenticationSchemes") is not None else None,
            "bulk": ScimServiceProviderConfigBulk.from_dict(obj["bulk"]) if obj.get("bulk") is not None else None,
            "changePassword": ScimServiceProviderConfigChangePassword.from_dict(obj["changePassword"]) if obj.get("changePassword") is not None else None,
            "documentationUri": obj.get("documentationUri"),
            "etag": ScimServiceProviderConfigEtag.from_dict(obj["etag"]) if obj.get("etag") is not None else None,
            "filter": ScimServiceProviderConfigFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "patch": ScimServiceProviderConfigPatch.from_dict(obj["patch"]) if obj.get("patch") is not None else None,
            "sort": ScimServiceProviderConfigSort.from_dict(obj["sort"]) if obj.get("sort") is not None else None
        })
        return _obj


