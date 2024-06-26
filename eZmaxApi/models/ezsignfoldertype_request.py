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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsignfoldertype_completion import FieldEEzsignfoldertypeCompletion
from eZmaxApi.models.field_e_ezsignfoldertype_disposal import FieldEEzsignfoldertypeDisposal
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
from eZmaxApi.models.field_e_ezsignfoldertype_sendreminderfrequency import FieldEEzsignfoldertypeSendreminderfrequency
from eZmaxApi.models.multilingual_ezsignfoldertype_name import MultilingualEzsignfoldertypeName
from typing import Optional, Set
from typing_extensions import Self

class EzsignfoldertypeRequest(BaseModel):
    """
    A Ezsignfoldertype Object
    """ # noqa: E501
    pki_ezsignfoldertype_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldertype.", alias="pkiEzsignfoldertypeID")
    obj_ezsignfoldertype_name: MultilingualEzsignfoldertypeName = Field(alias="objEzsignfoldertypeName")
    fki_branding_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Branding", alias="fkiBrandingID")
    fki_billingentityinternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    fki_usergroup_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupID")
    fki_usergroup_id_restricted: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupIDRestricted")
    fki_ezsigntsarequirement_id: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|", alias="fkiEzsigntsarequirementID")
    s_email_address_signed: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddressSigned")
    s_email_address_summary: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddressSummary")
    e_ezsignfoldertype_privacylevel: FieldEEzsignfoldertypePrivacylevel = Field(alias="eEzsignfoldertypePrivacylevel")
    e_ezsignfoldertype_sendreminderfrequency: Optional[FieldEEzsignfoldertypeSendreminderfrequency] = Field(default=None, alias="eEzsignfoldertypeSendreminderfrequency")
    i_ezsignfoldertype_archivaldays: Annotated[int, Field(le=180, strict=True, ge=0)] = Field(description="The number of days before the archival of Ezsignfolders created using this Ezsignfoldertype", alias="iEzsignfoldertypeArchivaldays")
    e_ezsignfoldertype_disposal: FieldEEzsignfoldertypeDisposal = Field(alias="eEzsignfoldertypeDisposal")
    e_ezsignfoldertype_completion: FieldEEzsignfoldertypeCompletion = Field(alias="eEzsignfoldertypeCompletion")
    i_ezsignfoldertype_disposaldays: Optional[Annotated[int, Field(le=9999, strict=True, ge=0)]] = Field(default=None, description="The number of days after the archival before the disposal of the Ezsignfolder", alias="iEzsignfoldertypeDisposaldays")
    i_ezsignfoldertype_deadlinedays: Annotated[int, Field(le=60, strict=True, ge=1)] = Field(description="The number of days to get all Ezsignsignatures", alias="iEzsignfoldertypeDeadlinedays")
    b_ezsignfoldertype_delegate: Optional[StrictBool] = Field(default=None, description="Wheter if delegation of signature is allowed to another user or not", alias="bEzsignfoldertypeDelegate")
    b_ezsignfoldertype_discussion: Optional[StrictBool] = Field(default=None, description="Wheter if creating a new Discussion is allowed or not", alias="bEzsignfoldertypeDiscussion")
    b_ezsignfoldertype_reassignezsignsigner: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signature is allowed by a signatory to another signatory or not", alias="bEzsignfoldertypeReassignezsignsigner")
    b_ezsignfoldertype_reassignuser: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signature is allowed by a user to a signatory or another user or not", alias="bEzsignfoldertypeReassignuser")
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
    b_ezsignfoldertype_isactive: StrictBool = Field(description="Whether the Ezsignfoldertype is active or not", alias="bEzsignfoldertypeIsactive")
    __properties: ClassVar[List[str]] = ["pkiEzsignfoldertypeID", "objEzsignfoldertypeName", "fkiBrandingID", "fkiBillingentityinternalID", "fkiUsergroupID", "fkiUsergroupIDRestricted", "fkiEzsigntsarequirementID", "sEmailAddressSigned", "sEmailAddressSummary", "eEzsignfoldertypePrivacylevel", "eEzsignfoldertypeSendreminderfrequency", "iEzsignfoldertypeArchivaldays", "eEzsignfoldertypeDisposal", "eEzsignfoldertypeCompletion", "iEzsignfoldertypeDisposaldays", "iEzsignfoldertypeDeadlinedays", "bEzsignfoldertypeDelegate", "bEzsignfoldertypeDiscussion", "bEzsignfoldertypeReassignezsignsigner", "bEzsignfoldertypeReassignuser", "bEzsignfoldertypeSendsignedtoezsignsigner", "bEzsignfoldertypeSendsignedtouser", "bEzsignfoldertypeSendattachmentezsignsigner", "bEzsignfoldertypeSendproofezsignsigner", "bEzsignfoldertypeSendattachmentuser", "bEzsignfoldertypeSendproofuser", "bEzsignfoldertypeSendproofemail", "bEzsignfoldertypeAllowdownloadattachmentezsignsigner", "bEzsignfoldertypeAllowdownloadproofezsignsigner", "bEzsignfoldertypeSendproofreceivealldocument", "bEzsignfoldertypeSendsignedtodocumentowner", "bEzsignfoldertypeSendsignedtofolderowner", "bEzsignfoldertypeSendsignedtofullgroup", "bEzsignfoldertypeSendsignedtolimitedgroup", "bEzsignfoldertypeSendsignedtocolleague", "bEzsignfoldertypeSendsummarytodocumentowner", "bEzsignfoldertypeSendsummarytofolderowner", "bEzsignfoldertypeSendsummarytofullgroup", "bEzsignfoldertypeSendsummarytolimitedgroup", "bEzsignfoldertypeSendsummarytocolleague", "bEzsignfoldertypeIsactive"]

    @field_validator('s_email_address_signed')
    def s_email_address_signed_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
        return value

    @field_validator('s_email_address_summary')
    def s_email_address_summary_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
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
        """Create an instance of EzsignfoldertypeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype_name
        if self.obj_ezsignfoldertype_name:
            _dict['objEzsignfoldertypeName'] = self.obj_ezsignfoldertype_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignfoldertypeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfoldertypeID": obj.get("pkiEzsignfoldertypeID"),
            "objEzsignfoldertypeName": MultilingualEzsignfoldertypeName.from_dict(obj["objEzsignfoldertypeName"]) if obj.get("objEzsignfoldertypeName") is not None else None,
            "fkiBrandingID": obj.get("fkiBrandingID"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "fkiUsergroupID": obj.get("fkiUsergroupID"),
            "fkiUsergroupIDRestricted": obj.get("fkiUsergroupIDRestricted"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "sEmailAddressSigned": obj.get("sEmailAddressSigned"),
            "sEmailAddressSummary": obj.get("sEmailAddressSummary"),
            "eEzsignfoldertypePrivacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "eEzsignfoldertypeSendreminderfrequency": obj.get("eEzsignfoldertypeSendreminderfrequency"),
            "iEzsignfoldertypeArchivaldays": obj.get("iEzsignfoldertypeArchivaldays"),
            "eEzsignfoldertypeDisposal": obj.get("eEzsignfoldertypeDisposal"),
            "eEzsignfoldertypeCompletion": obj.get("eEzsignfoldertypeCompletion"),
            "iEzsignfoldertypeDisposaldays": obj.get("iEzsignfoldertypeDisposaldays"),
            "iEzsignfoldertypeDeadlinedays": obj.get("iEzsignfoldertypeDeadlinedays"),
            "bEzsignfoldertypeDelegate": obj.get("bEzsignfoldertypeDelegate"),
            "bEzsignfoldertypeDiscussion": obj.get("bEzsignfoldertypeDiscussion"),
            "bEzsignfoldertypeReassignezsignsigner": obj.get("bEzsignfoldertypeReassignezsignsigner"),
            "bEzsignfoldertypeReassignuser": obj.get("bEzsignfoldertypeReassignuser"),
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
            "bEzsignfoldertypeIsactive": obj.get("bEzsignfoldertypeIsactive")
        })
        return _obj


