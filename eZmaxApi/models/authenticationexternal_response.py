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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.field_e_authenticationexternal_type import FieldEAuthenticationexternalType
from typing import Optional, Set
from typing_extensions import Self

class AuthenticationexternalResponse(BaseModel):
    """
    A Authenticationexternal Object
    """ # noqa: E501
    pki_authenticationexternal_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Authenticationexternal", alias="pkiAuthenticationexternalID")
    s_authenticationexternal_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Authenticationexternal", alias="sAuthenticationexternalDescription")
    e_authenticationexternal_type: FieldEAuthenticationexternalType = Field(alias="eAuthenticationexternalType")
    b_authenticationexternal_connected: Optional[StrictBool] = Field(default=None, description="Whether the Authenticationexternal has been connected or not", alias="bAuthenticationexternalConnected")
    s_authenticationexternal_authorizationurl: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The url to authorize the Authenticationexternal", alias="sAuthenticationexternalAuthorizationurl")
    obj_audit: CommonAudit = Field(alias="objAudit")
    __properties: ClassVar[List[str]] = ["pkiAuthenticationexternalID", "sAuthenticationexternalDescription", "eAuthenticationexternalType", "bAuthenticationexternalConnected", "sAuthenticationexternalAuthorizationurl", "objAudit"]

    @field_validator('s_authenticationexternal_description')
    def s_authenticationexternal_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_authenticationexternal_authorizationurl')
    def s_authenticationexternal_authorizationurl_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(https|http):\/\/[^\s\/$.?#].[^\s]*$", value):
            raise ValueError(r"must validate the regular expression /^(https|http):\/\/[^\s\/$.?#].[^\s]*$/")
        return value

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
        """Create an instance of AuthenticationexternalResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticationexternalResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiAuthenticationexternalID": obj.get("pkiAuthenticationexternalID"),
            "sAuthenticationexternalDescription": obj.get("sAuthenticationexternalDescription"),
            "eAuthenticationexternalType": obj.get("eAuthenticationexternalType"),
            "bAuthenticationexternalConnected": obj.get("bAuthenticationexternalConnected"),
            "sAuthenticationexternalAuthorizationurl": obj.get("sAuthenticationexternalAuthorizationurl"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None
        })
        return _obj


