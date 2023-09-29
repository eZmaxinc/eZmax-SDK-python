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
from eZmaxApi.models.ezsigndocument_request import EzsigndocumentRequest
from eZmaxApi.models.ezsigndocument_request_compound import EzsigndocumentRequestCompound

class EzsigndocumentCreateObjectV1Request(BaseModel):
    """
    Request for POST /1/object/ezsigndocument  # noqa: E501
    """
    obj_ezsigndocument: Optional[EzsigndocumentRequest] = Field(None, alias="objEzsigndocument")
    obj_ezsigndocument_compound: Optional[EzsigndocumentRequestCompound] = Field(None, alias="objEzsigndocumentCompound")
    __properties = ["objEzsigndocument", "objEzsigndocumentCompound"]

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
    def from_json(cls, json_str: str) -> EzsigndocumentCreateObjectV1Request:
        """Create an instance of EzsigndocumentCreateObjectV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigndocument
        if self.obj_ezsigndocument:
            _dict['objEzsigndocument'] = self.obj_ezsigndocument.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigndocument_compound
        if self.obj_ezsigndocument_compound:
            _dict['objEzsigndocumentCompound'] = self.obj_ezsigndocument_compound.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigndocumentCreateObjectV1Request:
        """Create an instance of EzsigndocumentCreateObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigndocumentCreateObjectV1Request.parse_obj(obj)

        _obj = EzsigndocumentCreateObjectV1Request.parse_obj({
            "obj_ezsigndocument": EzsigndocumentRequest.from_dict(obj.get("objEzsigndocument")) if obj.get("objEzsigndocument") is not None else None,
            "obj_ezsigndocument_compound": EzsigndocumentRequestCompound.from_dict(obj.get("objEzsigndocumentCompound")) if obj.get("objEzsigndocumentCompound") is not None else None
        })
        return _obj

