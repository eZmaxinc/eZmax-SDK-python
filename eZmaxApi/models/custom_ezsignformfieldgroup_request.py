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


from typing import List, Optional
from pydantic import BaseModel, Field, conint, conlist, constr
from eZmaxApi.models.custom_ezsignformfield_request import CustomEzsignformfieldRequest

class CustomEzsignformfieldgroupRequest(BaseModel):
    """
    A Custom Ezsignformfieldgroup Object to fill an Ezsignform using submitForm  # noqa: E501
    """
    pki_ezsignformfieldgroup_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignformfieldgroupID", description="The unique ID of the Ezsignformfieldgroup")
    s_ezsignformfieldgroup_label: Optional[constr(strict=True, max_length=50, min_length=1)] = Field(None, alias="sEzsignformfieldgroupLabel", description="The Label for the Ezsignformfieldgroup")
    a_obj_ezsignformfield: conlist(CustomEzsignformfieldRequest, min_items=1) = Field(..., alias="a_objEzsignformfield", description="An array containing all the values to fill the Ezsignform.")
    __properties = ["pkiEzsignformfieldgroupID", "sEzsignformfieldgroupLabel", "a_objEzsignformfield"]

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
    def from_json(cls, json_str: str) -> CustomEzsignformfieldgroupRequest:
        """Create an instance of CustomEzsignformfieldgroupRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignformfield (list)
        _items = []
        if self.a_obj_ezsignformfield:
            for _item in self.a_obj_ezsignformfield:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignformfield'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomEzsignformfieldgroupRequest:
        """Create an instance of CustomEzsignformfieldgroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomEzsignformfieldgroupRequest.parse_obj(obj)

        _obj = CustomEzsignformfieldgroupRequest.parse_obj({
            "pki_ezsignformfieldgroup_id": obj.get("pkiEzsignformfieldgroupID"),
            "s_ezsignformfieldgroup_label": obj.get("sEzsignformfieldgroupLabel"),
            "a_obj_ezsignformfield": [CustomEzsignformfieldRequest.from_dict(_item) for _item in obj.get("a_objEzsignformfield")] if obj.get("a_objEzsignformfield") is not None else None
        })
        return _obj

