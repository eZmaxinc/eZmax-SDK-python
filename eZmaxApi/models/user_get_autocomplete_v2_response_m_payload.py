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
from eZmaxApi.models.user_autocomplete_element_response import UserAutocompleteElementResponse

class UserGetAutocompleteV2ResponseMPayload(BaseModel):
    """
    Payload for POST /2/object/user/getAutocomplete  # noqa: E501
    """
    a_obj_user: conlist(UserAutocompleteElementResponse) = Field(..., alias="a_objUser", description="An array of User autocomplete element response.")
    __properties = ["a_objUser"]

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
    def from_json(cls, json_str: str) -> UserGetAutocompleteV2ResponseMPayload:
        """Create an instance of UserGetAutocompleteV2ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_user (list)
        _items = []
        if self.a_obj_user:
            for _item in self.a_obj_user:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objUser'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserGetAutocompleteV2ResponseMPayload:
        """Create an instance of UserGetAutocompleteV2ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserGetAutocompleteV2ResponseMPayload.parse_obj(obj)

        _obj = UserGetAutocompleteV2ResponseMPayload.parse_obj({
            "a_obj_user": [UserAutocompleteElementResponse.from_dict(_item) for _item in obj.get("a_objUser")] if obj.get("a_objUser") is not None else None
        })
        return _obj

