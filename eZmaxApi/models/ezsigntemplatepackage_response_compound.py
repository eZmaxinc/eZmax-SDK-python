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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist
from eZmaxApi.models.ezsigntemplatepackagemembership_response_compound import EzsigntemplatepackagemembershipResponseCompound
from eZmaxApi.models.ezsigntemplatepackagesigner_response_compound import EzsigntemplatepackagesignerResponseCompound

class EzsigntemplatepackageResponseCompound(BaseModel):
    """
    A Ezsigntemplatepackage Object  # noqa: E501
    """
    pki_ezsigntemplatepackage_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsigntemplatepackageID", description="The unique ID of the Ezsigntemplatepackage")
    fki_ezsignfoldertype_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfoldertypeID", description="The unique ID of the Ezsignfoldertype.")
    fki_language_id: conint(strict=True, le=2, ge=1) = Field(..., alias="fkiLanguageID", description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|")
    s_language_name_x: StrictStr = Field(..., alias="sLanguageNameX", description="The Name of the Language in the language of the requester")
    s_ezsigntemplatepackage_description: StrictStr = Field(..., alias="sEzsigntemplatepackageDescription", description="The description of the Ezsigntemplatepackage")
    b_ezsigntemplatepackage_adminonly: StrictBool = Field(..., alias="bEzsigntemplatepackageAdminonly", description="Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType=Normal)")
    b_ezsigntemplatepackage_needvalidation: StrictBool = Field(..., alias="bEzsigntemplatepackageNeedvalidation", description="Whether the Ezsignbulksend was automatically modified and needs a manual validation")
    b_ezsigntemplatepackage_isactive: StrictBool = Field(..., alias="bEzsigntemplatepackageIsactive", description="Whether the Ezsigntemplatepackage is active or not")
    s_ezsignfoldertype_name_x: StrictStr = Field(..., alias="sEzsignfoldertypeNameX", description="The name of the Ezsignfoldertype in the language of the requester")
    a_obj_ezsigntemplatepackagesigner: conlist(EzsigntemplatepackagesignerResponseCompound) = Field(..., alias="a_objEzsigntemplatepackagesigner")
    a_obj_ezsigntemplatepackagemembership: conlist(EzsigntemplatepackagemembershipResponseCompound) = Field(..., alias="a_objEzsigntemplatepackagemembership")
    __properties = ["pkiEzsigntemplatepackageID", "fkiEzsignfoldertypeID", "fkiLanguageID", "sLanguageNameX", "sEzsigntemplatepackageDescription", "bEzsigntemplatepackageAdminonly", "bEzsigntemplatepackageNeedvalidation", "bEzsigntemplatepackageIsactive", "sEzsignfoldertypeNameX", "a_objEzsigntemplatepackagesigner", "a_objEzsigntemplatepackagemembership"]

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
    def from_json(cls, json_str: str) -> EzsigntemplatepackageResponseCompound:
        """Create an instance of EzsigntemplatepackageResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatepackagesigner (list)
        _items = []
        if self.a_obj_ezsigntemplatepackagesigner:
            for _item in self.a_obj_ezsigntemplatepackagesigner:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplatepackagesigner'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatepackagemembership (list)
        _items = []
        if self.a_obj_ezsigntemplatepackagemembership:
            for _item in self.a_obj_ezsigntemplatepackagemembership:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplatepackagemembership'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatepackageResponseCompound:
        """Create an instance of EzsigntemplatepackageResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatepackageResponseCompound.parse_obj(obj)

        _obj = EzsigntemplatepackageResponseCompound.parse_obj({
            "pki_ezsigntemplatepackage_id": obj.get("pkiEzsigntemplatepackageID"),
            "fki_ezsignfoldertype_id": obj.get("fkiEzsignfoldertypeID"),
            "fki_language_id": obj.get("fkiLanguageID"),
            "s_language_name_x": obj.get("sLanguageNameX"),
            "s_ezsigntemplatepackage_description": obj.get("sEzsigntemplatepackageDescription"),
            "b_ezsigntemplatepackage_adminonly": obj.get("bEzsigntemplatepackageAdminonly"),
            "b_ezsigntemplatepackage_needvalidation": obj.get("bEzsigntemplatepackageNeedvalidation"),
            "b_ezsigntemplatepackage_isactive": obj.get("bEzsigntemplatepackageIsactive"),
            "s_ezsignfoldertype_name_x": obj.get("sEzsignfoldertypeNameX"),
            "a_obj_ezsigntemplatepackagesigner": [EzsigntemplatepackagesignerResponseCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplatepackagesigner")] if obj.get("a_objEzsigntemplatepackagesigner") is not None else None,
            "a_obj_ezsigntemplatepackagemembership": [EzsigntemplatepackagemembershipResponseCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplatepackagemembership")] if obj.get("a_objEzsigntemplatepackagemembership") is not None else None
        })
        return _obj

