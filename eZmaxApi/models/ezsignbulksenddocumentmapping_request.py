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
from pydantic import BaseModel, Field, conint

class EzsignbulksenddocumentmappingRequest(BaseModel):
    """
    A Ezsignbulksenddocumentmapping Object  # noqa: E501
    """
    pki_ezsignbulksenddocumentmapping_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignbulksenddocumentmappingID", description="The unique ID of the Ezsignbulksenddocumentmapping.")
    fki_ezsignbulksend_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignbulksendID", description="The unique ID of the Ezsignbulksend")
    fki_ezsigntemplatepackage_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsigntemplatepackageID", description="The unique ID of the Ezsigntemplatepackage")
    fki_ezsigntemplate_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsigntemplateID", description="The unique ID of the Ezsigntemplate")
    __properties = ["pkiEzsignbulksenddocumentmappingID", "fkiEzsignbulksendID", "fkiEzsigntemplatepackageID", "fkiEzsigntemplateID"]

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
    def from_json(cls, json_str: str) -> EzsignbulksenddocumentmappingRequest:
        """Create an instance of EzsignbulksenddocumentmappingRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignbulksenddocumentmappingRequest:
        """Create an instance of EzsignbulksenddocumentmappingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignbulksenddocumentmappingRequest.parse_obj(obj)

        _obj = EzsignbulksenddocumentmappingRequest.parse_obj({
            "pki_ezsignbulksenddocumentmapping_id": obj.get("pkiEzsignbulksenddocumentmappingID"),
            "fki_ezsignbulksend_id": obj.get("fkiEzsignbulksendID"),
            "fki_ezsigntemplatepackage_id": obj.get("fkiEzsigntemplatepackageID"),
            "fki_ezsigntemplate_id": obj.get("fkiEzsigntemplateID")
        })
        return _obj


