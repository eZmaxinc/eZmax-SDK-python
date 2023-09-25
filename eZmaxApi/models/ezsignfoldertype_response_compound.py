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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr, validator
from eZmaxApi.models.field_e_ezsignfoldertype_disposal import FieldEEzsignfoldertypeDisposal
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
from eZmaxApi.models.field_e_ezsignfoldertype_sendreminderfrequency import FieldEEzsignfoldertypeSendreminderfrequency
from eZmaxApi.models.multilingual_ezsignfoldertype_name import MultilingualEzsignfoldertypeName

class EzsignfoldertypeResponseCompound(BaseModel):
    """
    A Ezsignfoldertype Object  # noqa: E501
    """
    pki_ezsignfoldertype_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsignfoldertypeID", description="The unique ID of the Ezsignfoldertype.")
    obj_ezsignfoldertype_name: MultilingualEzsignfoldertypeName = Field(..., alias="objEzsignfoldertypeName")
    fki_branding_id: conint(strict=True, ge=0) = Field(..., alias="fkiBrandingID", description="The unique ID of the Branding")
    fki_billingentityinternal_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiBillingentityinternalID", description="The unique ID of the Billingentityinternal.")
    fki_usergroup_id: Optional[conint(strict=True, le=255, ge=0)] = Field(None, alias="fkiUsergroupID", description="The unique ID of the Usergroup")
    fki_usergroup_id_restricted: Optional[conint(strict=True, le=255, ge=0)] = Field(None, alias="fkiUsergroupIDRestricted", description="The unique ID of the Usergroup")
    fki_ezsigntsarequirement_id: Optional[conint(strict=True, le=3, ge=1)] = Field(None, alias="fkiEzsigntsarequirementID", description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|")
    s_branding_description_x: StrictStr = Field(..., alias="sBrandingDescriptionX", description="The Description of the Branding in the language of the requester")
    s_billingentityinternal_description_x: Optional[StrictStr] = Field(None, alias="sBillingentityinternalDescriptionX", description="The description of the Billingentityinternal in the language of the requester")
    s_ezsigntsarequirement_description_x: Optional[StrictStr] = Field(None, alias="sEzsigntsarequirementDescriptionX", description="The description of the Ezsigntsarequirement in the language of the requester")
    s_email_address_signed: Optional[StrictStr] = Field(None, alias="sEmailAddressSigned", description="The email address.")
    s_email_address_summary: Optional[StrictStr] = Field(None, alias="sEmailAddressSummary", description="The email address.")
    s_usergroup_name_x: Optional[constr(strict=True)] = Field(None, alias="sUsergroupNameX", description="The Name of the Usergroup in the language of the requester")
    s_usergroup_name_x_restricted: Optional[constr(strict=True)] = Field(None, alias="sUsergroupNameXRestricted", description="The Name of the Usergroup in the language of the requester")
    e_ezsignfoldertype_privacylevel: FieldEEzsignfoldertypePrivacylevel = Field(..., alias="eEzsignfoldertypePrivacylevel")
    e_ezsignfoldertype_sendreminderfrequency: Optional[FieldEEzsignfoldertypeSendreminderfrequency] = Field(None, alias="eEzsignfoldertypeSendreminderfrequency")
    i_ezsignfoldertype_archivaldays: conint(strict=True, le=180, ge=0) = Field(..., alias="iEzsignfoldertypeArchivaldays", description="The number of days before the archival of Ezsignfolders created using this Ezsignfoldertype")
    e_ezsignfoldertype_disposal: FieldEEzsignfoldertypeDisposal = Field(..., alias="eEzsignfoldertypeDisposal")
    i_ezsignfoldertype_disposaldays: Optional[conint(strict=True, le=9999, ge=0)] = Field(None, alias="iEzsignfoldertypeDisposaldays", description="The number of days after the archival before the disposal of the Ezsignfolder")
    i_ezsignfoldertype_deadlinedays: conint(strict=True, le=60, ge=1) = Field(..., alias="iEzsignfoldertypeDeadlinedays", description="The number of days to get all Ezsignsignatures")
    b_ezsignfoldertype_delegate: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeDelegate", description="Wheter if delegation of signature is allowed to another user or not")
    b_ezsignfoldertype_reassign: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeReassign", description="Wheter if Reassignment of signature is allowed to another signatory or not")
    b_ezsignfoldertype_sendattatchmentsigner: StrictBool = Field(..., alias="bEzsignfoldertypeSendattatchmentsigner", description="Whether we send the Ezsigndocument and the proof as attachment in the email")
    b_ezsignfoldertype_sendsignedtodocumentowner: StrictBool = Field(..., alias="bEzsignfoldertypeSendsignedtodocumentowner", description="Whether we send the signed Ezsigndocument to the Ezsigndocument's owner")
    b_ezsignfoldertype_sendsignedtofolderowner: StrictBool = Field(..., alias="bEzsignfoldertypeSendsignedtofolderowner", description="Whether we send the signed Ezsigndocument to the Ezsignfolder's owner")
    b_ezsignfoldertype_sendsignedtofullgroup: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeSendsignedtofullgroup", description="Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders")
    b_ezsignfoldertype_sendsignedtolimitedgroup: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeSendsignedtolimitedgroup", description="Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders")
    b_ezsignfoldertype_sendsignedtocolleague: StrictBool = Field(..., alias="bEzsignfoldertypeSendsignedtocolleague", description="Whether we send the signed Ezsigndocument to the colleagues")
    b_ezsignfoldertype_sendsummarytodocumentowner: StrictBool = Field(..., alias="bEzsignfoldertypeSendsummarytodocumentowner", description="Whether we send the summary to the Ezsigndocument's owner")
    b_ezsignfoldertype_sendsummarytofolderowner: StrictBool = Field(..., alias="bEzsignfoldertypeSendsummarytofolderowner", description="Whether we send the summary to the Ezsignfolder's owner")
    b_ezsignfoldertype_sendsummarytofullgroup: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeSendsummarytofullgroup", description="Whether we send the summary to the Usergroup that has acces to all Ezsignfolders")
    b_ezsignfoldertype_sendsummarytolimitedgroup: Optional[StrictBool] = Field(None, alias="bEzsignfoldertypeSendsummarytolimitedgroup", description="Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders")
    b_ezsignfoldertype_sendsummarytocolleague: StrictBool = Field(..., alias="bEzsignfoldertypeSendsummarytocolleague", description="Whether we send the summary to the colleagues")
    b_ezsignfoldertype_includeproofsigner: StrictBool = Field(..., alias="bEzsignfoldertypeIncludeproofsigner", description="Whether we include the proof with the signed Ezsigndocument for Ezsignsigners")
    b_ezsignfoldertype_includeproofuser: StrictBool = Field(..., alias="bEzsignfoldertypeIncludeproofuser", description="Whether we include the proof with the signed Ezsigndocument for users")
    b_ezsignfoldertype_isactive: StrictBool = Field(..., alias="bEzsignfoldertypeIsactive", description="Whether the Ezsignfoldertype is active or not")
    a_fki_user_id_signed: Optional[conlist(conint(strict=True, ge=0))] = Field(None, alias="a_fkiUserIDSigned")
    a_fki_user_id_summary: Optional[conlist(conint(strict=True, ge=0))] = Field(None, alias="a_fkiUserIDSummary")
    __properties = ["pkiEzsignfoldertypeID", "objEzsignfoldertypeName", "fkiBrandingID", "fkiBillingentityinternalID", "fkiUsergroupID", "fkiUsergroupIDRestricted", "fkiEzsigntsarequirementID", "sBrandingDescriptionX", "sBillingentityinternalDescriptionX", "sEzsigntsarequirementDescriptionX", "sEmailAddressSigned", "sEmailAddressSummary", "sUsergroupNameX", "sUsergroupNameXRestricted", "eEzsignfoldertypePrivacylevel", "eEzsignfoldertypeSendreminderfrequency", "iEzsignfoldertypeArchivaldays", "eEzsignfoldertypeDisposal", "iEzsignfoldertypeDisposaldays", "iEzsignfoldertypeDeadlinedays", "bEzsignfoldertypeDelegate", "bEzsignfoldertypeReassign", "bEzsignfoldertypeSendattatchmentsigner", "bEzsignfoldertypeSendsignedtodocumentowner", "bEzsignfoldertypeSendsignedtofolderowner", "bEzsignfoldertypeSendsignedtofullgroup", "bEzsignfoldertypeSendsignedtolimitedgroup", "bEzsignfoldertypeSendsignedtocolleague", "bEzsignfoldertypeSendsummarytodocumentowner", "bEzsignfoldertypeSendsummarytofolderowner", "bEzsignfoldertypeSendsummarytofullgroup", "bEzsignfoldertypeSendsummarytolimitedgroup", "bEzsignfoldertypeSendsummarytocolleague", "bEzsignfoldertypeIncludeproofsigner", "bEzsignfoldertypeIncludeproofuser", "bEzsignfoldertypeIsactive", "a_fkiUserIDSigned", "a_fkiUserIDSummary"]

    @validator('s_usergroup_name_x')
    def s_usergroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @validator('s_usergroup_name_x_restricted')
    def s_usergroup_name_x_restricted_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
    def from_json(cls, json_str: str) -> EzsignfoldertypeResponseCompound:
        """Create an instance of EzsignfoldertypeResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype_name
        if self.obj_ezsignfoldertype_name:
            _dict['objEzsignfoldertypeName'] = self.obj_ezsignfoldertype_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfoldertypeResponseCompound:
        """Create an instance of EzsignfoldertypeResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfoldertypeResponseCompound.parse_obj(obj)

        _obj = EzsignfoldertypeResponseCompound.parse_obj({
            "pki_ezsignfoldertype_id": obj.get("pkiEzsignfoldertypeID"),
            "obj_ezsignfoldertype_name": MultilingualEzsignfoldertypeName.from_dict(obj.get("objEzsignfoldertypeName")) if obj.get("objEzsignfoldertypeName") is not None else None,
            "fki_branding_id": obj.get("fkiBrandingID"),
            "fki_billingentityinternal_id": obj.get("fkiBillingentityinternalID"),
            "fki_usergroup_id": obj.get("fkiUsergroupID"),
            "fki_usergroup_id_restricted": obj.get("fkiUsergroupIDRestricted"),
            "fki_ezsigntsarequirement_id": obj.get("fkiEzsigntsarequirementID"),
            "s_branding_description_x": obj.get("sBrandingDescriptionX"),
            "s_billingentityinternal_description_x": obj.get("sBillingentityinternalDescriptionX"),
            "s_ezsigntsarequirement_description_x": obj.get("sEzsigntsarequirementDescriptionX"),
            "s_email_address_signed": obj.get("sEmailAddressSigned"),
            "s_email_address_summary": obj.get("sEmailAddressSummary"),
            "s_usergroup_name_x": obj.get("sUsergroupNameX"),
            "s_usergroup_name_x_restricted": obj.get("sUsergroupNameXRestricted"),
            "e_ezsignfoldertype_privacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "e_ezsignfoldertype_sendreminderfrequency": obj.get("eEzsignfoldertypeSendreminderfrequency"),
            "i_ezsignfoldertype_archivaldays": obj.get("iEzsignfoldertypeArchivaldays"),
            "e_ezsignfoldertype_disposal": obj.get("eEzsignfoldertypeDisposal"),
            "i_ezsignfoldertype_disposaldays": obj.get("iEzsignfoldertypeDisposaldays"),
            "i_ezsignfoldertype_deadlinedays": obj.get("iEzsignfoldertypeDeadlinedays"),
            "b_ezsignfoldertype_delegate": obj.get("bEzsignfoldertypeDelegate"),
            "b_ezsignfoldertype_reassign": obj.get("bEzsignfoldertypeReassign"),
            "b_ezsignfoldertype_sendattatchmentsigner": obj.get("bEzsignfoldertypeSendattatchmentsigner"),
            "b_ezsignfoldertype_sendsignedtodocumentowner": obj.get("bEzsignfoldertypeSendsignedtodocumentowner"),
            "b_ezsignfoldertype_sendsignedtofolderowner": obj.get("bEzsignfoldertypeSendsignedtofolderowner"),
            "b_ezsignfoldertype_sendsignedtofullgroup": obj.get("bEzsignfoldertypeSendsignedtofullgroup"),
            "b_ezsignfoldertype_sendsignedtolimitedgroup": obj.get("bEzsignfoldertypeSendsignedtolimitedgroup"),
            "b_ezsignfoldertype_sendsignedtocolleague": obj.get("bEzsignfoldertypeSendsignedtocolleague"),
            "b_ezsignfoldertype_sendsummarytodocumentowner": obj.get("bEzsignfoldertypeSendsummarytodocumentowner"),
            "b_ezsignfoldertype_sendsummarytofolderowner": obj.get("bEzsignfoldertypeSendsummarytofolderowner"),
            "b_ezsignfoldertype_sendsummarytofullgroup": obj.get("bEzsignfoldertypeSendsummarytofullgroup"),
            "b_ezsignfoldertype_sendsummarytolimitedgroup": obj.get("bEzsignfoldertypeSendsummarytolimitedgroup"),
            "b_ezsignfoldertype_sendsummarytocolleague": obj.get("bEzsignfoldertypeSendsummarytocolleague"),
            "b_ezsignfoldertype_includeproofsigner": obj.get("bEzsignfoldertypeIncludeproofsigner"),
            "b_ezsignfoldertype_includeproofuser": obj.get("bEzsignfoldertypeIncludeproofuser"),
            "b_ezsignfoldertype_isactive": obj.get("bEzsignfoldertypeIsactive"),
            "a_fki_user_id_signed": obj.get("a_fkiUserIDSigned"),
            "a_fki_user_id_summary": obj.get("a_fkiUserIDSummary")
        })
        return _obj


