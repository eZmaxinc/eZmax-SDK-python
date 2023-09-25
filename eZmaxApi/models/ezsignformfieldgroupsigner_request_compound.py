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

class EzsignformfieldgroupsignerRequestCompound(BaseModel):
    """
    An Ezsignformfieldgroupsigner Object and children to create a complete structure  # noqa: E501
    """
    pki_ezsignformfieldgroupsigner_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignformfieldgroupsignerID", description="The unique ID of the Ezsignformfieldgroupsigner")
    fki_ezsignfoldersignerassociation_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfoldersignerassociationID", description="The unique ID of the Ezsignfoldersignerassociation")
    __properties = ["pkiEzsignformfieldgroupsignerID", "fkiEzsignfoldersignerassociationID"]

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
    def from_json(cls, json_str: str) -> EzsignformfieldgroupsignerRequestCompound:
        """Create an instance of EzsignformfieldgroupsignerRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignformfieldgroupsignerRequestCompound:
        """Create an instance of EzsignformfieldgroupsignerRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignformfieldgroupsignerRequestCompound.parse_obj(obj)

        _obj = EzsignformfieldgroupsignerRequestCompound.parse_obj({
            "pki_ezsignformfieldgroupsigner_id": obj.get("pkiEzsignformfieldgroupsignerID"),
            "fki_ezsignfoldersignerassociation_id": obj.get("fkiEzsignfoldersignerassociationID")
        })
        return _obj


