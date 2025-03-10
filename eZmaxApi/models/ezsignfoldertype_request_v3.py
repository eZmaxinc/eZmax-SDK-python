# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
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
from eZmaxApi.models.field_e_ezsignfoldertype_documentdependency import FieldEEzsignfoldertypeDocumentdependency
from eZmaxApi.models.field_e_ezsignfoldertype_pdfanoncompliantaction import FieldEEzsignfoldertypePdfanoncompliantaction
from eZmaxApi.models.field_e_ezsignfoldertype_pdfarequirement import FieldEEzsignfoldertypePdfarequirement
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
from eZmaxApi.models.field_e_ezsignfoldertype_signeraccess import FieldEEzsignfoldertypeSigneraccess
from eZmaxApi.models.multilingual_ezsignfoldertype_name import MultilingualEzsignfoldertypeName
from typing import Optional, Set
from typing_extensions import Self

class EzsignfoldertypeRequestV3(BaseModel):
    """
    A Ezsignfoldertype Object
    """ # noqa: E501
    pki_ezsignfoldertype_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldertype.", alias="pkiEzsignfoldertypeID")
    obj_ezsignfoldertype_name: MultilingualEzsignfoldertypeName = Field(alias="objEzsignfoldertypeName")
    fki_branding_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Branding", alias="fkiBrandingID")
    fki_billingentityinternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    fki_ezsigntsarequirement_id: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|", alias="fkiEzsigntsarequirementID")
    fki_font_id_annotation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Font", alias="fkiFontIDAnnotation")
    fki_font_id_formfield: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Font", alias="fkiFontIDFormfield")
    fki_font_id_signature: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Font", alias="fkiFontIDSignature")
    fki_pdfalevel_id_convert: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Pdfalevel", alias="fkiPdfalevelIDConvert")
    a_fki_pdfalevel_id: Optional[List[Annotated[int, Field(le=255, strict=True, ge=0)]]] = Field(default=None, alias="a_fkiPdfalevelID")
    a_fki_userlogintype_id: List[Annotated[int, Field(strict=True, ge=0)]] = Field(alias="a_fkiUserlogintypeID")
    a_fki_usergroup_id_all: Optional[List[Annotated[int, Field(le=255, strict=True, ge=0)]]] = Field(default=None, alias="a_fkiUsergroupIDAll")
    a_fki_usergroup_id_restricted: Optional[List[Annotated[int, Field(le=255, strict=True, ge=0)]]] = Field(default=None, alias="a_fkiUsergroupIDRestricted")
    a_fki_usergroup_id_template: Optional[List[Annotated[int, Field(le=255, strict=True, ge=0)]]] = Field(default=None, alias="a_fkiUsergroupIDTemplate")
    e_ezsignfoldertype_documentdependency: Optional[FieldEEzsignfoldertypeDocumentdependency] = Field(default=None, alias="eEzsignfoldertypeDocumentdependency")
    s_email_address_signed: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddressSigned")
    s_email_address_summary: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddressSummary")
    e_ezsignfoldertype_pdfarequirement: Optional[FieldEEzsignfoldertypePdfarequirement] = Field(default=None, alias="eEzsignfoldertypePdfarequirement")
    e_ezsignfoldertype_pdfanoncompliantaction: Optional[FieldEEzsignfoldertypePdfanoncompliantaction] = Field(default=None, alias="eEzsignfoldertypePdfanoncompliantaction")
    e_ezsignfoldertype_privacylevel: FieldEEzsignfoldertypePrivacylevel = Field(alias="eEzsignfoldertypePrivacylevel")
    i_ezsignfoldertype_fontsizeannotation: Optional[Annotated[int, Field(le=255, strict=True, ge=1)]] = Field(default=None, description="Font size for annotations", alias="iEzsignfoldertypeFontsizeannotation")
    i_ezsignfoldertype_fontsizeformfield: Optional[Annotated[int, Field(le=255, strict=True, ge=1)]] = Field(default=None, description="Font size for form fields", alias="iEzsignfoldertypeFontsizeformfield")
    i_ezsignfoldertype_sendreminderfirstdays: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The number of days before the the first reminder sending", alias="iEzsignfoldertypeSendreminderfirstdays")
    i_ezsignfoldertype_sendreminderotherdays: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The number of days after the first reminder sending", alias="iEzsignfoldertypeSendreminderotherdays")
    i_ezsignfoldertype_archivaldays: Annotated[int, Field(le=180, strict=True, ge=0)] = Field(description="The number of days before the archival of Ezsignfolders created using this Ezsignfoldertype", alias="iEzsignfoldertypeArchivaldays")
    e_ezsignfoldertype_disposal: FieldEEzsignfoldertypeDisposal = Field(alias="eEzsignfoldertypeDisposal")
    e_ezsignfoldertype_completion: FieldEEzsignfoldertypeCompletion = Field(alias="eEzsignfoldertypeCompletion")
    i_ezsignfoldertype_disposaldays: Optional[Annotated[int, Field(le=9999, strict=True, ge=0)]] = Field(default=None, description="The number of days after the archival before the disposal of the Ezsignfolder", alias="iEzsignfoldertypeDisposaldays")
    i_ezsignfoldertype_deadlinedays: Annotated[int, Field(le=60, strict=True, ge=1)] = Field(description="The number of days to get all Ezsignsignatures", alias="iEzsignfoldertypeDeadlinedays")
    b_ezsignfoldertype_prematurelyendautomatically: Optional[StrictBool] = Field(default=None, description="Wheter if document will be ended prematurely after Ezsignfolder expires.", alias="bEzsignfoldertypePrematurelyendautomatically")
    i_ezsignfoldertype_prematurelyendautomaticallydays: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="Number of days between Ezsignfolder expiration and automatic prematurely end of Ezsigndocuments.", alias="iEzsignfoldertypePrematurelyendautomaticallydays")
    b_ezsignfoldertype_automaticsignature: Optional[StrictBool] = Field(default=None, description="Whether we allow the automatic signature by an User", alias="bEzsignfoldertypeAutomaticsignature")
    b_ezsignfoldertype_delegate: Optional[StrictBool] = Field(default=None, description="Wheter if delegation of signature is allowed to another user or not", alias="bEzsignfoldertypeDelegate")
    b_ezsignfoldertype_discussion: Optional[StrictBool] = Field(default=None, description="Wheter if creating a new Discussion is allowed or not", alias="bEzsignfoldertypeDiscussion")
    b_ezsignfoldertype_logrecipientinproof: Optional[StrictBool] = Field(default=None, description="Whether we log recipient of signed document in proof", alias="bEzsignfoldertypeLogrecipientinproof")
    b_ezsignfoldertype_reassignezsignsigner: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signature is allowed by a signatory to another signatory or not", alias="bEzsignfoldertypeReassignezsignsigner")
    b_ezsignfoldertype_reassignuser: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signature is allowed by a user to a signatory or another user or not", alias="bEzsignfoldertypeReassignuser")
    b_ezsignfoldertype_reassigngroup: Optional[StrictBool] = Field(default=None, description="Wheter if Reassignment of signatures of the groups to which the user belongs is authorized by a user to himself", alias="bEzsignfoldertypeReassigngroup")
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
    e_ezsignfoldertype_signeraccess: Optional[FieldEEzsignfoldertypeSigneraccess] = Field(default=None, alias="eEzsignfoldertypeSigneraccess")
    b_ezsignfoldertype_isactive: StrictBool = Field(description="Whether the Ezsignfoldertype is active or not", alias="bEzsignfoldertypeIsactive")
    __properties: ClassVar[List[str]] = ["pkiEzsignfoldertypeID", "objEzsignfoldertypeName", "fkiBrandingID", "fkiBillingentityinternalID", "fkiEzsigntsarequirementID", "fkiFontIDAnnotation", "fkiFontIDFormfield", "fkiFontIDSignature", "fkiPdfalevelIDConvert", "a_fkiPdfalevelID", "a_fkiUserlogintypeID", "a_fkiUsergroupIDAll", "a_fkiUsergroupIDRestricted", "a_fkiUsergroupIDTemplate", "eEzsignfoldertypeDocumentdependency", "sEmailAddressSigned", "sEmailAddressSummary", "eEzsignfoldertypePdfarequirement", "eEzsignfoldertypePdfanoncompliantaction", "eEzsignfoldertypePrivacylevel", "iEzsignfoldertypeFontsizeannotation", "iEzsignfoldertypeFontsizeformfield", "iEzsignfoldertypeSendreminderfirstdays", "iEzsignfoldertypeSendreminderotherdays", "iEzsignfoldertypeArchivaldays", "eEzsignfoldertypeDisposal", "eEzsignfoldertypeCompletion", "iEzsignfoldertypeDisposaldays", "iEzsignfoldertypeDeadlinedays", "bEzsignfoldertypePrematurelyendautomatically", "iEzsignfoldertypePrematurelyendautomaticallydays", "bEzsignfoldertypeAutomaticsignature", "bEzsignfoldertypeDelegate", "bEzsignfoldertypeDiscussion", "bEzsignfoldertypeLogrecipientinproof", "bEzsignfoldertypeReassignezsignsigner", "bEzsignfoldertypeReassignuser", "bEzsignfoldertypeReassigngroup", "bEzsignfoldertypeSendsignedtoezsignsigner", "bEzsignfoldertypeSendsignedtouser", "bEzsignfoldertypeSendattachmentezsignsigner", "bEzsignfoldertypeSendproofezsignsigner", "bEzsignfoldertypeSendattachmentuser", "bEzsignfoldertypeSendproofuser", "bEzsignfoldertypeSendproofemail", "bEzsignfoldertypeAllowdownloadattachmentezsignsigner", "bEzsignfoldertypeAllowdownloadproofezsignsigner", "bEzsignfoldertypeSendproofreceivealldocument", "bEzsignfoldertypeSendsignedtodocumentowner", "bEzsignfoldertypeSendsignedtofolderowner", "bEzsignfoldertypeSendsignedtofullgroup", "bEzsignfoldertypeSendsignedtolimitedgroup", "bEzsignfoldertypeSendsignedtocolleague", "bEzsignfoldertypeSendsummarytodocumentowner", "bEzsignfoldertypeSendsummarytofolderowner", "bEzsignfoldertypeSendsummarytofullgroup", "bEzsignfoldertypeSendsummarytolimitedgroup", "bEzsignfoldertypeSendsummarytocolleague", "eEzsignfoldertypeSigneraccess", "bEzsignfoldertypeIsactive"]

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
        """Create an instance of EzsignfoldertypeRequestV3 from a JSON string"""
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
        """Create an instance of EzsignfoldertypeRequestV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfoldertypeID": obj.get("pkiEzsignfoldertypeID"),
            "objEzsignfoldertypeName": MultilingualEzsignfoldertypeName.from_dict(obj["objEzsignfoldertypeName"]) if obj.get("objEzsignfoldertypeName") is not None else None,
            "fkiBrandingID": obj.get("fkiBrandingID"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "fkiFontIDAnnotation": obj.get("fkiFontIDAnnotation"),
            "fkiFontIDFormfield": obj.get("fkiFontIDFormfield"),
            "fkiFontIDSignature": obj.get("fkiFontIDSignature"),
            "fkiPdfalevelIDConvert": obj.get("fkiPdfalevelIDConvert"),
            "a_fkiPdfalevelID": obj.get("a_fkiPdfalevelID"),
            "a_fkiUserlogintypeID": obj.get("a_fkiUserlogintypeID"),
            "a_fkiUsergroupIDAll": obj.get("a_fkiUsergroupIDAll"),
            "a_fkiUsergroupIDRestricted": obj.get("a_fkiUsergroupIDRestricted"),
            "a_fkiUsergroupIDTemplate": obj.get("a_fkiUsergroupIDTemplate"),
            "eEzsignfoldertypeDocumentdependency": obj.get("eEzsignfoldertypeDocumentdependency"),
            "sEmailAddressSigned": obj.get("sEmailAddressSigned"),
            "sEmailAddressSummary": obj.get("sEmailAddressSummary"),
            "eEzsignfoldertypePdfarequirement": obj.get("eEzsignfoldertypePdfarequirement"),
            "eEzsignfoldertypePdfanoncompliantaction": obj.get("eEzsignfoldertypePdfanoncompliantaction"),
            "eEzsignfoldertypePrivacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "iEzsignfoldertypeFontsizeannotation": obj.get("iEzsignfoldertypeFontsizeannotation"),
            "iEzsignfoldertypeFontsizeformfield": obj.get("iEzsignfoldertypeFontsizeformfield"),
            "iEzsignfoldertypeSendreminderfirstdays": obj.get("iEzsignfoldertypeSendreminderfirstdays"),
            "iEzsignfoldertypeSendreminderotherdays": obj.get("iEzsignfoldertypeSendreminderotherdays"),
            "iEzsignfoldertypeArchivaldays": obj.get("iEzsignfoldertypeArchivaldays"),
            "eEzsignfoldertypeDisposal": obj.get("eEzsignfoldertypeDisposal"),
            "eEzsignfoldertypeCompletion": obj.get("eEzsignfoldertypeCompletion"),
            "iEzsignfoldertypeDisposaldays": obj.get("iEzsignfoldertypeDisposaldays"),
            "iEzsignfoldertypeDeadlinedays": obj.get("iEzsignfoldertypeDeadlinedays"),
            "bEzsignfoldertypePrematurelyendautomatically": obj.get("bEzsignfoldertypePrematurelyendautomatically"),
            "iEzsignfoldertypePrematurelyendautomaticallydays": obj.get("iEzsignfoldertypePrematurelyendautomaticallydays"),
            "bEzsignfoldertypeAutomaticsignature": obj.get("bEzsignfoldertypeAutomaticsignature"),
            "bEzsignfoldertypeDelegate": obj.get("bEzsignfoldertypeDelegate"),
            "bEzsignfoldertypeDiscussion": obj.get("bEzsignfoldertypeDiscussion"),
            "bEzsignfoldertypeLogrecipientinproof": obj.get("bEzsignfoldertypeLogrecipientinproof"),
            "bEzsignfoldertypeReassignezsignsigner": obj.get("bEzsignfoldertypeReassignezsignsigner"),
            "bEzsignfoldertypeReassignuser": obj.get("bEzsignfoldertypeReassignuser"),
            "bEzsignfoldertypeReassigngroup": obj.get("bEzsignfoldertypeReassigngroup"),
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
            "eEzsignfoldertypeSigneraccess": obj.get("eEzsignfoldertypeSigneraccess"),
            "bEzsignfoldertypeIsactive": obj.get("bEzsignfoldertypeIsactive")
        })
        return _obj


