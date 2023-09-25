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
from pydantic import BaseModel, Field, StrictStr, conint, conlist
from eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response import CustomFormDataEzsignformfieldgroupResponse

class CustomFormDataSignerResponse(BaseModel):
    """
    A form Data Signer Object  # noqa: E501
    """
    fki_ezsignfoldersignerassociation_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfoldersignerassociationID", description="The unique ID of the Ezsignfoldersignerassociation")
    fki_user_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiUserID", description="The unique ID of the User")
    s_contact_firstname: StrictStr = Field(..., alias="sContactFirstname", description="The First name of the contact")
    s_contact_lastname: StrictStr = Field(..., alias="sContactLastname", description="The Last name of the contact")
    a_obj_ezsignformfieldgroup: conlist(CustomFormDataEzsignformfieldgroupResponse) = Field(..., alias="a_objEzsignformfieldgroup")
    __properties = ["fkiEzsignfoldersignerassociationID", "fkiUserID", "sContactFirstname", "sContactLastname", "a_objEzsignformfieldgroup"]

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
    def from_json(cls, json_str: str) -> CustomFormDataSignerResponse:
        """Create an instance of CustomFormDataSignerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignformfieldgroup (list)
        _items = []
        if self.a_obj_ezsignformfieldgroup:
            for _item in self.a_obj_ezsignformfieldgroup:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignformfieldgroup'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomFormDataSignerResponse:
        """Create an instance of CustomFormDataSignerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomFormDataSignerResponse.parse_obj(obj)

        _obj = CustomFormDataSignerResponse.parse_obj({
            "fki_ezsignfoldersignerassociation_id": obj.get("fkiEzsignfoldersignerassociationID"),
            "fki_user_id": obj.get("fkiUserID"),
            "s_contact_firstname": obj.get("sContactFirstname"),
            "s_contact_lastname": obj.get("sContactLastname"),
            "a_obj_ezsignformfieldgroup": [CustomFormDataEzsignformfieldgroupResponse.from_dict(_item) for _item in obj.get("a_objEzsignformfieldgroup")] if obj.get("a_objEzsignformfieldgroup") is not None else None
        })
        return _obj


