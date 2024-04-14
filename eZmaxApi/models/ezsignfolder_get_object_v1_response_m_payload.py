# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_ezsignfoldertype_response import CustomEzsignfoldertypeResponse
from eZmaxApi.models.field_e_ezsignfolder_completion import FieldEEzsignfolderCompletion
from eZmaxApi.models.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
from eZmaxApi.models.field_e_ezsignfolder_step import FieldEEzsignfolderStep
from typing import Optional, Set
from typing_extensions import Self

class EzsignfolderGetObjectV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}
    """ # noqa: E501
    pki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="pkiEzsignfolderID")
    fki_ezsignfoldertype_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    obj_ezsignfoldertype: Optional[CustomEzsignfoldertypeResponse] = Field(default=None, alias="objEzsignfoldertype")
    e_ezsignfolder_completion: FieldEEzsignfolderCompletion = Field(alias="eEzsignfolderCompletion")
    s_ezsignfoldertype_name_x: Optional[StrictStr] = Field(default=None, alias="sEzsignfoldertypeNameX")
    fki_billingentityinternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    s_billingentityinternal_description_x: Optional[StrictStr] = Field(default=None, description="The description of the Billingentityinternal in the language of the requester", alias="sBillingentityinternalDescriptionX")
    fki_ezsigntsarequirement_id: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|", alias="fkiEzsigntsarequirementID")
    s_ezsigntsarequirement_description_x: Optional[StrictStr] = Field(default=None, description="The description of the Ezsigntsarequirement in the language of the requester", alias="sEzsigntsarequirementDescriptionX")
    s_ezsignfolder_description: StrictStr = Field(description="The description of the Ezsignfolder", alias="sEzsignfolderDescription")
    t_ezsignfolder_note: Optional[StrictStr] = Field(default=None, description="Note about the Ezsignfolder", alias="tEzsignfolderNote")
    b_ezsignfolder_isdisposable: Optional[StrictBool] = Field(default=None, description="If the Ezsigndocument can be disposed", alias="bEzsignfolderIsdisposable")
    e_ezsignfolder_sendreminderfrequency: Optional[FieldEEzsignfolderSendreminderfrequency] = Field(default=None, alias="eEzsignfolderSendreminderfrequency")
    dt_ezsignfolder_delayedsenddate: Optional[StrictStr] = Field(default=None, description="The date and time at which the Ezsignfolder will be sent in the future.", alias="dtEzsignfolderDelayedsenddate")
    dt_ezsignfolder_duedate: Optional[StrictStr] = Field(default=None, description="The maximum date and time at which the Ezsignfolder can be signed.", alias="dtEzsignfolderDuedate")
    dt_ezsignfolder_sentdate: Optional[StrictStr] = Field(default=None, description="The date and time at which the Ezsignfolder was sent the last time.", alias="dtEzsignfolderSentdate")
    dt_ezsignfolder_scheduledarchive: Optional[StrictStr] = Field(default=None, description="The scheduled date and time at which the Ezsignfolder should be archived.", alias="dtEzsignfolderScheduledarchive")
    dt_ezsignfolder_scheduleddispose: Optional[StrictStr] = Field(default=None, description="The scheduled date at which the Ezsignfolder should be Disposed.", alias="dtEzsignfolderScheduleddispose")
    e_ezsignfolder_step: Optional[FieldEEzsignfolderStep] = Field(default=None, alias="eEzsignfolderStep")
    dt_ezsignfolder_close: Optional[StrictStr] = Field(default=None, description="The date and time at which the Ezsignfolder was closed. Either by applying the last signature or by completing it prematurely.", alias="dtEzsignfolderClose")
    t_ezsignfolder_message: Optional[StrictStr] = Field(default=None, description="A custom text message that will be added to the email sent.", alias="tEzsignfolderMessage")
    obj_audit: Optional[CommonAudit] = Field(default=None, alias="objAudit")
    s_ezsignfolder_externalid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This field can be used to store an External ID from the client's system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format. ", alias="sEzsignfolderExternalid")
    __properties: ClassVar[List[str]] = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "objEzsignfoldertype", "eEzsignfolderCompletion", "sEzsignfoldertypeNameX", "fkiBillingentityinternalID", "sBillingentityinternalDescriptionX", "fkiEzsigntsarequirementID", "sEzsigntsarequirementDescriptionX", "sEzsignfolderDescription", "tEzsignfolderNote", "bEzsignfolderIsdisposable", "eEzsignfolderSendreminderfrequency", "dtEzsignfolderDelayedsenddate", "dtEzsignfolderDuedate", "dtEzsignfolderSentdate", "dtEzsignfolderScheduledarchive", "dtEzsignfolderScheduleddispose", "eEzsignfolderStep", "dtEzsignfolderClose", "tEzsignfolderMessage", "objAudit", "sEzsignfolderExternalid"]

    @field_validator('s_ezsignfolder_externalid')
    def s_ezsignfolder_externalid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,128}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,128}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EzsignfolderGetObjectV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype
        if self.obj_ezsignfoldertype:
            _dict['objEzsignfoldertype'] = self.obj_ezsignfoldertype.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignfolderGetObjectV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfolderID": obj.get("pkiEzsignfolderID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "objEzsignfoldertype": CustomEzsignfoldertypeResponse.from_dict(obj["objEzsignfoldertype"]) if obj.get("objEzsignfoldertype") is not None else None,
            "eEzsignfolderCompletion": obj.get("eEzsignfolderCompletion"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "sBillingentityinternalDescriptionX": obj.get("sBillingentityinternalDescriptionX"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "sEzsigntsarequirementDescriptionX": obj.get("sEzsigntsarequirementDescriptionX"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "tEzsignfolderNote": obj.get("tEzsignfolderNote"),
            "bEzsignfolderIsdisposable": obj.get("bEzsignfolderIsdisposable"),
            "eEzsignfolderSendreminderfrequency": obj.get("eEzsignfolderSendreminderfrequency"),
            "dtEzsignfolderDelayedsenddate": obj.get("dtEzsignfolderDelayedsenddate"),
            "dtEzsignfolderDuedate": obj.get("dtEzsignfolderDuedate"),
            "dtEzsignfolderSentdate": obj.get("dtEzsignfolderSentdate"),
            "dtEzsignfolderScheduledarchive": obj.get("dtEzsignfolderScheduledarchive"),
            "dtEzsignfolderScheduleddispose": obj.get("dtEzsignfolderScheduleddispose"),
            "eEzsignfolderStep": obj.get("eEzsignfolderStep"),
            "dtEzsignfolderClose": obj.get("dtEzsignfolderClose"),
            "tEzsignfolderMessage": obj.get("tEzsignfolderMessage"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "sEzsignfolderExternalid": obj.get("sEzsignfolderExternalid")
        })
        return _obj


