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
from pydantic import BaseModel, Field, conlist
from eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response import CustomEzsignfolderEzsignsignaturesAutomaticResponse
from eZmaxApi.models.field_e_ezsignsignature_type import FieldEEzsignsignatureType

class EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getEzsignsignaturesAutomatic  # noqa: E501
    """
    a_e_ezsignsignature_type: conlist(FieldEEzsignsignatureType, unique_items=True) = Field(..., alias="a_eEzsignsignatureType", description="All eEzsignsignatureType contained in the response")
    a_obj_ezsignfolder: conlist(CustomEzsignfolderEzsignsignaturesAutomaticResponse) = Field(..., alias="a_objEzsignfolder")
    __properties = ["a_eEzsignsignatureType", "a_objEzsignfolder"]

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
    def from_json(cls, json_str: str) -> EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload:
        """Create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignfolder (list)
        _items = []
        if self.a_obj_ezsignfolder:
            for _item in self.a_obj_ezsignfolder:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignfolder'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload:
        """Create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload.parse_obj(obj)

        _obj = EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload.parse_obj({
            "a_e_ezsignsignature_type": obj.get("a_eEzsignsignatureType"),
            "a_obj_ezsignfolder": [CustomEzsignfolderEzsignsignaturesAutomaticResponse.from_dict(_item) for _item in obj.get("a_objEzsignfolder")] if obj.get("a_objEzsignfolder") is not None else None
        })
        return _obj


