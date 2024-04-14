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
from eZmaxApi.models.custom_contact_name_response import CustomContactNameResponse
from eZmaxApi.models.custom_creditcardtransaction_response import CustomCreditcardtransactionResponse
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.ezsignelementdependency_response_compound import EzsignelementdependencyResponseCompound
from eZmaxApi.models.ezsignsignaturecustomdate_response_compound import EzsignsignaturecustomdateResponseCompound
from eZmaxApi.models.field_e_ezsignsignature_attachmentnamesource import FieldEEzsignsignatureAttachmentnamesource
from eZmaxApi.models.field_e_ezsignsignature_dependencyrequirement import FieldEEzsignsignatureDependencyrequirement
from eZmaxApi.models.field_e_ezsignsignature_font import FieldEEzsignsignatureFont
from eZmaxApi.models.field_e_ezsignsignature_tooltipposition import FieldEEzsignsignatureTooltipposition
from eZmaxApi.models.field_e_ezsignsignature_type import FieldEEzsignsignatureType
from eZmaxApi.models.signature_response_compound import SignatureResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignatureResponseCompound(BaseModel):
    """
    An Ezsignsignature Object and children to create a complete structure
    """ # noqa: E501
    pki_ezsignsignature_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignsignature", alias="pkiEzsignsignatureID")
    fki_ezsigndocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentID")
    fki_ezsignfoldersignerassociation_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldersignerassociation", alias="fkiEzsignfoldersignerassociationID")
    fki_ezsignsigningreason_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignsigningreason", alias="fkiEzsignsigningreasonID")
    s_ezsignsigningreason_description_x: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The description of the Ezsignsigningreason in the language of the requester", alias="sEzsignsigningreasonDescriptionX")
    i_ezsignpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigndocument", alias="iEzsignpagePagenumber")
    i_ezsignsignature_x: Annotated[int, Field(strict=True, ge=0)] = Field(description="The X coordinate (Horizontal) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsignsignatureX")
    i_ezsignsignature_y: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Y coordinate (Vertical) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsignsignatureY")
    i_ezsignsignature_height: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The height of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have an height of 2 inches, you would use \"200\" for the iEzsignsignatureHeight.", alias="iEzsignsignatureHeight")
    i_ezsignsignature_width: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The width of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have a width of 2 inches, you would use \"200\" for the iEzsignsignatureWidth.", alias="iEzsignsignatureWidth")
    i_ezsignsignature_step: StrictInt = Field(description="The step when the Ezsignsigner will be invited to sign", alias="iEzsignsignatureStep")
    i_ezsignsignature_stepadjusted: Optional[StrictInt] = Field(default=None, description="The step when the Ezsignsigner will be invited to sign", alias="iEzsignsignatureStepadjusted")
    e_ezsignsignature_type: FieldEEzsignsignatureType = Field(alias="eEzsignsignatureType")
    t_ezsignsignature_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsignsigner about the Ezsignsignature", alias="tEzsignsignatureTooltip")
    e_ezsignsignature_tooltipposition: Optional[FieldEEzsignsignatureTooltipposition] = Field(default=None, alias="eEzsignsignatureTooltipposition")
    e_ezsignsignature_font: Optional[FieldEEzsignsignatureFont] = Field(default=None, alias="eEzsignsignatureFont")
    i_ezsignsignature_validationstep: Optional[StrictInt] = Field(default=None, description="The step when the Ezsignsigner will be invited to validate the Ezsignsignature of eEzsignsignatureType Attachments", alias="iEzsignsignatureValidationstep")
    s_ezsignsignature_attachmentdescription: Optional[StrictStr] = Field(default=None, description="The description attached to the attachment name added in Ezsignsignature of eEzsignsignatureType Attachments", alias="sEzsignsignatureAttachmentdescription")
    e_ezsignsignature_attachmentnamesource: Optional[FieldEEzsignsignatureAttachmentnamesource] = Field(default=None, alias="eEzsignsignatureAttachmentnamesource")
    b_ezsignsignature_required: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature is required or not. This field is relevant only with Ezsignsignature with eEzsignsignatureType = Attachments.", alias="bEzsignsignatureRequired")
    fki_ezsignfoldersignerassociation_id_validation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldersignerassociation", alias="fkiEzsignfoldersignerassociationIDValidation")
    dt_ezsignsignature_date: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The date the Ezsignsignature was signed", alias="dtEzsignsignatureDate")
    i_ezsignsignatureattachment_count: Optional[StrictInt] = Field(default=None, description="The count of Ezsignsignatureattachment", alias="iEzsignsignatureattachmentCount")
    s_ezsignsignature_description: Optional[StrictStr] = Field(default=None, description="The value entered while signing Ezsignsignature of eEzsignsignatureType **City**, **FieldText** and **FieldTextarea**", alias="sEzsignsignatureDescription")
    i_ezsignsignature_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsignsignature  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea**", alias="iEzsignsignatureMaxlength")
    e_ezsignsignature_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsignsignatureTextvalidation")
    e_ezsignsignature_dependencyrequirement: Optional[FieldEEzsignsignatureDependencyrequirement] = Field(default=None, alias="eEzsignsignatureDependencyrequirement")
    s_ezsignsignature_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea** and eEzsignsignatureTextvalidation is **Custom**", alias="sEzsignsignatureRegexp")
    obj_contact_name: CustomContactNameResponse = Field(alias="objContactName")
    obj_contact_name_delegation: Optional[CustomContactNameResponse] = Field(default=None, alias="objContactNameDelegation")
    obj_signature: Optional[SignatureResponseCompound] = Field(default=None, alias="objSignature")
    b_ezsignsignature_customdate: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**)", alias="bEzsignsignatureCustomdate")
    a_obj_ezsignsignaturecustomdate: Optional[List[EzsignsignaturecustomdateResponseCompound]] = Field(default=None, description="An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.", alias="a_objEzsignsignaturecustomdate")
    obj_creditcardtransaction: Optional[CustomCreditcardtransactionResponse] = Field(default=None, alias="objCreditcardtransaction")
    a_obj_ezsignelementdependency: Optional[List[EzsignelementdependencyResponseCompound]] = Field(default=None, alias="a_objEzsignelementdependency")
    __properties: ClassVar[List[str]] = ["pkiEzsignsignatureID", "fkiEzsigndocumentID", "fkiEzsignfoldersignerassociationID", "fkiEzsignsigningreasonID", "sEzsignsigningreasonDescriptionX", "iEzsignpagePagenumber", "iEzsignsignatureX", "iEzsignsignatureY", "iEzsignsignatureHeight", "iEzsignsignatureWidth", "iEzsignsignatureStep", "iEzsignsignatureStepadjusted", "eEzsignsignatureType", "tEzsignsignatureTooltip", "eEzsignsignatureTooltipposition", "eEzsignsignatureFont", "iEzsignsignatureValidationstep", "sEzsignsignatureAttachmentdescription", "eEzsignsignatureAttachmentnamesource", "bEzsignsignatureRequired", "fkiEzsignfoldersignerassociationIDValidation", "dtEzsignsignatureDate", "iEzsignsignatureattachmentCount", "sEzsignsignatureDescription", "iEzsignsignatureMaxlength", "eEzsignsignatureTextvalidation", "eEzsignsignatureDependencyrequirement", "sEzsignsignatureRegexp", "objContactName", "objContactNameDelegation", "objSignature", "bEzsignsignatureCustomdate", "a_objEzsignsignaturecustomdate", "objCreditcardtransaction", "a_objEzsignelementdependency"]

    @field_validator('s_ezsignsigningreason_description_x')
    def s_ezsignsigningreason_description_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('dt_ezsignsignature_date')
    def dt_ezsignsignature_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('s_ezsignsignature_regexp')
    def s_ezsignsignature_regexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\^.*\$$|^$", value):
            raise ValueError(r"must validate the regular expression /^\^.*\$$|^$/")
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
        """Create an instance of EzsignsignatureResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_contact_name
        if self.obj_contact_name:
            _dict['objContactName'] = self.obj_contact_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_contact_name_delegation
        if self.obj_contact_name_delegation:
            _dict['objContactNameDelegation'] = self.obj_contact_name_delegation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_signature
        if self.obj_signature:
            _dict['objSignature'] = self.obj_signature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignsignaturecustomdate (list)
        _items = []
        if self.a_obj_ezsignsignaturecustomdate:
            for _item in self.a_obj_ezsignsignaturecustomdate:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignsignaturecustomdate'] = _items
        # override the default output from pydantic by calling `to_dict()` of obj_creditcardtransaction
        if self.obj_creditcardtransaction:
            _dict['objCreditcardtransaction'] = self.obj_creditcardtransaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignelementdependency (list)
        _items = []
        if self.a_obj_ezsignelementdependency:
            for _item in self.a_obj_ezsignelementdependency:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignelementdependency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignatureResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignsignatureID": obj.get("pkiEzsignsignatureID"),
            "fkiEzsigndocumentID": obj.get("fkiEzsigndocumentID"),
            "fkiEzsignfoldersignerassociationID": obj.get("fkiEzsignfoldersignerassociationID"),
            "fkiEzsignsigningreasonID": obj.get("fkiEzsignsigningreasonID"),
            "sEzsignsigningreasonDescriptionX": obj.get("sEzsignsigningreasonDescriptionX"),
            "iEzsignpagePagenumber": obj.get("iEzsignpagePagenumber"),
            "iEzsignsignatureX": obj.get("iEzsignsignatureX"),
            "iEzsignsignatureY": obj.get("iEzsignsignatureY"),
            "iEzsignsignatureHeight": obj.get("iEzsignsignatureHeight"),
            "iEzsignsignatureWidth": obj.get("iEzsignsignatureWidth"),
            "iEzsignsignatureStep": obj.get("iEzsignsignatureStep"),
            "iEzsignsignatureStepadjusted": obj.get("iEzsignsignatureStepadjusted"),
            "eEzsignsignatureType": obj.get("eEzsignsignatureType"),
            "tEzsignsignatureTooltip": obj.get("tEzsignsignatureTooltip"),
            "eEzsignsignatureTooltipposition": obj.get("eEzsignsignatureTooltipposition"),
            "eEzsignsignatureFont": obj.get("eEzsignsignatureFont"),
            "iEzsignsignatureValidationstep": obj.get("iEzsignsignatureValidationstep"),
            "sEzsignsignatureAttachmentdescription": obj.get("sEzsignsignatureAttachmentdescription"),
            "eEzsignsignatureAttachmentnamesource": obj.get("eEzsignsignatureAttachmentnamesource"),
            "bEzsignsignatureRequired": obj.get("bEzsignsignatureRequired"),
            "fkiEzsignfoldersignerassociationIDValidation": obj.get("fkiEzsignfoldersignerassociationIDValidation"),
            "dtEzsignsignatureDate": obj.get("dtEzsignsignatureDate"),
            "iEzsignsignatureattachmentCount": obj.get("iEzsignsignatureattachmentCount"),
            "sEzsignsignatureDescription": obj.get("sEzsignsignatureDescription"),
            "iEzsignsignatureMaxlength": obj.get("iEzsignsignatureMaxlength"),
            "eEzsignsignatureTextvalidation": obj.get("eEzsignsignatureTextvalidation"),
            "eEzsignsignatureDependencyrequirement": obj.get("eEzsignsignatureDependencyrequirement"),
            "sEzsignsignatureRegexp": obj.get("sEzsignsignatureRegexp"),
            "objContactName": CustomContactNameResponse.from_dict(obj["objContactName"]) if obj.get("objContactName") is not None else None,
            "objContactNameDelegation": CustomContactNameResponse.from_dict(obj["objContactNameDelegation"]) if obj.get("objContactNameDelegation") is not None else None,
            "objSignature": SignatureResponseCompound.from_dict(obj["objSignature"]) if obj.get("objSignature") is not None else None,
            "bEzsignsignatureCustomdate": obj.get("bEzsignsignatureCustomdate"),
            "a_objEzsignsignaturecustomdate": [EzsignsignaturecustomdateResponseCompound.from_dict(_item) for _item in obj["a_objEzsignsignaturecustomdate"]] if obj.get("a_objEzsignsignaturecustomdate") is not None else None,
            "objCreditcardtransaction": CustomCreditcardtransactionResponse.from_dict(obj["objCreditcardtransaction"]) if obj.get("objCreditcardtransaction") is not None else None,
            "a_objEzsignelementdependency": [EzsignelementdependencyResponseCompound.from_dict(_item) for _item in obj["a_objEzsignelementdependency"]] if obj.get("a_objEzsignelementdependency") is not None else None
        })
        return _obj


