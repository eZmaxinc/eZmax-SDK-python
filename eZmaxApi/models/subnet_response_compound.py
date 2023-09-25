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
from pydantic import BaseModel, Field, conint
from eZmaxApi.models.multilingual_subnet_description import MultilingualSubnetDescription

class SubnetResponseCompound(BaseModel):
    """
    A Subnet Object  # noqa: E501
    """
    pki_subnet_id: conint(strict=True, le=65535, ge=0) = Field(..., alias="pkiSubnetID", description="The unique ID of the Subnet")
    fki_user_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiUserID", description="The unique ID of the User")
    fki_apikey_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiApikeyID", description="The unique ID of the Apikey")
    obj_subnet_description: MultilingualSubnetDescription = Field(..., alias="objSubnetDescription")
    i_subnet_network: conint(strict=True, le=4294967295, ge=0) = Field(..., alias="iSubnetNetwork", description="The network of the Subnet in integer form. For example 8.8.8.0 would be 134744064")
    i_subnet_mask: conint(strict=True, le=4294967295, ge=0) = Field(..., alias="iSubnetMask", description="The mask of the Subnet  in integer form. For example 255.255.255.0 would be 4294967040")
    __properties = ["pkiSubnetID", "fkiUserID", "fkiApikeyID", "objSubnetDescription", "iSubnetNetwork", "iSubnetMask"]

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
    def from_json(cls, json_str: str) -> SubnetResponseCompound:
        """Create an instance of SubnetResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_subnet_description
        if self.obj_subnet_description:
            _dict['objSubnetDescription'] = self.obj_subnet_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubnetResponseCompound:
        """Create an instance of SubnetResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubnetResponseCompound.parse_obj(obj)

        _obj = SubnetResponseCompound.parse_obj({
            "pki_subnet_id": obj.get("pkiSubnetID"),
            "fki_user_id": obj.get("fkiUserID"),
            "fki_apikey_id": obj.get("fkiApikeyID"),
            "obj_subnet_description": MultilingualSubnetDescription.from_dict(obj.get("objSubnetDescription")) if obj.get("objSubnetDescription") is not None else None,
            "i_subnet_network": obj.get("iSubnetNetwork"),
            "i_subnet_mask": obj.get("iSubnetMask")
        })
        return _obj


