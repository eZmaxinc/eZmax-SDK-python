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
from pydantic import BaseModel, Field, conint, conlist
from eZmaxApi.models.ezsigntemplate_response_compound import EzsigntemplateResponseCompound
from eZmaxApi.models.ezsigntemplatepackagesignermembership_response_compound import EzsigntemplatepackagesignermembershipResponseCompound

class EzsigntemplatepackagemembershipResponseCompound(BaseModel):
    """
    A Ezsigntemplatepackagemembership Object  # noqa: E501
    """
    pki_ezsigntemplatepackagemembership_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsigntemplatepackagemembershipID", description="The unique ID of the Ezsigntemplatepackagemembership")
    fki_ezsigntemplatepackage_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplatepackageID", description="The unique ID of the Ezsigntemplatepackage")
    fki_ezsigntemplate_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplateID", description="The unique ID of the Ezsigntemplate")
    i_ezsigntemplatepackagemembership_order: conint(strict=True, ge=1) = Field(..., alias="iEzsigntemplatepackagemembershipOrder", description="The order in which the Ezsigntemplate will be imported when using an Ezsigntemplatepackage.")
    obj_ezsigntemplate: EzsigntemplateResponseCompound = Field(..., alias="objEzsigntemplate")
    a_obj_ezsigntemplatepackagesignermembership: conlist(EzsigntemplatepackagesignermembershipResponseCompound) = Field(..., alias="a_objEzsigntemplatepackagesignermembership")
    __properties = ["pkiEzsigntemplatepackagemembershipID", "fkiEzsigntemplatepackageID", "fkiEzsigntemplateID", "iEzsigntemplatepackagemembershipOrder", "objEzsigntemplate", "a_objEzsigntemplatepackagesignermembership"]

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
    def from_json(cls, json_str: str) -> EzsigntemplatepackagemembershipResponseCompound:
        """Create an instance of EzsigntemplatepackagemembershipResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplate
        if self.obj_ezsigntemplate:
            _dict['objEzsigntemplate'] = self.obj_ezsigntemplate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatepackagesignermembership (list)
        _items = []
        if self.a_obj_ezsigntemplatepackagesignermembership:
            for _item in self.a_obj_ezsigntemplatepackagesignermembership:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplatepackagesignermembership'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatepackagemembershipResponseCompound:
        """Create an instance of EzsigntemplatepackagemembershipResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatepackagemembershipResponseCompound.parse_obj(obj)

        _obj = EzsigntemplatepackagemembershipResponseCompound.parse_obj({
            "pki_ezsigntemplatepackagemembership_id": obj.get("pkiEzsigntemplatepackagemembershipID"),
            "fki_ezsigntemplatepackage_id": obj.get("fkiEzsigntemplatepackageID"),
            "fki_ezsigntemplate_id": obj.get("fkiEzsigntemplateID"),
            "i_ezsigntemplatepackagemembership_order": obj.get("iEzsigntemplatepackagemembershipOrder"),
            "obj_ezsigntemplate": EzsigntemplateResponseCompound.from_dict(obj.get("objEzsigntemplate")) if obj.get("objEzsigntemplate") is not None else None,
            "a_obj_ezsigntemplatepackagesignermembership": [EzsigntemplatepackagesignermembershipResponseCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplatepackagesignermembership")] if obj.get("a_objEzsigntemplatepackagesignermembership") is not None else None
        })
        return _obj


