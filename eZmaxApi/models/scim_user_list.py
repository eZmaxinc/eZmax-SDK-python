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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from eZmaxApi.models.scim_user import ScimUser

class ScimUserList(BaseModel):
    """
    ScimUserList
    """
    total_results: Optional[StrictInt] = Field(None, alias="totalResults")
    items_per_page: Optional[StrictInt] = Field(None, alias="itemsPerPage")
    start_index: Optional[StrictInt] = Field(None, alias="startIndex")
    schemas: Optional[conlist(StrictStr)] = None
    resources: Optional[conlist(ScimUser)] = Field(None, alias="Resources")
    __properties = ["totalResults", "itemsPerPage", "startIndex", "schemas", "Resources"]

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
    def from_json(cls, json_str: str) -> ScimUserList:
        """Create an instance of ScimUserList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScimUserList:
        """Create an instance of ScimUserList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScimUserList.parse_obj(obj)

        _obj = ScimUserList.parse_obj({
            "total_results": obj.get("totalResults"),
            "items_per_page": obj.get("itemsPerPage"),
            "start_index": obj.get("startIndex"),
            "schemas": obj.get("schemas"),
            "resources": [ScimUser.from_dict(_item) for _item in obj.get("Resources")] if obj.get("Resources") is not None else None
        })
        return _obj

