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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from eZmaxApi.models.scim_group_member import ScimGroupMember

class ScimGroup(BaseModel):
    """
    ScimGroup
    """
    id: Optional[StrictStr] = None
    display_name: constr(strict=True) = Field(..., alias="displayName", description="The Name of the Usergroup in the language of the requester")
    members: Optional[conlist(ScimGroupMember)] = None
    __properties = ["id", "displayName", "members"]

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

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
    def from_json(cls, json_str: str) -> ScimGroup:
        """Create an instance of ScimGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScimGroup:
        """Create an instance of ScimGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScimGroup.parse_obj(obj)

        _obj = ScimGroup.parse_obj({
            "id": obj.get("id"),
            "display_name": obj.get("displayName"),
            "members": [ScimGroupMember.from_dict(_item) for _item in obj.get("members")] if obj.get("members") is not None else None
        })
        return _obj

