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
from pydantic import BaseModel, Field, StrictStr, conint
from eZmaxApi.models.contactinformations_request_compound import ContactinformationsRequestCompound

class ContactRequestCompound(BaseModel):
    """
    A Contact Object and children to create a complete structure  # noqa: E501
    """
    fki_contacttitle_id: conint(strict=True, ge=0) = Field(..., alias="fkiContacttitleID", description="The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)|")
    fki_language_id: conint(strict=True, le=2, ge=1) = Field(..., alias="fkiLanguageID", description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|")
    s_contact_firstname: StrictStr = Field(..., alias="sContactFirstname", description="The First name of the contact")
    s_contact_lastname: StrictStr = Field(..., alias="sContactLastname", description="The Last name of the contact")
    s_contact_company: StrictStr = Field(..., alias="sContactCompany", description="The Company name of the contact")
    dt_contact_birthdate: Optional[StrictStr] = Field(None, alias="dtContactBirthdate", description="The Birth Date of the contact")
    obj_contactinformations: ContactinformationsRequestCompound = Field(..., alias="objContactinformations")
    __properties = ["fkiContacttitleID", "fkiLanguageID", "sContactFirstname", "sContactLastname", "sContactCompany", "dtContactBirthdate", "objContactinformations"]

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
    def from_json(cls, json_str: str) -> ContactRequestCompound:
        """Create an instance of ContactRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_contactinformations
        if self.obj_contactinformations:
            _dict['objContactinformations'] = self.obj_contactinformations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContactRequestCompound:
        """Create an instance of ContactRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContactRequestCompound.parse_obj(obj)

        _obj = ContactRequestCompound.parse_obj({
            "fki_contacttitle_id": obj.get("fkiContacttitleID"),
            "fki_language_id": obj.get("fkiLanguageID"),
            "s_contact_firstname": obj.get("sContactFirstname"),
            "s_contact_lastname": obj.get("sContactLastname"),
            "s_contact_company": obj.get("sContactCompany"),
            "dt_contact_birthdate": obj.get("dtContactBirthdate"),
            "obj_contactinformations": ContactinformationsRequestCompound.from_dict(obj.get("objContactinformations")) if obj.get("objContactinformations") is not None else None
        })
        return _obj

