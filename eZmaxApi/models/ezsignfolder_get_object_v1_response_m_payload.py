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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, constr, validator
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_ezsignfoldertype_response import CustomEzsignfoldertypeResponse
from eZmaxApi.models.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
from eZmaxApi.models.field_e_ezsignfolder_step import FieldEEzsignfolderStep

class EzsignfolderGetObjectV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}  # noqa: E501
    """
    pki_ezsignfolder_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsignfolderID", description="The unique ID of the Ezsignfolder")
    fki_ezsignfoldertype_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsignfoldertypeID", description="The unique ID of the Ezsignfoldertype.")
    obj_ezsignfoldertype: Optional[CustomEzsignfoldertypeResponse] = Field(None, alias="objEzsignfoldertype")
    s_ezsignfoldertype_name_x: Optional[StrictStr] = Field(None, alias="sEzsignfoldertypeNameX")
    fki_billingentityinternal_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiBillingentityinternalID", description="The unique ID of the Billingentityinternal.")
    s_billingentityinternal_description_x: Optional[StrictStr] = Field(None, alias="sBillingentityinternalDescriptionX", description="The description of the Billingentityinternal in the language of the requester")
    fki_ezsigntsarequirement_id: Optional[conint(strict=True, le=3, ge=1)] = Field(None, alias="fkiEzsigntsarequirementID", description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|")
    s_ezsigntsarequirement_description_x: Optional[StrictStr] = Field(None, alias="sEzsigntsarequirementDescriptionX", description="The description of the Ezsigntsarequirement in the language of the requester")
    s_ezsignfolder_description: StrictStr = Field(..., alias="sEzsignfolderDescription", description="The description of the Ezsignfolder")
    t_ezsignfolder_note: Optional[StrictStr] = Field(None, alias="tEzsignfolderNote", description="Note about the Ezsignfolder")
    b_ezsignfolder_isdisposable: Optional[StrictBool] = Field(None, alias="bEzsignfolderIsdisposable", description="If the Ezsigndocument can be disposed")
    e_ezsignfolder_sendreminderfrequency: Optional[FieldEEzsignfolderSendreminderfrequency] = Field(None, alias="eEzsignfolderSendreminderfrequency")
    dt_ezsignfolder_delayedsenddate: Optional[StrictStr] = Field(None, alias="dtEzsignfolderDelayedsenddate", description="The date and time at which the Ezsignfolder will be sent in the future.")
    dt_ezsignfolder_duedate: Optional[StrictStr] = Field(None, alias="dtEzsignfolderDuedate", description="The maximum date and time at which the Ezsignfolder can be signed.")
    dt_ezsignfolder_sentdate: Optional[StrictStr] = Field(None, alias="dtEzsignfolderSentdate", description="The date and time at which the Ezsignfolder was sent the last time.")
    dt_ezsignfolder_scheduledarchive: Optional[StrictStr] = Field(None, alias="dtEzsignfolderScheduledarchive", description="The scheduled date and time at which the Ezsignfolder should be archived.")
    dt_ezsignfolder_scheduleddispose: Optional[StrictStr] = Field(None, alias="dtEzsignfolderScheduleddispose", description="The scheduled date at which the Ezsignfolder should be Disposed.")
    e_ezsignfolder_step: Optional[FieldEEzsignfolderStep] = Field(None, alias="eEzsignfolderStep")
    dt_ezsignfolder_close: Optional[StrictStr] = Field(None, alias="dtEzsignfolderClose", description="The date and time at which the Ezsignfolder was closed. Either by applying the last signature or by completing it prematurely.")
    t_ezsignfolder_message: Optional[StrictStr] = Field(None, alias="tEzsignfolderMessage", description="A custom text message that will be added to the email sent.")
    obj_audit: Optional[CommonAudit] = Field(None, alias="objAudit")
    s_ezsignfolder_externalid: Optional[constr(strict=True)] = Field(None, alias="sEzsignfolderExternalid", description="This field can be used to store an External ID from the client's system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format. ")
    __properties = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "objEzsignfoldertype", "sEzsignfoldertypeNameX", "fkiBillingentityinternalID", "sBillingentityinternalDescriptionX", "fkiEzsigntsarequirementID", "sEzsigntsarequirementDescriptionX", "sEzsignfolderDescription", "tEzsignfolderNote", "bEzsignfolderIsdisposable", "eEzsignfolderSendreminderfrequency", "dtEzsignfolderDelayedsenddate", "dtEzsignfolderDuedate", "dtEzsignfolderSentdate", "dtEzsignfolderScheduledarchive", "dtEzsignfolderScheduleddispose", "eEzsignfolderStep", "dtEzsignfolderClose", "tEzsignfolderMessage", "objAudit", "sEzsignfolderExternalid"]

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
    def from_json(cls, json_str: str) -> EzsignfolderGetObjectV1ResponseMPayload:
        """Create an instance of EzsignfolderGetObjectV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype
        if self.obj_ezsignfoldertype:
            _dict['objEzsignfoldertype'] = self.obj_ezsignfoldertype.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfolderGetObjectV1ResponseMPayload:
        """Create an instance of EzsignfolderGetObjectV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfolderGetObjectV1ResponseMPayload.parse_obj(obj)

        _obj = EzsignfolderGetObjectV1ResponseMPayload.parse_obj({
            "pki_ezsignfolder_id": obj.get("pkiEzsignfolderID"),
            "fki_ezsignfoldertype_id": obj.get("fkiEzsignfoldertypeID"),
            "obj_ezsignfoldertype": CustomEzsignfoldertypeResponse.from_dict(obj.get("objEzsignfoldertype")) if obj.get("objEzsignfoldertype") is not None else None,
            "s_ezsignfoldertype_name_x": obj.get("sEzsignfoldertypeNameX"),
            "fki_billingentityinternal_id": obj.get("fkiBillingentityinternalID"),
            "s_billingentityinternal_description_x": obj.get("sBillingentityinternalDescriptionX"),
            "fki_ezsigntsarequirement_id": obj.get("fkiEzsigntsarequirementID"),
            "s_ezsigntsarequirement_description_x": obj.get("sEzsigntsarequirementDescriptionX"),
            "s_ezsignfolder_description": obj.get("sEzsignfolderDescription"),
            "t_ezsignfolder_note": obj.get("tEzsignfolderNote"),
            "b_ezsignfolder_isdisposable": obj.get("bEzsignfolderIsdisposable"),
            "e_ezsignfolder_sendreminderfrequency": obj.get("eEzsignfolderSendreminderfrequency"),
            "dt_ezsignfolder_delayedsenddate": obj.get("dtEzsignfolderDelayedsenddate"),
            "dt_ezsignfolder_duedate": obj.get("dtEzsignfolderDuedate"),
            "dt_ezsignfolder_sentdate": obj.get("dtEzsignfolderSentdate"),
            "dt_ezsignfolder_scheduledarchive": obj.get("dtEzsignfolderScheduledarchive"),
            "dt_ezsignfolder_scheduleddispose": obj.get("dtEzsignfolderScheduleddispose"),
            "e_ezsignfolder_step": obj.get("eEzsignfolderStep"),
            "dt_ezsignfolder_close": obj.get("dtEzsignfolderClose"),
            "t_ezsignfolder_message": obj.get("tEzsignfolderMessage"),
            "obj_audit": CommonAudit.from_dict(obj.get("objAudit")) if obj.get("objAudit") is not None else None,
            "s_ezsignfolder_externalid": obj.get("sEzsignfolderExternalid")
        })
        return _obj


