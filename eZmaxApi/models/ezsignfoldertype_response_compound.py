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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsignfoldertype_disposal import FieldEEzsignfoldertypeDisposal
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
from eZmaxApi.models.field_e_ezsignfoldertype_sendreminderfrequency import FieldEEzsignfoldertypeSendreminderfrequency
from eZmaxApi.models.multilingual_ezsignfoldertype_name import MultilingualEzsignfoldertypeName
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzsignfoldertypeResponseCompound(BaseModel):
    """
    A Ezsignfoldertype Object
    """ # noqa: E501
    pki_ezsignfoldertype_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldertype.", alias="pkiEzsignfoldertypeID")
    obj_ezsignfoldertype_name: MultilingualEzsignfoldertypeName = Field(alias="objEzsignfoldertypeName")
    fki_branding_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Branding", alias="fkiBrandingID")
    fki_billingentityinternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    fki_usergroup_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupID")
    fki_usergroup_id_restricted: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupIDRestricted")
    fki_ezsigntsarequirement_id: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|", alias="fkiEzsigntsarequirementID")
    s_branding_description_x: StrictStr = Field(description="The Description of the Branding in the language of the requester", alias="sBrandingDescriptionX")
    s_billingentityinternal_description_x: Optional[StrictStr] = Field(default=None, description="The description of the Billingentityinternal in the language of the requester", alias="sBillingentityinternalDescriptionX")
    s_ezsigntsarequirement_description_x: Optional[StrictStr] = Field(default=None, description="The description of the Ezsigntsarequirement in the language of the requester", alias="sEzsigntsarequirementDescriptionX")
    s_email_address_signed: Optional[StrictStr] = Field(default=None, description="The email address.", alias="sEmailAddressSigned")
    s_email_address_summary: Optional[StrictStr] = Field(default=None, description="The email address.", alias="sEmailAddressSummary")
    s_usergroup_name_x: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Name of the Usergroup in the language of the requester", alias="sUsergroupNameX")
    s_usergroup_name_x_restricted: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Name of the Usergroup in the language of the requester", alias="sUsergroupNameXRestricted")
    e_ezsignfoldertype_privacylevel: FieldEEzsignfoldertypePrivacylevel = Field(alias="eEzsignfoldertypePrivacylevel")
    e_ezsignfoldertype_sendreminderfrequency: Optional[FieldEEzsignfoldertypeSendreminderfrequency] = Field(default=None, alias="eEzsignfoldertypeSendreminderfrequency")
    i_ezsignfoldertype_archivaldays: Annotated[int, Field(le=180, strict=True, ge=0)] = Field(description="The number of days before the archival of Ezsignfolders created using this Ezsignfoldertype", alias="iEzsignfoldertypeArchivaldays")
    e_ezsignfoldertype_disposal: FieldEEzsignfoldertypeDisposal = Field(alias="eEzsignfoldertypeDisposal")
    i_ezsignfoldertype_disposaldays: Optional[Annotated[int, Field(le=9999, strict=True, ge=0)]] = Field(default=None, description="The number of days after the archival before the disposal of the Ezsignfolder", alias="iEzsignfoldertypeDisposaldays")
    i_ezsignfoldertype_deadlinedays: Annotated[int, Field(le=60, strict=True, ge=1)] = Field(description="The number of days to get all Ezsignsignatures", alias="iEzsignfoldertypeDeadlinedays")
    b_ezsignfoldertype_delegate: Optional[StrictBool] = Field(default=None, description="Wheter if delegation of signature is allowed to another user or not", alias="bEzsignfoldertypeDelegate")
    b_ezsignfoldertype_reassign: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signature is allowed to another signatory or not", alias="bEzsignfoldertypeReassign")
    b_ezsignfoldertype_sendattatchmentsigner: Optional[StrictBool] = Field(default=None, description="THIS FIELD WILL BE DELETED. Whether we send the Ezsigndocument and the proof as attachment in the email", alias="bEzsignfoldertypeSendattatchmentsigner")
    b_ezsignfoldertype_sendsignedtoezsignsigner: Optional[StrictBool] = Field(default=None, description="Whether we send an email to Ezsignsigner  when document is completed", alias="bEzsignfoldertypeSendsignedtoezsignsigner")
    b_ezsignfoldertype_sendsignedtouser: Optional[StrictBool] = Field(default=None, description="Whether we send an email to User who signed when document is completed", alias="bEzsignfoldertypeSendsignedtouser")
    b_ezsignfoldertype_sendattachmentezsignsigner: Optional[StrictBool] = Field(default=None, description="Whether we send the Ezsigndocument in the email to Ezsignsigner", alias="bEzsignfoldertypeSendattachmentezsignsigner")
    b_ezsignfoldertype_sendproofezsignsigner: Optional[StrictBool] = Field(default=None, description="Whether we send the proof in the email to Ezsignsigner", alias="bEzsignfoldertypeSendproofezsignsigner")
    b_ezsignfoldertype_sendattachmentuser: Optional[StrictBool] = Field(default=None, description="Whether we send the Ezsigndocument in the email to User", alias="bEzsignfoldertypeSendattachmentuser")
    b_ezsignfoldertype_sendproofuser: Optional[StrictBool] = Field(default=None, description="Whether we send the proof in the email to User", alias="bEzsignfoldertypeSendproofuser")
    b_ezsignfoldertype_sendproofemail: Optional[StrictBool] = Field(default=None, description="Whether we send the proof in the email to external recipient", alias="bEzsignfoldertypeSendproofemail")
    b_ezsignfoldertype_allowdownloadattachmentezsignsigner: Optional[StrictBool] = Field(default=None, description="Whether we allow the Ezsigndocument to be downloaded by an Ezsignsigner", alias="bEzsignfoldertypeAllowdownloadattachmentezsignsigner")
    b_ezsignfoldertype_allowdownloadproofezsignsigner: Optional[StrictBool] = Field(default=None, description="Whether we allow the proof to be downloaded by an Ezsignsigner", alias="bEzsignfoldertypeAllowdownloadproofezsignsigner")
    b_ezsignfoldertype_sendproofreceivealldocument: Optional[StrictBool] = Field(default=None, description="Whether we send the proof to user and Ezsignsigner who receive all documents.", alias="bEzsignfoldertypeSendproofreceivealldocument")
    b_ezsignfoldertype_sendsignedtodocumentowner: StrictBool = Field(description="Whether we send the signed Ezsigndocument to the Ezsigndocument's owner", alias="bEzsignfoldertypeSendsignedtodocumentowner")
    b_ezsignfoldertype_sendsignedtofolderowner: StrictBool = Field(description="Whether we send the signed Ezsigndocument to the Ezsignfolder's owner", alias="bEzsignfoldertypeSendsignedtofolderowner")
    b_ezsignfoldertype_sendsignedtofullgroup: Optional[StrictBool] = Field(default=None, description="Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders", alias="bEzsignfoldertypeSendsignedtofullgroup")
    b_ezsignfoldertype_sendsignedtolimitedgroup: Optional[StrictBool] = Field(default=None, description="THIS FIELD WILL BE DELETED. Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders", alias="bEzsignfoldertypeSendsignedtolimitedgroup")
    b_ezsignfoldertype_sendsignedtocolleague: StrictBool = Field(description="Whether we send the signed Ezsigndocument to the colleagues", alias="bEzsignfoldertypeSendsignedtocolleague")
    b_ezsignfoldertype_sendsummarytodocumentowner: StrictBool = Field(description="Whether we send the summary to the Ezsigndocument's owner", alias="bEzsignfoldertypeSendsummarytodocumentowner")
    b_ezsignfoldertype_sendsummarytofolderowner: StrictBool = Field(description="Whether we send the summary to the Ezsignfolder's owner", alias="bEzsignfoldertypeSendsummarytofolderowner")
    b_ezsignfoldertype_sendsummarytofullgroup: Optional[StrictBool] = Field(default=None, description="Whether we send the summary to the Usergroup that has acces to all Ezsignfolders", alias="bEzsignfoldertypeSendsummarytofullgroup")
    b_ezsignfoldertype_sendsummarytolimitedgroup: Optional[StrictBool] = Field(default=None, description="Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders", alias="bEzsignfoldertypeSendsummarytolimitedgroup")
    b_ezsignfoldertype_sendsummarytocolleague: StrictBool = Field(description="Whether we send the summary to the colleagues", alias="bEzsignfoldertypeSendsummarytocolleague")
    b_ezsignfoldertype_includeproofsigner: Optional[StrictBool] = Field(default=None, description="THIS FIELD WILL BE DELETED. Whether we include the proof with the signed Ezsigndocument for Ezsignsigners", alias="bEzsignfoldertypeIncludeproofsigner")
    b_ezsignfoldertype_includeproofuser: StrictBool = Field(description="Whether we include the proof with the signed Ezsigndocument for users", alias="bEzsignfoldertypeIncludeproofuser")
    b_ezsignfoldertype_isactive: StrictBool = Field(description="Whether the Ezsignfoldertype is active or not", alias="bEzsignfoldertypeIsactive")
    a_fki_user_id_signed: Optional[List[Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="a_fkiUserIDSigned")
    a_fki_user_id_summary: Optional[List[Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="a_fkiUserIDSummary")
    __properties: ClassVar[List[str]] = ["pkiEzsignfoldertypeID", "objEzsignfoldertypeName", "fkiBrandingID", "fkiBillingentityinternalID", "fkiUsergroupID", "fkiUsergroupIDRestricted", "fkiEzsigntsarequirementID", "sBrandingDescriptionX", "sBillingentityinternalDescriptionX", "sEzsigntsarequirementDescriptionX", "sEmailAddressSigned", "sEmailAddressSummary", "sUsergroupNameX", "sUsergroupNameXRestricted", "eEzsignfoldertypePrivacylevel", "eEzsignfoldertypeSendreminderfrequency", "iEzsignfoldertypeArchivaldays", "eEzsignfoldertypeDisposal", "iEzsignfoldertypeDisposaldays", "iEzsignfoldertypeDeadlinedays", "bEzsignfoldertypeDelegate", "bEzsignfoldertypeReassign", "bEzsignfoldertypeSendattatchmentsigner", "bEzsignfoldertypeSendsignedtoezsignsigner", "bEzsignfoldertypeSendsignedtouser", "bEzsignfoldertypeSendattachmentezsignsigner", "bEzsignfoldertypeSendproofezsignsigner", "bEzsignfoldertypeSendattachmentuser", "bEzsignfoldertypeSendproofuser", "bEzsignfoldertypeSendproofemail", "bEzsignfoldertypeAllowdownloadattachmentezsignsigner", "bEzsignfoldertypeAllowdownloadproofezsignsigner", "bEzsignfoldertypeSendproofreceivealldocument", "bEzsignfoldertypeSendsignedtodocumentowner", "bEzsignfoldertypeSendsignedtofolderowner", "bEzsignfoldertypeSendsignedtofullgroup", "bEzsignfoldertypeSendsignedtolimitedgroup", "bEzsignfoldertypeSendsignedtocolleague", "bEzsignfoldertypeSendsummarytodocumentowner", "bEzsignfoldertypeSendsummarytofolderowner", "bEzsignfoldertypeSendsummarytofullgroup", "bEzsignfoldertypeSendsummarytolimitedgroup", "bEzsignfoldertypeSendsummarytocolleague", "bEzsignfoldertypeIncludeproofsigner", "bEzsignfoldertypeIncludeproofuser", "bEzsignfoldertypeIsactive", "a_fkiUserIDSigned", "a_fkiUserIDSummary"]

    @field_validator('s_usergroup_name_x')
    def s_usergroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_usergroup_name_x_restricted')
    def s_usergroup_name_x_restricted_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EzsignfoldertypeResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype_name
        if self.obj_ezsignfoldertype_name:
            _dict['objEzsignfoldertypeName'] = self.obj_ezsignfoldertype_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EzsignfoldertypeResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfoldertypeID": obj.get("pkiEzsignfoldertypeID"),
            "objEzsignfoldertypeName": MultilingualEzsignfoldertypeName.from_dict(obj.get("objEzsignfoldertypeName")) if obj.get("objEzsignfoldertypeName") is not None else None,
            "fkiBrandingID": obj.get("fkiBrandingID"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "fkiUsergroupID": obj.get("fkiUsergroupID"),
            "fkiUsergroupIDRestricted": obj.get("fkiUsergroupIDRestricted"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "sBrandingDescriptionX": obj.get("sBrandingDescriptionX"),
            "sBillingentityinternalDescriptionX": obj.get("sBillingentityinternalDescriptionX"),
            "sEzsigntsarequirementDescriptionX": obj.get("sEzsigntsarequirementDescriptionX"),
            "sEmailAddressSigned": obj.get("sEmailAddressSigned"),
            "sEmailAddressSummary": obj.get("sEmailAddressSummary"),
            "sUsergroupNameX": obj.get("sUsergroupNameX"),
            "sUsergroupNameXRestricted": obj.get("sUsergroupNameXRestricted"),
            "eEzsignfoldertypePrivacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "eEzsignfoldertypeSendreminderfrequency": obj.get("eEzsignfoldertypeSendreminderfrequency"),
            "iEzsignfoldertypeArchivaldays": obj.get("iEzsignfoldertypeArchivaldays"),
            "eEzsignfoldertypeDisposal": obj.get("eEzsignfoldertypeDisposal"),
            "iEzsignfoldertypeDisposaldays": obj.get("iEzsignfoldertypeDisposaldays"),
            "iEzsignfoldertypeDeadlinedays": obj.get("iEzsignfoldertypeDeadlinedays"),
            "bEzsignfoldertypeDelegate": obj.get("bEzsignfoldertypeDelegate"),
            "bEzsignfoldertypeReassign": obj.get("bEzsignfoldertypeReassign"),
            "bEzsignfoldertypeSendattatchmentsigner": obj.get("bEzsignfoldertypeSendattatchmentsigner"),
            "bEzsignfoldertypeSendsignedtoezsignsigner": obj.get("bEzsignfoldertypeSendsignedtoezsignsigner"),
            "bEzsignfoldertypeSendsignedtouser": obj.get("bEzsignfoldertypeSendsignedtouser"),
            "bEzsignfoldertypeSendattachmentezsignsigner": obj.get("bEzsignfoldertypeSendattachmentezsignsigner"),
            "bEzsignfoldertypeSendproofezsignsigner": obj.get("bEzsignfoldertypeSendproofezsignsigner"),
            "bEzsignfoldertypeSendattachmentuser": obj.get("bEzsignfoldertypeSendattachmentuser"),
            "bEzsignfoldertypeSendproofuser": obj.get("bEzsignfoldertypeSendproofuser"),
            "bEzsignfoldertypeSendproofemail": obj.get("bEzsignfoldertypeSendproofemail"),
            "bEzsignfoldertypeAllowdownloadattachmentezsignsigner": obj.get("bEzsignfoldertypeAllowdownloadattachmentezsignsigner"),
            "bEzsignfoldertypeAllowdownloadproofezsignsigner": obj.get("bEzsignfoldertypeAllowdownloadproofezsignsigner"),
            "bEzsignfoldertypeSendproofreceivealldocument": obj.get("bEzsignfoldertypeSendproofreceivealldocument"),
            "bEzsignfoldertypeSendsignedtodocumentowner": obj.get("bEzsignfoldertypeSendsignedtodocumentowner"),
            "bEzsignfoldertypeSendsignedtofolderowner": obj.get("bEzsignfoldertypeSendsignedtofolderowner"),
            "bEzsignfoldertypeSendsignedtofullgroup": obj.get("bEzsignfoldertypeSendsignedtofullgroup"),
            "bEzsignfoldertypeSendsignedtolimitedgroup": obj.get("bEzsignfoldertypeSendsignedtolimitedgroup"),
            "bEzsignfoldertypeSendsignedtocolleague": obj.get("bEzsignfoldertypeSendsignedtocolleague"),
            "bEzsignfoldertypeSendsummarytodocumentowner": obj.get("bEzsignfoldertypeSendsummarytodocumentowner"),
            "bEzsignfoldertypeSendsummarytofolderowner": obj.get("bEzsignfoldertypeSendsummarytofolderowner"),
            "bEzsignfoldertypeSendsummarytofullgroup": obj.get("bEzsignfoldertypeSendsummarytofullgroup"),
            "bEzsignfoldertypeSendsummarytolimitedgroup": obj.get("bEzsignfoldertypeSendsummarytolimitedgroup"),
            "bEzsignfoldertypeSendsummarytocolleague": obj.get("bEzsignfoldertypeSendsummarytocolleague"),
            "bEzsignfoldertypeIncludeproofsigner": obj.get("bEzsignfoldertypeIncludeproofsigner"),
            "bEzsignfoldertypeIncludeproofuser": obj.get("bEzsignfoldertypeIncludeproofuser"),
            "bEzsignfoldertypeIsactive": obj.get("bEzsignfoldertypeIsactive"),
            "a_fkiUserIDSigned": obj.get("a_fkiUserIDSigned"),
            "a_fkiUserIDSummary": obj.get("a_fkiUserIDSummary")
        })
        return _obj


