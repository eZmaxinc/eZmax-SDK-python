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
from pydantic import BaseModel, Field
from eZmaxApi.models.franchisereferalincome_request import FranchisereferalincomeRequest
from eZmaxApi.models.franchisereferalincome_request_compound import FranchisereferalincomeRequestCompound

class FranchisereferalincomeCreateObjectV1Request(BaseModel):
    """
    Request for POST /1/object/franchisereferalincome  # noqa: E501
    """
    obj_franchisereferalincome: Optional[FranchisereferalincomeRequest] = Field(None, alias="objFranchisereferalincome")
    obj_franchisereferalincome_compound: Optional[FranchisereferalincomeRequestCompound] = Field(None, alias="objFranchisereferalincomeCompound")
    __properties = ["objFranchisereferalincome", "objFranchisereferalincomeCompound"]

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
    def from_json(cls, json_str: str) -> FranchisereferalincomeCreateObjectV1Request:
        """Create an instance of FranchisereferalincomeCreateObjectV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_franchisereferalincome
        if self.obj_franchisereferalincome:
            _dict['objFranchisereferalincome'] = self.obj_franchisereferalincome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_franchisereferalincome_compound
        if self.obj_franchisereferalincome_compound:
            _dict['objFranchisereferalincomeCompound'] = self.obj_franchisereferalincome_compound.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FranchisereferalincomeCreateObjectV1Request:
        """Create an instance of FranchisereferalincomeCreateObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FranchisereferalincomeCreateObjectV1Request.parse_obj(obj)

        _obj = FranchisereferalincomeCreateObjectV1Request.parse_obj({
            "obj_franchisereferalincome": FranchisereferalincomeRequest.from_dict(obj.get("objFranchisereferalincome")) if obj.get("objFranchisereferalincome") is not None else None,
            "obj_franchisereferalincome_compound": FranchisereferalincomeRequestCompound.from_dict(obj.get("objFranchisereferalincomeCompound")) if obj.get("objFranchisereferalincomeCompound") is not None else None
        })
        return _obj

