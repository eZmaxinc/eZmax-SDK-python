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
from pydantic import BaseModel, Field, StrictStr, conint

class EzsigntemplatepackagesignerRequest(BaseModel):
    """
    A Ezsigntemplatepackagesigner Object  # noqa: E501
    """
    pki_ezsigntemplatepackagesigner_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsigntemplatepackagesignerID", description="The unique ID of the Ezsigntemplatepackagesigner")
    fki_ezsigntemplatepackage_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplatepackageID", description="The unique ID of the Ezsigntemplatepackage")
    s_ezsigntemplatepackagesigner_description: StrictStr = Field(..., alias="sEzsigntemplatepackagesignerDescription", description="The description of the Ezsigntemplatepackagesigner")
    __properties = ["pkiEzsigntemplatepackagesignerID", "fkiEzsigntemplatepackageID", "sEzsigntemplatepackagesignerDescription"]

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
    def from_json(cls, json_str: str) -> EzsigntemplatepackagesignerRequest:
        """Create an instance of EzsigntemplatepackagesignerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatepackagesignerRequest:
        """Create an instance of EzsigntemplatepackagesignerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatepackagesignerRequest.parse_obj(obj)

        _obj = EzsigntemplatepackagesignerRequest.parse_obj({
            "pki_ezsigntemplatepackagesigner_id": obj.get("pkiEzsigntemplatepackagesignerID"),
            "fki_ezsigntemplatepackage_id": obj.get("fkiEzsigntemplatepackageID"),
            "s_ezsigntemplatepackagesigner_description": obj.get("sEzsigntemplatepackagesignerDescription")
        })
        return _obj

