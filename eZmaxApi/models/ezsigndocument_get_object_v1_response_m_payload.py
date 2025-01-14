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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.computed_e_ezsigndocument_steptype import ComputedEEzsigndocumentSteptype
from eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response import CustomEzsignfoldersignerassociationstatusResponse
from eZmaxApi.models.ezsigndocumentdependency_response import EzsigndocumentdependencyResponse
from eZmaxApi.models.field_e_ezsigndocument_step import FieldEEzsigndocumentStep
from typing import Optional, Set
from typing_extensions import Self

class EzsigndocumentGetObjectV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}
    """ # noqa: E501
    pki_ezsigndocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigndocument", alias="pkiEzsigndocumentID")
    fki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="fkiEzsignfolderID")
    fki_ezsignfoldersignerassociation_id_declinedtosign: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldersignerassociation", alias="fkiEzsignfoldersignerassociationIDDeclinedtosign")
    dt_ezsigndocument_duedate: StrictStr = Field(description="The maximum date and time at which the Ezsigndocument can be signed.", alias="dtEzsigndocumentDuedate")
    dt_ezsignform_completed: Optional[StrictStr] = Field(default=None, description="The date and time at which the Ezsignform has been completed.", alias="dtEzsignformCompleted")
    fki_language_id: Optional[Annotated[int, Field(le=2, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_ezsigndocument_name: StrictStr = Field(description="The name of the document that will be presented to Ezsignfoldersignerassociations", alias="sEzsigndocumentName")
    e_ezsigndocument_step: FieldEEzsigndocumentStep = Field(alias="eEzsigndocumentStep")
    dt_ezsigndocument_firstsend: Optional[StrictStr] = Field(default=None, description="The date and time when the Ezsigndocument was first sent.", alias="dtEzsigndocumentFirstsend")
    dt_ezsigndocument_lastsend: Optional[StrictStr] = Field(default=None, description="The date and time when the Ezsigndocument was sent the last time.", alias="dtEzsigndocumentLastsend")
    i_ezsigndocument_order: Annotated[int, Field(strict=True, ge=1)] = Field(description="The order in which the Ezsigndocument will be presented to the signatory in the Ezsignfolder.", alias="iEzsigndocumentOrder")
    i_ezsigndocument_pagetotal: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of pages in the Ezsigndocument.", alias="iEzsigndocumentPagetotal")
    i_ezsigndocument_signaturesigned: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of signatures that were signed in the document.", alias="iEzsigndocumentSignaturesigned")
    i_ezsigndocument_signaturetotal: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of total signatures that were requested in the Ezsigndocument.", alias="iEzsigndocumentSignaturetotal")
    i_ezsigndocument_formfieldtotal: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of total Ezsignformfield that were requested in the Ezsigndocument.", alias="iEzsigndocumentFormfieldtotal")
    s_ezsigndocument_md5initial: Optional[StrictStr] = Field(default=None, description="MD5 Hash of the initial PDF Document before signatures were applied to it.", alias="sEzsigndocumentMD5initial")
    t_ezsigndocument_declinedtosignreason: Optional[StrictStr] = Field(default=None, description="A custom text message that will contain the refusal message if the Ezsigndocument is declined to sign", alias="tEzsigndocumentDeclinedtosignreason")
    s_ezsigndocument_md5signed: Optional[StrictStr] = Field(default=None, description="MD5 Hash of the final PDF Document after all signatures were applied to it.", alias="sEzsigndocumentMD5signed")
    b_ezsigndocument_ezsignform: Optional[StrictBool] = Field(default=None, description="If the Ezsigndocument contains an Ezsignform or not", alias="bEzsigndocumentEzsignform")
    b_ezsigndocument_hassignedsignatures: Optional[StrictBool] = Field(default=None, description="If the Ezsigndocument contains signed signatures (From internal or external sources)", alias="bEzsigndocumentHassignedsignatures")
    obj_audit: Optional[CommonAudit] = Field(default=None, alias="objAudit")
    s_ezsigndocument_externalid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This field can be used to store an External ID from the client's system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format. ", alias="sEzsigndocumentExternalid")
    i_ezsigndocument_ezsignsignatureattachmenttotal: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of Ezsigndocumentattachment total", alias="iEzsigndocumentEzsignsignatureattachmenttotal")
    i_ezsigndocument_ezsigndiscussiontotal: StrictInt = Field(description="The total number of Ezsigndiscussions", alias="iEzsigndocumentEzsigndiscussiontotal")
    e_ezsigndocument_steptype: ComputedEEzsigndocumentSteptype = Field(alias="eEzsigndocumentSteptype")
    i_ezsigndocument_stepformtotal: StrictInt = Field(description="The total number of steps in the form filling phase", alias="iEzsigndocumentStepformtotal")
    i_ezsigndocument_stepformcurrent: StrictInt = Field(description="The current step in the form filling phase", alias="iEzsigndocumentStepformcurrent")
    i_ezsigndocument_stepsignaturetotal: StrictInt = Field(description="The total number of steps in the signature filling phase", alias="iEzsigndocumentStepsignaturetotal")
    i_ezsigndocument_stepsignature_current: StrictInt = Field(description="The current step in the signature phase", alias="iEzsigndocumentStepsignatureCurrent")
    a_obj_ezsignfoldersignerassociationstatus: List[CustomEzsignfoldersignerassociationstatusResponse] = Field(alias="a_objEzsignfoldersignerassociationstatus")
    a_obj_ezsigndocumentdependency: Optional[List[EzsigndocumentdependencyResponse]] = Field(default=None, alias="a_objEzsigndocumentdependency")
    __properties: ClassVar[List[str]] = ["pkiEzsigndocumentID", "fkiEzsignfolderID", "fkiEzsignfoldersignerassociationIDDeclinedtosign", "dtEzsigndocumentDuedate", "dtEzsignformCompleted", "fkiLanguageID", "sEzsigndocumentName", "eEzsigndocumentStep", "dtEzsigndocumentFirstsend", "dtEzsigndocumentLastsend", "iEzsigndocumentOrder", "iEzsigndocumentPagetotal", "iEzsigndocumentSignaturesigned", "iEzsigndocumentSignaturetotal", "iEzsigndocumentFormfieldtotal", "sEzsigndocumentMD5initial", "tEzsigndocumentDeclinedtosignreason", "sEzsigndocumentMD5signed", "bEzsigndocumentEzsignform", "bEzsigndocumentHassignedsignatures", "objAudit", "sEzsigndocumentExternalid", "iEzsigndocumentEzsignsignatureattachmenttotal", "iEzsigndocumentEzsigndiscussiontotal", "eEzsigndocumentSteptype", "iEzsigndocumentStepformtotal", "iEzsigndocumentStepformcurrent", "iEzsigndocumentStepsignaturetotal", "iEzsigndocumentStepsignatureCurrent", "a_objEzsignfoldersignerassociationstatus", "a_objEzsigndocumentdependency"]

    @field_validator('s_ezsigndocument_externalid')
    def s_ezsigndocument_externalid_validate_regular_expression(cls, value):
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
        """Create an instance of EzsigndocumentGetObjectV1ResponseMPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignfoldersignerassociationstatus (list)
        _items = []
        if self.a_obj_ezsignfoldersignerassociationstatus:
            for _item_a_obj_ezsignfoldersignerassociationstatus in self.a_obj_ezsignfoldersignerassociationstatus:
                if _item_a_obj_ezsignfoldersignerassociationstatus:
                    _items.append(_item_a_obj_ezsignfoldersignerassociationstatus.to_dict())
            _dict['a_objEzsignfoldersignerassociationstatus'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigndocumentdependency (list)
        _items = []
        if self.a_obj_ezsigndocumentdependency:
            for _item_a_obj_ezsigndocumentdependency in self.a_obj_ezsigndocumentdependency:
                if _item_a_obj_ezsigndocumentdependency:
                    _items.append(_item_a_obj_ezsigndocumentdependency.to_dict())
            _dict['a_objEzsigndocumentdependency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigndocumentGetObjectV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigndocumentID": obj.get("pkiEzsigndocumentID"),
            "fkiEzsignfolderID": obj.get("fkiEzsignfolderID"),
            "fkiEzsignfoldersignerassociationIDDeclinedtosign": obj.get("fkiEzsignfoldersignerassociationIDDeclinedtosign"),
            "dtEzsigndocumentDuedate": obj.get("dtEzsigndocumentDuedate"),
            "dtEzsignformCompleted": obj.get("dtEzsignformCompleted"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sEzsigndocumentName": obj.get("sEzsigndocumentName"),
            "eEzsigndocumentStep": obj.get("eEzsigndocumentStep"),
            "dtEzsigndocumentFirstsend": obj.get("dtEzsigndocumentFirstsend"),
            "dtEzsigndocumentLastsend": obj.get("dtEzsigndocumentLastsend"),
            "iEzsigndocumentOrder": obj.get("iEzsigndocumentOrder"),
            "iEzsigndocumentPagetotal": obj.get("iEzsigndocumentPagetotal"),
            "iEzsigndocumentSignaturesigned": obj.get("iEzsigndocumentSignaturesigned"),
            "iEzsigndocumentSignaturetotal": obj.get("iEzsigndocumentSignaturetotal"),
            "iEzsigndocumentFormfieldtotal": obj.get("iEzsigndocumentFormfieldtotal"),
            "sEzsigndocumentMD5initial": obj.get("sEzsigndocumentMD5initial"),
            "tEzsigndocumentDeclinedtosignreason": obj.get("tEzsigndocumentDeclinedtosignreason"),
            "sEzsigndocumentMD5signed": obj.get("sEzsigndocumentMD5signed"),
            "bEzsigndocumentEzsignform": obj.get("bEzsigndocumentEzsignform"),
            "bEzsigndocumentHassignedsignatures": obj.get("bEzsigndocumentHassignedsignatures"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "sEzsigndocumentExternalid": obj.get("sEzsigndocumentExternalid"),
            "iEzsigndocumentEzsignsignatureattachmenttotal": obj.get("iEzsigndocumentEzsignsignatureattachmenttotal"),
            "iEzsigndocumentEzsigndiscussiontotal": obj.get("iEzsigndocumentEzsigndiscussiontotal"),
            "eEzsigndocumentSteptype": obj.get("eEzsigndocumentSteptype"),
            "iEzsigndocumentStepformtotal": obj.get("iEzsigndocumentStepformtotal"),
            "iEzsigndocumentStepformcurrent": obj.get("iEzsigndocumentStepformcurrent"),
            "iEzsigndocumentStepsignaturetotal": obj.get("iEzsigndocumentStepsignaturetotal"),
            "iEzsigndocumentStepsignatureCurrent": obj.get("iEzsigndocumentStepsignatureCurrent"),
            "a_objEzsignfoldersignerassociationstatus": [CustomEzsignfoldersignerassociationstatusResponse.from_dict(_item) for _item in obj["a_objEzsignfoldersignerassociationstatus"]] if obj.get("a_objEzsignfoldersignerassociationstatus") is not None else None,
            "a_objEzsigndocumentdependency": [EzsigndocumentdependencyResponse.from_dict(_item) for _item in obj["a_objEzsigndocumentdependency"]] if obj.get("a_objEzsigndocumentdependency") is not None else None
        })
        return _obj


