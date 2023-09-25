# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_contact_name_response import CustomContactNameResponse
from eZmaxApi.models.multilingual_apikey_description import MultilingualApikeyDescription

class ApikeyResponse(BaseModel):
    """
    An Apikey Object  # noqa: E501
    """
    pki_apikey_id: conint(strict=True, ge=0) = Field(..., alias="pkiApikeyID", description="The unique ID of the Apikey")
    fki_user_id: conint(strict=True, ge=0) = Field(..., alias="fkiUserID", description="The unique ID of the User")
    obj_apikey_description: MultilingualApikeyDescription = Field(..., alias="objApikeyDescription")
    obj_contact_name: CustomContactNameResponse = Field(..., alias="objContactName")
    s_apikey_apikey: Optional[StrictStr] = Field(None, alias="sApikeyApikey", description="The Apikey for the API key.  This will be hidden if we are not creating or regenerating the Apikey.")
    s_apikey_secret: Optional[StrictStr] = Field(None, alias="sApikeySecret", description="The Secret for the API key.  This will be hidden if we are not creating or regenerating the Apikey.")
    b_apikey_isactive: StrictBool = Field(..., alias="bApikeyIsactive", description="Whether the apikey is active or not")
    b_apikey_issigned: Optional[StrictBool] = Field(None, alias="bApikeyIssigned", description="Whether the apikey is signed or not")
    obj_audit: CommonAudit = Field(..., alias="objAudit")
    __properties = ["pkiApikeyID", "fkiUserID", "objApikeyDescription", "objContactName", "sApikeyApikey", "sApikeySecret", "bApikeyIsactive", "bApikeyIssigned", "objAudit"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApikeyResponse:
        """Create an instance of ApikeyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_apikey_description
        if self.obj_apikey_description:
            _dict['objApikeyDescription'] = self.obj_apikey_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_contact_name
        if self.obj_contact_name:
            _dict['objContactName'] = self.obj_contact_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApikeyResponse:
        """Create an instance of ApikeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApikeyResponse.parse_obj(obj)

        _obj = ApikeyResponse.parse_obj({
            "pki_apikey_id": obj.get("pkiApikeyID"),
            "fki_user_id": obj.get("fkiUserID"),
            "obj_apikey_description": MultilingualApikeyDescription.from_dict(obj.get("objApikeyDescription")) if obj.get("objApikeyDescription") is not None else None,
            "obj_contact_name": CustomContactNameResponse.from_dict(obj.get("objContactName")) if obj.get("objContactName") is not None else None,
            "s_apikey_apikey": obj.get("sApikeyApikey"),
            "s_apikey_secret": obj.get("sApikeySecret"),
            "b_apikey_isactive": obj.get("bApikeyIsactive"),
            "b_apikey_issigned": obj.get("bApikeyIssigned"),
            "obj_audit": CommonAudit.from_dict(obj.get("objAudit")) if obj.get("objAudit") is not None else None
        })
        return _obj


