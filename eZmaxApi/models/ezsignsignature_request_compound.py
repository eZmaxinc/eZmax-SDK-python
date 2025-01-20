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
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.ezsignelementdependency_request import EzsignelementdependencyRequest
from eZmaxApi.models.ezsignsignaturecustomdate_request import EzsignsignaturecustomdateRequest
from eZmaxApi.models.field_e_ezsignsignature_attachmentnamesource import FieldEEzsignsignatureAttachmentnamesource
from eZmaxApi.models.field_e_ezsignsignature_consultationtrigger import FieldEEzsignsignatureConsultationtrigger
from eZmaxApi.models.field_e_ezsignsignature_dependencyrequirement import FieldEEzsignsignatureDependencyrequirement
from eZmaxApi.models.field_e_ezsignsignature_font import FieldEEzsignsignatureFont
from eZmaxApi.models.field_e_ezsignsignature_tooltipposition import FieldEEzsignsignatureTooltipposition
from eZmaxApi.models.field_e_ezsignsignature_type import FieldEEzsignsignatureType
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignatureRequestCompound(BaseModel):
    """
    An Ezsignsignature Object and children to create a complete structure
    """ # noqa: E501
    pki_ezsignsignature_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignsignature", alias="pkiEzsignsignatureID")
    fki_ezsignfoldersignerassociation_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldersignerassociation", alias="fkiEzsignfoldersignerassociationID")
    i_ezsignpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigndocument", alias="iEzsignpagePagenumber")
    i_ezsignsignature_x: Annotated[int, Field(strict=True, ge=0)] = Field(description="The X coordinate (Horizontal) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsignsignatureX")
    i_ezsignsignature_y: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Y coordinate (Vertical) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsignsignatureY")
    i_ezsignsignature_width: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The width of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have a width of 2 inches, you would use \"200\" for the iEzsignsignatureWidth.", alias="iEzsignsignatureWidth")
    i_ezsignsignature_height: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The height of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have an height of 2 inches, you would use \"200\" for the iEzsignsignatureHeight.", alias="iEzsignsignatureHeight")
    i_ezsignsignature_step: StrictInt = Field(description="The step when the Ezsignsigner will be invited to sign", alias="iEzsignsignatureStep")
    e_ezsignsignature_type: FieldEEzsignsignatureType = Field(alias="eEzsignsignatureType")
    fki_ezsigndocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentID")
    t_ezsignsignature_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsignsigner about the Ezsignsignature", alias="tEzsignsignatureTooltip")
    e_ezsignsignature_tooltipposition: Optional[FieldEEzsignsignatureTooltipposition] = Field(default=None, alias="eEzsignsignatureTooltipposition")
    e_ezsignsignature_font: Optional[FieldEEzsignsignatureFont] = Field(default=None, alias="eEzsignsignatureFont")
    fki_ezsignfoldersignerassociation_id_validation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldersignerassociation", alias="fkiEzsignfoldersignerassociationIDValidation")
    b_ezsignsignature_handwritten: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature must be handwritten or not when eEzsignsignatureType = Signature.", alias="bEzsignsignatureHandwritten")
    b_ezsignsignature_reason: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature must include a reason or not when eEzsignsignatureType = Signature.", alias="bEzsignsignatureReason")
    b_ezsignsignature_required: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature is required or not. This field is relevant only with Ezsignsignature with eEzsignsignatureType = Attachments, Text or Textarea.", alias="bEzsignsignatureRequired")
    e_ezsignsignature_attachmentnamesource: Optional[FieldEEzsignsignatureAttachmentnamesource] = Field(default=None, alias="eEzsignsignatureAttachmentnamesource")
    s_ezsignsignature_attachmentdescription: Optional[StrictStr] = Field(default=None, description="The description attached to the attachment name added in Ezsignsignature of eEzsignsignatureType Attachments", alias="sEzsignsignatureAttachmentdescription")
    e_ezsignsignature_consultationtrigger: Optional[FieldEEzsignsignatureConsultationtrigger] = Field(default=None, alias="eEzsignsignatureConsultationtrigger")
    i_ezsignsignature_validationstep: Optional[StrictInt] = Field(default=None, description="The step when the Ezsignsigner will be invited to validate the Ezsignsignature of eEzsignsignatureType Attachments", alias="iEzsignsignatureValidationstep")
    i_ezsignsignature_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsignsignature  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea**", alias="iEzsignsignatureMaxlength")
    s_ezsignsignature_defaultvalue: Optional[StrictStr] = Field(default=None, description="The default value for the Ezsignsignature  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sCompany} | Company name | eZmax Solutions Inc. | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 |", alias="sEzsignsignatureDefaultvalue")
    e_ezsignsignature_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsignsignatureTextvalidation")
    s_ezsignsignature_textvalidationcustommessage: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Description of validation rule. Show by signatory.", alias="sEzsignsignatureTextvalidationcustommessage")
    s_ezsignsignature_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea** and eEzsignsignatureTextvalidation is **Custom**", alias="sEzsignsignatureRegexp")
    e_ezsignsignature_dependencyrequirement: Optional[FieldEEzsignsignatureDependencyrequirement] = Field(default=None, alias="eEzsignsignatureDependencyrequirement")
    b_ezsignsignature_customdate: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**)", alias="bEzsignsignatureCustomdate")
    a_obj_ezsignsignaturecustomdate: Optional[List[EzsignsignaturecustomdateRequest]] = Field(default=None, description="An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.", alias="a_objEzsignsignaturecustomdate")
    a_obj_ezsignelementdependency: Optional[List[EzsignelementdependencyRequest]] = Field(default=None, alias="a_objEzsignelementdependency")
    __properties: ClassVar[List[str]] = ["pkiEzsignsignatureID", "fkiEzsignfoldersignerassociationID", "iEzsignpagePagenumber", "iEzsignsignatureX", "iEzsignsignatureY", "iEzsignsignatureWidth", "iEzsignsignatureHeight", "iEzsignsignatureStep", "eEzsignsignatureType", "fkiEzsigndocumentID", "tEzsignsignatureTooltip", "eEzsignsignatureTooltipposition", "eEzsignsignatureFont", "fkiEzsignfoldersignerassociationIDValidation", "bEzsignsignatureHandwritten", "bEzsignsignatureReason", "bEzsignsignatureRequired", "eEzsignsignatureAttachmentnamesource", "sEzsignsignatureAttachmentdescription", "eEzsignsignatureConsultationtrigger", "iEzsignsignatureValidationstep", "iEzsignsignatureMaxlength", "sEzsignsignatureDefaultvalue", "eEzsignsignatureTextvalidation", "sEzsignsignatureTextvalidationcustommessage", "sEzsignsignatureRegexp", "eEzsignsignatureDependencyrequirement", "bEzsignsignatureCustomdate", "a_objEzsignsignaturecustomdate", "a_objEzsignelementdependency"]

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
        """Create an instance of EzsignsignatureRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignsignaturecustomdate (list)
        _items = []
        if self.a_obj_ezsignsignaturecustomdate:
            for _item_a_obj_ezsignsignaturecustomdate in self.a_obj_ezsignsignaturecustomdate:
                if _item_a_obj_ezsignsignaturecustomdate:
                    _items.append(_item_a_obj_ezsignsignaturecustomdate.to_dict())
            _dict['a_objEzsignsignaturecustomdate'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignelementdependency (list)
        _items = []
        if self.a_obj_ezsignelementdependency:
            for _item_a_obj_ezsignelementdependency in self.a_obj_ezsignelementdependency:
                if _item_a_obj_ezsignelementdependency:
                    _items.append(_item_a_obj_ezsignelementdependency.to_dict())
            _dict['a_objEzsignelementdependency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignatureRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignsignatureID": obj.get("pkiEzsignsignatureID"),
            "fkiEzsignfoldersignerassociationID": obj.get("fkiEzsignfoldersignerassociationID"),
            "iEzsignpagePagenumber": obj.get("iEzsignpagePagenumber"),
            "iEzsignsignatureX": obj.get("iEzsignsignatureX"),
            "iEzsignsignatureY": obj.get("iEzsignsignatureY"),
            "iEzsignsignatureWidth": obj.get("iEzsignsignatureWidth"),
            "iEzsignsignatureHeight": obj.get("iEzsignsignatureHeight"),
            "iEzsignsignatureStep": obj.get("iEzsignsignatureStep"),
            "eEzsignsignatureType": obj.get("eEzsignsignatureType"),
            "fkiEzsigndocumentID": obj.get("fkiEzsigndocumentID"),
            "tEzsignsignatureTooltip": obj.get("tEzsignsignatureTooltip"),
            "eEzsignsignatureTooltipposition": obj.get("eEzsignsignatureTooltipposition"),
            "eEzsignsignatureFont": obj.get("eEzsignsignatureFont"),
            "fkiEzsignfoldersignerassociationIDValidation": obj.get("fkiEzsignfoldersignerassociationIDValidation"),
            "bEzsignsignatureHandwritten": obj.get("bEzsignsignatureHandwritten"),
            "bEzsignsignatureReason": obj.get("bEzsignsignatureReason"),
            "bEzsignsignatureRequired": obj.get("bEzsignsignatureRequired"),
            "eEzsignsignatureAttachmentnamesource": obj.get("eEzsignsignatureAttachmentnamesource"),
            "sEzsignsignatureAttachmentdescription": obj.get("sEzsignsignatureAttachmentdescription"),
            "eEzsignsignatureConsultationtrigger": obj.get("eEzsignsignatureConsultationtrigger"),
            "iEzsignsignatureValidationstep": obj.get("iEzsignsignatureValidationstep"),
            "iEzsignsignatureMaxlength": obj.get("iEzsignsignatureMaxlength"),
            "sEzsignsignatureDefaultvalue": obj.get("sEzsignsignatureDefaultvalue"),
            "eEzsignsignatureTextvalidation": obj.get("eEzsignsignatureTextvalidation"),
            "sEzsignsignatureTextvalidationcustommessage": obj.get("sEzsignsignatureTextvalidationcustommessage"),
            "sEzsignsignatureRegexp": obj.get("sEzsignsignatureRegexp"),
            "eEzsignsignatureDependencyrequirement": obj.get("eEzsignsignatureDependencyrequirement"),
            "bEzsignsignatureCustomdate": obj.get("bEzsignsignatureCustomdate"),
            "a_objEzsignsignaturecustomdate": [EzsignsignaturecustomdateRequest.from_dict(_item) for _item in obj["a_objEzsignsignaturecustomdate"]] if obj.get("a_objEzsignsignaturecustomdate") is not None else None,
            "a_objEzsignelementdependency": [EzsignelementdependencyRequest.from_dict(_item) for _item in obj["a_objEzsignelementdependency"]] if obj.get("a_objEzsignelementdependency") is not None else None
        })
        return _obj


