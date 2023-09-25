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
from eZmaxApi.models.custom_ezsignfoldersignerassociationmessage_request import CustomEzsignfoldersignerassociationmessageRequest

class EzsignfolderSendV2Request(BaseModel):
    """
    Request for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/send  # noqa: E501
    """
    t_ezsignfolder_message: StrictStr = Field(..., alias="tEzsignfolderMessage", description="A custom text message that will be added to the email sent.")
    a_fki_ezsignfoldersignerassociation_id: conlist(conint(strict=True, ge=0)) = Field(..., alias="a_fkiEzsignfoldersignerassociationID")
    a_obj_ezsignfoldersignerassociationmessage: conlist(CustomEzsignfoldersignerassociationmessageRequest) = Field(..., alias="a_objEzsignfoldersignerassociationmessage")
    __properties = ["tEzsignfolderMessage", "a_fkiEzsignfoldersignerassociationID", "a_objEzsignfoldersignerassociationmessage"]

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
    def from_json(cls, json_str: str) -> EzsignfolderSendV2Request:
        """Create an instance of EzsignfolderSendV2Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignfoldersignerassociationmessage (list)
        _items = []
        if self.a_obj_ezsignfoldersignerassociationmessage:
            for _item in self.a_obj_ezsignfoldersignerassociationmessage:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignfoldersignerassociationmessage'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfolderSendV2Request:
        """Create an instance of EzsignfolderSendV2Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfolderSendV2Request.parse_obj(obj)

        _obj = EzsignfolderSendV2Request.parse_obj({
            "t_ezsignfolder_message": obj.get("tEzsignfolderMessage"),
            "a_fki_ezsignfoldersignerassociation_id": obj.get("a_fkiEzsignfoldersignerassociationID"),
            "a_obj_ezsignfoldersignerassociationmessage": [CustomEzsignfoldersignerassociationmessageRequest.from_dict(_item) for _item in obj.get("a_objEzsignfoldersignerassociationmessage")] if obj.get("a_objEzsignfoldersignerassociationmessage") is not None else None
        })
        return _obj


