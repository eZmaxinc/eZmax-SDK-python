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
from eZmaxApi.models.ezsignsignature_request_compound import EzsignsignatureRequestCompound

class EzsigndocumentEditEzsignsignaturesV1Request(BaseModel):
    """
    Request for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignsignatures  # noqa: E501
    """
    a_obj_ezsignsignature: conlist(EzsignsignatureRequestCompound) = Field(..., alias="a_objEzsignsignature")
    __properties = ["a_objEzsignsignature"]

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
    def from_json(cls, json_str: str) -> EzsigndocumentEditEzsignsignaturesV1Request:
        """Create an instance of EzsigndocumentEditEzsignsignaturesV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignsignature (list)
        _items = []
        if self.a_obj_ezsignsignature:
            for _item in self.a_obj_ezsignsignature:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignsignature'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigndocumentEditEzsignsignaturesV1Request:
        """Create an instance of EzsigndocumentEditEzsignsignaturesV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigndocumentEditEzsignsignaturesV1Request.parse_obj(obj)

        _obj = EzsigndocumentEditEzsignsignaturesV1Request.parse_obj({
            "a_obj_ezsignsignature": [EzsignsignatureRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsignsignature")] if obj.get("a_objEzsignsignature") is not None else None
        })
        return _obj

