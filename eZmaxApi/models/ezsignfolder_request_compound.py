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
from eZmaxApi.models.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency

class EzsignfolderRequestCompound(BaseModel):
    """
    An Ezsignfolder Object and children to create a complete structure  # noqa: E501
    """
    pki_ezsignfolder_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignfolderID", description="The unique ID of the Ezsignfolder")
    fki_ezsignfoldertype_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfoldertypeID", description="The unique ID of the Ezsignfoldertype.")
    fki_ezsigntsarequirement_id: Optional[conint(strict=True, le=3, ge=1)] = Field(None, alias="fkiEzsigntsarequirementID", description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|")
    s_ezsignfolder_description: StrictStr = Field(..., alias="sEzsignfolderDescription", description="The description of the Ezsignfolder")
    t_ezsignfolder_note: Optional[StrictStr] = Field(None, alias="tEzsignfolderNote", description="Note about the Ezsignfolder")
    e_ezsignfolder_sendreminderfrequency: FieldEEzsignfolderSendreminderfrequency = Field(..., alias="eEzsignfolderSendreminderfrequency")
    s_ezsignfolder_externalid: Optional[constr(strict=True)] = Field(None, alias="sEzsignfolderExternalid", description="This field can be used to store an External ID from the client's system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format. ")
    __properties = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "fkiEzsigntsarequirementID", "sEzsignfolderDescription", "tEzsignfolderNote", "eEzsignfolderSendreminderfrequency", "sEzsignfolderExternalid"]

    @validator('s_ezsignfolder_externalid')
    def s_ezsignfolder_externalid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,64}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,64}$/")
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
    def from_json(cls, json_str: str) -> EzsignfolderRequestCompound:
        """Create an instance of EzsignfolderRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfolderRequestCompound:
        """Create an instance of EzsignfolderRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfolderRequestCompound.parse_obj(obj)

        _obj = EzsignfolderRequestCompound.parse_obj({
            "pki_ezsignfolder_id": obj.get("pkiEzsignfolderID"),
            "fki_ezsignfoldertype_id": obj.get("fkiEzsignfoldertypeID"),
            "fki_ezsigntsarequirement_id": obj.get("fkiEzsigntsarequirementID"),
            "s_ezsignfolder_description": obj.get("sEzsignfolderDescription"),
            "t_ezsignfolder_note": obj.get("tEzsignfolderNote"),
            "e_ezsignfolder_sendreminderfrequency": obj.get("eEzsignfolderSendreminderfrequency"),
            "s_ezsignfolder_externalid": obj.get("sEzsignfolderExternalid")
        })
        return _obj


