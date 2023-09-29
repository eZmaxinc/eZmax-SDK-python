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
from pydantic import BaseModel, Field, conint, conlist

class UsergroupdelegationCreateObjectV1ResponseMPayload(BaseModel):
    """
    Payload for POST /1/object/usergroupdelegation  # noqa: E501
    """
    a_pki_usergroupdelegation_id: conlist(conint(strict=True, le=65535, ge=0)) = Field(..., alias="a_pkiUsergroupdelegationID", description="An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request.")
    __properties = ["a_pkiUsergroupdelegationID"]

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
    def from_json(cls, json_str: str) -> UsergroupdelegationCreateObjectV1ResponseMPayload:
        """Create an instance of UsergroupdelegationCreateObjectV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsergroupdelegationCreateObjectV1ResponseMPayload:
        """Create an instance of UsergroupdelegationCreateObjectV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsergroupdelegationCreateObjectV1ResponseMPayload.parse_obj(obj)

        _obj = UsergroupdelegationCreateObjectV1ResponseMPayload.parse_obj({
            "a_pki_usergroupdelegation_id": obj.get("a_pkiUsergroupdelegationID")
        })
        return _obj

