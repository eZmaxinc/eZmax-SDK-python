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
from pydantic import BaseModel, Field, StrictStr

class MultilingualEzsignfoldertypeName(BaseModel):
    """
    Name of the Ezsignfoldertype  # noqa: E501
    """
    s_ezsignfoldertype_name1: Optional[StrictStr] = Field(None, alias="sEzsignfoldertypeName1", description="The name of the Ezsignfoldertype in French")
    s_ezsignfoldertype_name2: Optional[StrictStr] = Field(None, alias="sEzsignfoldertypeName2", description="The name of the Ezsignfoldertype in English")
    __properties = ["sEzsignfoldertypeName1", "sEzsignfoldertypeName2"]

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
    def from_json(cls, json_str: str) -> MultilingualEzsignfoldertypeName:
        """Create an instance of MultilingualEzsignfoldertypeName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MultilingualEzsignfoldertypeName:
        """Create an instance of MultilingualEzsignfoldertypeName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MultilingualEzsignfoldertypeName.parse_obj(obj)

        _obj = MultilingualEzsignfoldertypeName.parse_obj({
            "s_ezsignfoldertype_name1": obj.get("sEzsignfoldertypeName1"),
            "s_ezsignfoldertype_name2": obj.get("sEzsignfoldertypeName2")
        })
        return _obj

