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
from pydantic import BaseModel, Field, StrictStr, conint, constr, validator
from eZmaxApi.models.field_e_phone_type import FieldEPhoneType

class PhoneRequestCompound(BaseModel):
    """
    A Phone Object and children to create a complete structure  # noqa: E501
    """
    pki_phone_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiPhoneID", description="The unique ID of the Phone.")
    fki_phonetype_id: conint(strict=True, ge=0) = Field(..., alias="fkiPhonetypeID", description="The unique ID of the Phonetype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Mobile| |4|Fax| |5|Pager| |6|Toll Free|")
    e_phone_type: Optional[FieldEPhoneType] = Field(None, alias="ePhoneType")
    s_phone_region: Optional[StrictStr] = Field(None, alias="sPhoneRegion", description="The region of the phone number. (For a North America Number only)  The region is the \"514\" section in this sample phone number: (514) 990-1516 x123")
    s_phone_exchange: Optional[StrictStr] = Field(None, alias="sPhoneExchange", description="The exchange of the phone number. (For a North America Number only)  The exchange is the \"990\" section in this sample phone number: (514) 990-1516 x123")
    s_phone_number: Optional[StrictStr] = Field(None, alias="sPhoneNumber", description="The number of the phone number. (For a North America Number only)  The number is the \"1516\" section in this sample phone number: (514) 990-1516 x123")
    s_phone_international: Optional[StrictStr] = Field(None, alias="sPhoneInternational", description="The international phone number.")
    s_phone_extension: Optional[StrictStr] = Field(None, alias="sPhoneExtension", description="The extension of the phone number.  The extension is the \"123\" section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers")
    s_phone_e164: Optional[constr(strict=True)] = Field(None, alias="sPhoneE164", description="A phone number in E.164 Format")
    __properties = ["pkiPhoneID", "fkiPhonetypeID", "ePhoneType", "sPhoneRegion", "sPhoneExchange", "sPhoneNumber", "sPhoneInternational", "sPhoneExtension", "sPhoneE164"]

    @validator('s_phone_e164')
    def s_phone_e164_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
        return value

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
    def from_json(cls, json_str: str) -> PhoneRequestCompound:
        """Create an instance of PhoneRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PhoneRequestCompound:
        """Create an instance of PhoneRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PhoneRequestCompound.parse_obj(obj)

        _obj = PhoneRequestCompound.parse_obj({
            "pki_phone_id": obj.get("pkiPhoneID"),
            "fki_phonetype_id": obj.get("fkiPhonetypeID"),
            "e_phone_type": obj.get("ePhoneType"),
            "s_phone_region": obj.get("sPhoneRegion"),
            "s_phone_exchange": obj.get("sPhoneExchange"),
            "s_phone_number": obj.get("sPhoneNumber"),
            "s_phone_international": obj.get("sPhoneInternational"),
            "s_phone_extension": obj.get("sPhoneExtension"),
            "s_phone_e164": obj.get("sPhoneE164")
        })
        return _obj


