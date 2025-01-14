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
from eZmaxApi.models.ezsigntemplateelementdependency_request_compound import EzsigntemplateelementdependencyRequestCompound
from eZmaxApi.models.ezsigntemplatesignaturecustomdate_request_compound_v2 import EzsigntemplatesignaturecustomdateRequestCompoundV2
from eZmaxApi.models.field_e_ezsigntemplatesignature_attachmentnamesource import FieldEEzsigntemplatesignatureAttachmentnamesource
from eZmaxApi.models.field_e_ezsigntemplatesignature_consultationtrigger import FieldEEzsigntemplatesignatureConsultationtrigger
from eZmaxApi.models.field_e_ezsigntemplatesignature_dependencyrequirement import FieldEEzsigntemplatesignatureDependencyrequirement
from eZmaxApi.models.field_e_ezsigntemplatesignature_font import FieldEEzsigntemplatesignatureFont
from eZmaxApi.models.field_e_ezsigntemplatesignature_positioning import FieldEEzsigntemplatesignaturePositioning
from eZmaxApi.models.field_e_ezsigntemplatesignature_positioningoccurence import FieldEEzsigntemplatesignaturePositioningoccurence
from eZmaxApi.models.field_e_ezsigntemplatesignature_tooltipposition import FieldEEzsigntemplatesignatureTooltipposition
from eZmaxApi.models.field_e_ezsigntemplatesignature_type import FieldEEzsigntemplatesignatureType
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatesignatureRequestCompoundV2(BaseModel):
    """
    A Ezsigntemplatesignature Object and children
    """ # noqa: E501
    pki_ezsigntemplatesignature_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatesignature", alias="pkiEzsigntemplatesignatureID")
    fki_ezsigntemplatedocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocument", alias="fkiEzsigntemplatedocumentID")
    fki_ezsigntemplatesigner_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatesigner", alias="fkiEzsigntemplatesignerID")
    fki_ezsigntemplatesigner_id_validation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatesigner", alias="fkiEzsigntemplatesignerIDValidation")
    b_ezsigntemplatesignature_handwritten: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplatesignature must be handwritten or not when eEzsigntemplatesignatureType = Signature.", alias="bEzsigntemplatesignatureHandwritten")
    b_ezsigntemplatesignature_reason: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplatesignature must include a reason or not when eEzsigntemplatesignatureType = Signature.", alias="bEzsigntemplatesignatureReason")
    e_ezsigntemplatesignature_positioning: Optional[FieldEEzsigntemplatesignaturePositioning] = Field(default=None, alias="eEzsigntemplatesignaturePositioning")
    i_ezsigntemplatedocumentpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigntemplatedocument", alias="iEzsigntemplatedocumentpagePagenumber")
    i_ezsigntemplatesignature_x: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The X coordinate (Horizontal) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsigntemplatesignatureX")
    i_ezsigntemplatesignature_y: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The Y coordinate (Vertical) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsigntemplatesignatureY")
    i_ezsigntemplatesignature_width: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The width of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have a width of 2 inches, you would use \"200\" for the iEzsigntemplatesignatureWidth.", alias="iEzsigntemplatesignatureWidth")
    i_ezsigntemplatesignature_height: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The height of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have an height of 2 inches, you would use \"200\" for the iEzsigntemplatesignatureHeight.", alias="iEzsigntemplatesignatureHeight")
    i_ezsigntemplatesignature_step: Annotated[int, Field(strict=True, ge=1)] = Field(description="The step when the Ezsigntemplatesigner will be invited to sign", alias="iEzsigntemplatesignatureStep")
    e_ezsigntemplatesignature_type: FieldEEzsigntemplatesignatureType = Field(alias="eEzsigntemplatesignatureType")
    e_ezsigntemplatesignature_consultationtrigger: Optional[FieldEEzsigntemplatesignatureConsultationtrigger] = Field(default=None, alias="eEzsigntemplatesignatureConsultationtrigger")
    t_ezsigntemplatesignature_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature", alias="tEzsigntemplatesignatureTooltip")
    e_ezsigntemplatesignature_tooltipposition: Optional[FieldEEzsigntemplatesignatureTooltipposition] = Field(default=None, alias="eEzsigntemplatesignatureTooltipposition")
    e_ezsigntemplatesignature_font: Optional[FieldEEzsigntemplatesignatureFont] = Field(default=None, alias="eEzsigntemplatesignatureFont")
    b_ezsigntemplatesignature_required: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplatesignature is required or not. This field is relevant only with Ezsigntemplatesignature with eEzsigntemplatesignatureType = Attachments.", alias="bEzsigntemplatesignatureRequired")
    e_ezsigntemplatesignature_attachmentnamesource: Optional[FieldEEzsigntemplatesignatureAttachmentnamesource] = Field(default=None, alias="eEzsigntemplatesignatureAttachmentnamesource")
    s_ezsigntemplatesignature_attachmentdescription: Optional[StrictStr] = Field(default=None, description="The description attached to the attachment name added in Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments", alias="sEzsigntemplatesignatureAttachmentdescription")
    i_ezsigntemplatesignature_validationstep: Optional[StrictInt] = Field(default=None, description="The step when the Ezsigntemplatesigner will be invited to validate the Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments", alias="iEzsigntemplatesignatureValidationstep")
    i_ezsigntemplatesignature_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsigntemplatesignature  This can only be set if eEzsigntemplatesignatureType is **FieldText** or **FieldTextarea**", alias="iEzsigntemplatesignatureMaxlength")
    s_ezsigntemplatesignature_defaultvalue: Optional[StrictStr] = Field(default=None, description="The default value for the Ezsigntemplatesignature  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sCompany} | Company name | eZmax Solutions Inc. | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 |", alias="sEzsigntemplatesignatureDefaultvalue")
    s_ezsigntemplatesignature_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsigntemplatesignature.  This can only be set if eEzsigntemplatesignatureType is **Text** or **Textarea**", alias="sEzsigntemplatesignatureRegexp")
    e_ezsigntemplatesignature_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsigntemplatesignatureTextvalidation")
    s_ezsigntemplatesignature_textvalidationcustommessage: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Description of validation rule. Show by signatory.", alias="sEzsigntemplatesignatureTextvalidationcustommessage")
    e_ezsigntemplatesignature_dependencyrequirement: Optional[FieldEEzsigntemplatesignatureDependencyrequirement] = Field(default=None, alias="eEzsigntemplatesignatureDependencyrequirement")
    s_ezsigntemplatesignature_positioningpattern: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The string pattern to search for the positioning. **This is not a regexp**  This will be required if **eEzsigntemplatesignaturePositioning** is set to **PerCoordinates**", alias="sEzsigntemplatesignaturePositioningpattern")
    i_ezsigntemplatesignature_positioningoffsetx: Optional[StrictInt] = Field(default=None, description="The offset X  This will be required if **eEzsigntemplatesignaturePositioning** is set to **PerCoordinates**", alias="iEzsigntemplatesignaturePositioningoffsetx")
    i_ezsigntemplatesignature_positioningoffsety: Optional[StrictInt] = Field(default=None, description="The offset Y  This will be required if **eEzsigntemplatesignaturePositioning** is set to **PerCoordinates**", alias="iEzsigntemplatesignaturePositioningoffsety")
    e_ezsigntemplatesignature_positioningoccurence: Optional[FieldEEzsigntemplatesignaturePositioningoccurence] = Field(default=None, alias="eEzsigntemplatesignaturePositioningoccurence")
    b_ezsigntemplatesignature_customdate: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**)", alias="bEzsigntemplatesignatureCustomdate")
    a_obj_ezsigntemplatesignaturecustomdate: Optional[List[EzsigntemplatesignaturecustomdateRequestCompoundV2]] = Field(default=None, description="An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.", alias="a_objEzsigntemplatesignaturecustomdate")
    a_obj_ezsigntemplateelementdependency: Optional[List[EzsigntemplateelementdependencyRequestCompound]] = Field(default=None, alias="a_objEzsigntemplateelementdependency")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatesignatureID", "fkiEzsigntemplatedocumentID", "fkiEzsigntemplatesignerID", "fkiEzsigntemplatesignerIDValidation", "bEzsigntemplatesignatureHandwritten", "bEzsigntemplatesignatureReason", "eEzsigntemplatesignaturePositioning", "iEzsigntemplatedocumentpagePagenumber", "iEzsigntemplatesignatureX", "iEzsigntemplatesignatureY", "iEzsigntemplatesignatureWidth", "iEzsigntemplatesignatureHeight", "iEzsigntemplatesignatureStep", "eEzsigntemplatesignatureType", "eEzsigntemplatesignatureConsultationtrigger", "tEzsigntemplatesignatureTooltip", "eEzsigntemplatesignatureTooltipposition", "eEzsigntemplatesignatureFont", "bEzsigntemplatesignatureRequired", "eEzsigntemplatesignatureAttachmentnamesource", "sEzsigntemplatesignatureAttachmentdescription", "iEzsigntemplatesignatureValidationstep", "iEzsigntemplatesignatureMaxlength", "sEzsigntemplatesignatureDefaultvalue", "sEzsigntemplatesignatureRegexp", "eEzsigntemplatesignatureTextvalidation", "sEzsigntemplatesignatureTextvalidationcustommessage", "eEzsigntemplatesignatureDependencyrequirement", "sEzsigntemplatesignaturePositioningpattern", "iEzsigntemplatesignaturePositioningoffsetx", "iEzsigntemplatesignaturePositioningoffsety", "eEzsigntemplatesignaturePositioningoccurence", "bEzsigntemplatesignatureCustomdate", "a_objEzsigntemplatesignaturecustomdate", "a_objEzsigntemplateelementdependency"]

    @field_validator('s_ezsigntemplatesignature_regexp')
    def s_ezsigntemplatesignature_regexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\^.*\$$|^$", value):
            raise ValueError(r"must validate the regular expression /^\^.*\$$|^$/")
        return value

    @field_validator('s_ezsigntemplatesignature_positioningpattern')
    def s_ezsigntemplatesignature_positioningpattern_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,30}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,30}$/")
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
        """Create an instance of EzsigntemplatesignatureRequestCompoundV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatesignaturecustomdate (list)
        _items = []
        if self.a_obj_ezsigntemplatesignaturecustomdate:
            for _item_a_obj_ezsigntemplatesignaturecustomdate in self.a_obj_ezsigntemplatesignaturecustomdate:
                if _item_a_obj_ezsigntemplatesignaturecustomdate:
                    _items.append(_item_a_obj_ezsigntemplatesignaturecustomdate.to_dict())
            _dict['a_objEzsigntemplatesignaturecustomdate'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplateelementdependency (list)
        _items = []
        if self.a_obj_ezsigntemplateelementdependency:
            for _item_a_obj_ezsigntemplateelementdependency in self.a_obj_ezsigntemplateelementdependency:
                if _item_a_obj_ezsigntemplateelementdependency:
                    _items.append(_item_a_obj_ezsigntemplateelementdependency.to_dict())
            _dict['a_objEzsigntemplateelementdependency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigntemplatesignatureRequestCompoundV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatesignatureID": obj.get("pkiEzsigntemplatesignatureID"),
            "fkiEzsigntemplatedocumentID": obj.get("fkiEzsigntemplatedocumentID"),
            "fkiEzsigntemplatesignerID": obj.get("fkiEzsigntemplatesignerID"),
            "fkiEzsigntemplatesignerIDValidation": obj.get("fkiEzsigntemplatesignerIDValidation"),
            "bEzsigntemplatesignatureHandwritten": obj.get("bEzsigntemplatesignatureHandwritten"),
            "bEzsigntemplatesignatureReason": obj.get("bEzsigntemplatesignatureReason"),
            "eEzsigntemplatesignaturePositioning": obj.get("eEzsigntemplatesignaturePositioning"),
            "iEzsigntemplatedocumentpagePagenumber": obj.get("iEzsigntemplatedocumentpagePagenumber"),
            "iEzsigntemplatesignatureX": obj.get("iEzsigntemplatesignatureX"),
            "iEzsigntemplatesignatureY": obj.get("iEzsigntemplatesignatureY"),
            "iEzsigntemplatesignatureWidth": obj.get("iEzsigntemplatesignatureWidth"),
            "iEzsigntemplatesignatureHeight": obj.get("iEzsigntemplatesignatureHeight"),
            "iEzsigntemplatesignatureStep": obj.get("iEzsigntemplatesignatureStep"),
            "eEzsigntemplatesignatureType": obj.get("eEzsigntemplatesignatureType"),
            "eEzsigntemplatesignatureConsultationtrigger": obj.get("eEzsigntemplatesignatureConsultationtrigger"),
            "tEzsigntemplatesignatureTooltip": obj.get("tEzsigntemplatesignatureTooltip"),
            "eEzsigntemplatesignatureTooltipposition": obj.get("eEzsigntemplatesignatureTooltipposition"),
            "eEzsigntemplatesignatureFont": obj.get("eEzsigntemplatesignatureFont"),
            "bEzsigntemplatesignatureRequired": obj.get("bEzsigntemplatesignatureRequired"),
            "eEzsigntemplatesignatureAttachmentnamesource": obj.get("eEzsigntemplatesignatureAttachmentnamesource"),
            "sEzsigntemplatesignatureAttachmentdescription": obj.get("sEzsigntemplatesignatureAttachmentdescription"),
            "iEzsigntemplatesignatureValidationstep": obj.get("iEzsigntemplatesignatureValidationstep"),
            "iEzsigntemplatesignatureMaxlength": obj.get("iEzsigntemplatesignatureMaxlength"),
            "sEzsigntemplatesignatureDefaultvalue": obj.get("sEzsigntemplatesignatureDefaultvalue"),
            "sEzsigntemplatesignatureRegexp": obj.get("sEzsigntemplatesignatureRegexp"),
            "eEzsigntemplatesignatureTextvalidation": obj.get("eEzsigntemplatesignatureTextvalidation"),
            "sEzsigntemplatesignatureTextvalidationcustommessage": obj.get("sEzsigntemplatesignatureTextvalidationcustommessage"),
            "eEzsigntemplatesignatureDependencyrequirement": obj.get("eEzsigntemplatesignatureDependencyrequirement"),
            "sEzsigntemplatesignaturePositioningpattern": obj.get("sEzsigntemplatesignaturePositioningpattern"),
            "iEzsigntemplatesignaturePositioningoffsetx": obj.get("iEzsigntemplatesignaturePositioningoffsetx"),
            "iEzsigntemplatesignaturePositioningoffsety": obj.get("iEzsigntemplatesignaturePositioningoffsety"),
            "eEzsigntemplatesignaturePositioningoccurence": obj.get("eEzsigntemplatesignaturePositioningoccurence"),
            "bEzsigntemplatesignatureCustomdate": obj.get("bEzsigntemplatesignatureCustomdate"),
            "a_objEzsigntemplatesignaturecustomdate": [EzsigntemplatesignaturecustomdateRequestCompoundV2.from_dict(_item) for _item in obj["a_objEzsigntemplatesignaturecustomdate"]] if obj.get("a_objEzsigntemplatesignaturecustomdate") is not None else None,
            "a_objEzsigntemplateelementdependency": [EzsigntemplateelementdependencyRequestCompound.from_dict(_item) for _item in obj["a_objEzsigntemplateelementdependency"]] if obj.get("a_objEzsigntemplateelementdependency") is not None else None
        })
        return _obj


