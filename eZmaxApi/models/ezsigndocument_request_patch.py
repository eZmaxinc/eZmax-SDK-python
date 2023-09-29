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

class EzsigndocumentRequestPatch(BaseModel):
    """
    An Ezsigndocument Object  # noqa: E501
    """
    dt_ezsigndocument_duedate: Optional[StrictStr] = Field(None, alias="dtEzsigndocumentDuedate", description="The maximum date and time at which the Ezsigndocument can be signed.")
    s_ezsigndocument_name: Optional[StrictStr] = Field(None, alias="sEzsigndocumentName", description="The name of the document that will be presented to Ezsignfoldersignerassociations")
    __properties = ["dtEzsigndocumentDuedate", "sEzsigndocumentName"]

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
    def from_json(cls, json_str: str) -> EzsigndocumentRequestPatch:
        """Create an instance of EzsigndocumentRequestPatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigndocumentRequestPatch:
        """Create an instance of EzsigndocumentRequestPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigndocumentRequestPatch.parse_obj(obj)

        _obj = EzsigndocumentRequestPatch.parse_obj({
            "dt_ezsigndocument_duedate": obj.get("dtEzsigndocumentDuedate"),
            "s_ezsigndocument_name": obj.get("sEzsigndocumentName")
        })
        return _obj

