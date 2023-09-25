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


from typing import List
from pydantic import BaseModel, Field, conlist
from eZmaxApi.models.ezsignsignergroupmembership_response_compound import EzsignsignergroupmembershipResponseCompound

class EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload(BaseModel):
    """
    Response for GET /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/getEzsignsignergroupmemberships  # noqa: E501
    """
    a_obj_ezsignsignergroupmembership: conlist(EzsignsignergroupmembershipResponseCompound) = Field(..., alias="a_objEzsignsignergroupmembership")
    __properties = ["a_objEzsignsignergroupmembership"]

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
    def from_json(cls, json_str: str) -> EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload:
        """Create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignsignergroupmembership (list)
        _items = []
        if self.a_obj_ezsignsignergroupmembership:
            for _item in self.a_obj_ezsignsignergroupmembership:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignsignergroupmembership'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload:
        """Create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload.parse_obj(obj)

        _obj = EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload.parse_obj({
            "a_obj_ezsignsignergroupmembership": [EzsignsignergroupmembershipResponseCompound.from_dict(_item) for _item in obj.get("a_objEzsignsignergroupmembership")] if obj.get("a_objEzsignsignergroupmembership") is not None else None
        })
        return _obj


