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
from pydantic import BaseModel, Field, StrictStr, conint, conlist

class EzsigndocumentApplyEzsigntemplateV1Request(BaseModel):
    """
    Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate  # noqa: E501
    """
    fki_ezsigntemplate_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplateID", description="The unique ID of the Ezsigntemplate")
    a_s_ezsigntemplatesigner: conlist(StrictStr, min_items=1) = Field(..., alias="a_sEzsigntemplatesigner")
    a_pki_ezsignfoldersignerassociation_id: conlist(conint(strict=True, ge=0), min_items=1) = Field(..., alias="a_pkiEzsignfoldersignerassociationID")
    __properties = ["fkiEzsigntemplateID", "a_sEzsigntemplatesigner", "a_pkiEzsignfoldersignerassociationID"]

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
    def from_json(cls, json_str: str) -> EzsigndocumentApplyEzsigntemplateV1Request:
        """Create an instance of EzsigndocumentApplyEzsigntemplateV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigndocumentApplyEzsigntemplateV1Request:
        """Create an instance of EzsigndocumentApplyEzsigntemplateV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigndocumentApplyEzsigntemplateV1Request.parse_obj(obj)

        _obj = EzsigndocumentApplyEzsigntemplateV1Request.parse_obj({
            "fki_ezsigntemplate_id": obj.get("fkiEzsigntemplateID"),
            "a_s_ezsigntemplatesigner": obj.get("a_sEzsigntemplatesigner"),
            "a_pki_ezsignfoldersignerassociation_id": obj.get("a_pkiEzsignfoldersignerassociationID")
        })
        return _obj


