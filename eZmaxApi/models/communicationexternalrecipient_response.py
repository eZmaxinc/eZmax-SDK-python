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
from pydantic import BaseModel, Field, StrictInt
from eZmaxApi.models.descriptionstatic_response_compound import DescriptionstaticResponseCompound
from eZmaxApi.models.emailstatic_response_compound import EmailstaticResponseCompound
from eZmaxApi.models.field_e_communicationexternalrecipient_type import FieldECommunicationexternalrecipientType
from eZmaxApi.models.phonestatic_response_compound import PhonestaticResponseCompound

class CommunicationexternalrecipientResponse(BaseModel):
    """
    A Communicationexternalrecipient Object  # noqa: E501
    """
    pki_communicationexternalrecipient_id: StrictInt = Field(..., alias="pkiCommunicationexternalrecipientID", description="The unique ID of the Communicationexternalrecipient")
    e_communicationexternalrecipient_type: FieldECommunicationexternalrecipientType = Field(..., alias="eCommunicationexternalrecipientType")
    obj_descriptionstatic: DescriptionstaticResponseCompound = Field(..., alias="objDescriptionstatic")
    obj_emailstatic: Optional[EmailstaticResponseCompound] = Field(None, alias="objEmailstatic")
    obj_phonestatic: Optional[PhonestaticResponseCompound] = Field(None, alias="objPhonestatic")
    __properties = ["pkiCommunicationexternalrecipientID", "eCommunicationexternalrecipientType", "objDescriptionstatic", "objEmailstatic", "objPhonestatic"]

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
    def from_json(cls, json_str: str) -> CommunicationexternalrecipientResponse:
        """Create an instance of CommunicationexternalrecipientResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_descriptionstatic
        if self.obj_descriptionstatic:
            _dict['objDescriptionstatic'] = self.obj_descriptionstatic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_emailstatic
        if self.obj_emailstatic:
            _dict['objEmailstatic'] = self.obj_emailstatic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phonestatic
        if self.obj_phonestatic:
            _dict['objPhonestatic'] = self.obj_phonestatic.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommunicationexternalrecipientResponse:
        """Create an instance of CommunicationexternalrecipientResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommunicationexternalrecipientResponse.parse_obj(obj)

        _obj = CommunicationexternalrecipientResponse.parse_obj({
            "pki_communicationexternalrecipient_id": obj.get("pkiCommunicationexternalrecipientID"),
            "e_communicationexternalrecipient_type": obj.get("eCommunicationexternalrecipientType"),
            "obj_descriptionstatic": DescriptionstaticResponseCompound.from_dict(obj.get("objDescriptionstatic")) if obj.get("objDescriptionstatic") is not None else None,
            "obj_emailstatic": EmailstaticResponseCompound.from_dict(obj.get("objEmailstatic")) if obj.get("objEmailstatic") is not None else None,
            "obj_phonestatic": PhonestaticResponseCompound.from_dict(obj.get("objPhonestatic")) if obj.get("objPhonestatic") is not None else None
        })
        return _obj


