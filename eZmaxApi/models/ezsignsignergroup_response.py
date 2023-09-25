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
from pydantic import BaseModel, Field, StrictStr, conint
from eZmaxApi.models.multilingual_ezsignsignergroup_description import MultilingualEzsignsignergroupDescription

class EzsignsignergroupResponse(BaseModel):
    """
    An Ezsignsignergroup Object  # noqa: E501
    """
    pki_ezsignsignergroup_id: conint(strict=True, le=65535, ge=0) = Field(..., alias="pkiEzsignsignergroupID", description="The unique ID of the Ezsignsignergroup")
    obj_ezsignsignergroup_description: MultilingualEzsignsignergroupDescription = Field(..., alias="objEzsignsignergroupDescription")
    s_ezsignsignergroup_description_x: Optional[StrictStr] = Field(None, alias="sEzsignsignergroupDescriptionX", description="The Description of the Ezsignsignergroup in the language of the requester")
    __properties = ["pkiEzsignsignergroupID", "objEzsignsignergroupDescription", "sEzsignsignergroupDescriptionX"]

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
    def from_json(cls, json_str: str) -> EzsignsignergroupResponse:
        """Create an instance of EzsignsignergroupResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignsignergroup_description
        if self.obj_ezsignsignergroup_description:
            _dict['objEzsignsignergroupDescription'] = self.obj_ezsignsignergroup_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignergroupResponse:
        """Create an instance of EzsignsignergroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignergroupResponse.parse_obj(obj)

        _obj = EzsignsignergroupResponse.parse_obj({
            "pki_ezsignsignergroup_id": obj.get("pkiEzsignsignergroupID"),
            "obj_ezsignsignergroup_description": MultilingualEzsignsignergroupDescription.from_dict(obj.get("objEzsignsignergroupDescription")) if obj.get("objEzsignsignergroupDescription") is not None else None,
            "s_ezsignsignergroup_description_x": obj.get("sEzsignsignergroupDescriptionX")
        })
        return _obj


