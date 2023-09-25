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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist, constr, validator
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.ezsigntemplatesignaturecustomdate_response_compound import EzsigntemplatesignaturecustomdateResponseCompound
from eZmaxApi.models.field_e_ezsigntemplatesignature_attachmentnamesource import FieldEEzsigntemplatesignatureAttachmentnamesource
from eZmaxApi.models.field_e_ezsigntemplatesignature_font import FieldEEzsigntemplatesignatureFont
from eZmaxApi.models.field_e_ezsigntemplatesignature_tooltipposition import FieldEEzsigntemplatesignatureTooltipposition
from eZmaxApi.models.field_e_ezsigntemplatesignature_type import FieldEEzsigntemplatesignatureType

class EzsigntemplatesignatureResponseCompound(BaseModel):
    """
    A Ezsigntemplatesignature Object  # noqa: E501
    """
    pki_ezsigntemplatesignature_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsigntemplatesignatureID", description="The unique ID of the Ezsigntemplatesignature")
    fki_ezsigntemplatedocument_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplatedocumentID", description="The unique ID of the Ezsigntemplatedocument")
    fki_ezsigntemplatesigner_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplatesignerID", description="The unique ID of the Ezsigntemplatesigner")
    fki_ezsigntemplatesigner_id_validation: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsigntemplatesignerIDValidation", description="The unique ID of the Ezsigntemplatesigner")
    i_ezsigntemplatedocumentpage_pagenumber: conint(strict=True, ge=1) = Field(..., alias="iEzsigntemplatedocumentpagePagenumber", description="The page number in the Ezsigntemplatedocument")
    i_ezsigntemplatesignature_x: conint(strict=True, ge=0) = Field(..., alias="iEzsigntemplatesignatureX", description="The X coordinate (Horizontal) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 2 inches from the left border of the page, you would use \"200\" for the X coordinate.")
    i_ezsigntemplatesignature_y: conint(strict=True, ge=0) = Field(..., alias="iEzsigntemplatesignatureY", description="The Y coordinate (Vertical) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.")
    i_ezsigntemplatesignature_width: Optional[conint(strict=True, ge=0)] = Field(None, alias="iEzsigntemplatesignatureWidth", description="The width of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have a width of 2 inches, you would use \"200\" for the iEzsigntemplatesignatureWidth.")
    i_ezsigntemplatesignature_height: Optional[conint(strict=True, ge=0)] = Field(None, alias="iEzsigntemplatesignatureHeight", description="The height of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have an height of 2 inches, you would use \"200\" for the iEzsigntemplatesignatureHeight.")
    i_ezsigntemplatesignature_step: conint(strict=True, ge=1) = Field(..., alias="iEzsigntemplatesignatureStep", description="The step when the Ezsigntemplatesigner will be invited to sign")
    e_ezsigntemplatesignature_type: FieldEEzsigntemplatesignatureType = Field(..., alias="eEzsigntemplatesignatureType")
    t_ezsigntemplatesignature_tooltip: Optional[StrictStr] = Field(None, alias="tEzsigntemplatesignatureTooltip", description="A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature")
    e_ezsigntemplatesignature_tooltipposition: Optional[FieldEEzsigntemplatesignatureTooltipposition] = Field(None, alias="eEzsigntemplatesignatureTooltipposition")
    e_ezsigntemplatesignature_font: Optional[FieldEEzsigntemplatesignatureFont] = Field(None, alias="eEzsigntemplatesignatureFont")
    i_ezsigntemplatesignature_validationstep: Optional[StrictInt] = Field(None, alias="iEzsigntemplatesignatureValidationstep", description="The step when the Ezsigntemplatesigner will be invited to validate the Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments")
    s_ezsigntemplatesignature_attachmentdescription: Optional[StrictStr] = Field(None, alias="sEzsigntemplatesignatureAttachmentdescription", description="The description attached to the attachment name added in Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments")
    e_ezsigntemplatesignature_attachmentnamesource: Optional[FieldEEzsigntemplatesignatureAttachmentnamesource] = Field(None, alias="eEzsigntemplatesignatureAttachmentnamesource")
    b_ezsigntemplatesignature_required: Optional[StrictBool] = Field(None, alias="bEzsigntemplatesignatureRequired", description="Whether the Ezsigntemplatesignature is required or not. This field is relevant only with Ezsigntemplatesignature with eEzsigntemplatesignatureType = Attachments.")
    i_ezsigntemplatesignature_maxlength: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="iEzsigntemplatesignatureMaxlength", description="The maximum length for the value in the Ezsigntemplatesignature  This can only be set if eEzsigntemplatesignatureType is **FieldText** or **FieldTextarea**")
    s_ezsigntemplatesignature_regexp: Optional[constr(strict=True)] = Field(None, alias="sEzsigntemplatesignatureRegexp", description="A regular expression to indicate what values are acceptable for the Ezsigntemplatesignature.  This can only be set if eEzsigntemplatesignatureType is **Text** or **Textarea**")
    e_ezsigntemplatesignature_textvalidation: Optional[EnumTextvalidation] = Field(None, alias="eEzsigntemplatesignatureTextvalidation")
    b_ezsigntemplatesignature_customdate: Optional[StrictBool] = Field(None, alias="bEzsigntemplatesignatureCustomdate", description="Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**)")
    a_obj_ezsigntemplatesignaturecustomdate: Optional[conlist(EzsigntemplatesignaturecustomdateResponseCompound)] = Field(None, alias="a_objEzsigntemplatesignaturecustomdate", description="An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.")
    __properties = ["pkiEzsigntemplatesignatureID", "fkiEzsigntemplatedocumentID", "fkiEzsigntemplatesignerID", "fkiEzsigntemplatesignerIDValidation", "iEzsigntemplatedocumentpagePagenumber", "iEzsigntemplatesignatureX", "iEzsigntemplatesignatureY", "iEzsigntemplatesignatureWidth", "iEzsigntemplatesignatureHeight", "iEzsigntemplatesignatureStep", "eEzsigntemplatesignatureType", "tEzsigntemplatesignatureTooltip", "eEzsigntemplatesignatureTooltipposition", "eEzsigntemplatesignatureFont", "iEzsigntemplatesignatureValidationstep", "sEzsigntemplatesignatureAttachmentdescription", "eEzsigntemplatesignatureAttachmentnamesource", "bEzsigntemplatesignatureRequired", "iEzsigntemplatesignatureMaxlength", "sEzsigntemplatesignatureRegexp", "eEzsigntemplatesignatureTextvalidation", "bEzsigntemplatesignatureCustomdate", "a_objEzsigntemplatesignaturecustomdate"]

    @validator('s_ezsigntemplatesignature_regexp')
    def s_ezsigntemplatesignature_regexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\^.*\$$|^$", value):
            raise ValueError(r"must validate the regular expression /^\^.*\$$|^$/")
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
    def from_json(cls, json_str: str) -> EzsigntemplatesignatureResponseCompound:
        """Create an instance of EzsigntemplatesignatureResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatesignaturecustomdate (list)
        _items = []
        if self.a_obj_ezsigntemplatesignaturecustomdate:
            for _item in self.a_obj_ezsigntemplatesignaturecustomdate:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplatesignaturecustomdate'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatesignatureResponseCompound:
        """Create an instance of EzsigntemplatesignatureResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatesignatureResponseCompound.parse_obj(obj)

        _obj = EzsigntemplatesignatureResponseCompound.parse_obj({
            "pki_ezsigntemplatesignature_id": obj.get("pkiEzsigntemplatesignatureID"),
            "fki_ezsigntemplatedocument_id": obj.get("fkiEzsigntemplatedocumentID"),
            "fki_ezsigntemplatesigner_id": obj.get("fkiEzsigntemplatesignerID"),
            "fki_ezsigntemplatesigner_id_validation": obj.get("fkiEzsigntemplatesignerIDValidation"),
            "i_ezsigntemplatedocumentpage_pagenumber": obj.get("iEzsigntemplatedocumentpagePagenumber"),
            "i_ezsigntemplatesignature_x": obj.get("iEzsigntemplatesignatureX"),
            "i_ezsigntemplatesignature_y": obj.get("iEzsigntemplatesignatureY"),
            "i_ezsigntemplatesignature_width": obj.get("iEzsigntemplatesignatureWidth"),
            "i_ezsigntemplatesignature_height": obj.get("iEzsigntemplatesignatureHeight"),
            "i_ezsigntemplatesignature_step": obj.get("iEzsigntemplatesignatureStep"),
            "e_ezsigntemplatesignature_type": obj.get("eEzsigntemplatesignatureType"),
            "t_ezsigntemplatesignature_tooltip": obj.get("tEzsigntemplatesignatureTooltip"),
            "e_ezsigntemplatesignature_tooltipposition": obj.get("eEzsigntemplatesignatureTooltipposition"),
            "e_ezsigntemplatesignature_font": obj.get("eEzsigntemplatesignatureFont"),
            "i_ezsigntemplatesignature_validationstep": obj.get("iEzsigntemplatesignatureValidationstep"),
            "s_ezsigntemplatesignature_attachmentdescription": obj.get("sEzsigntemplatesignatureAttachmentdescription"),
            "e_ezsigntemplatesignature_attachmentnamesource": obj.get("eEzsigntemplatesignatureAttachmentnamesource"),
            "b_ezsigntemplatesignature_required": obj.get("bEzsigntemplatesignatureRequired"),
            "i_ezsigntemplatesignature_maxlength": obj.get("iEzsigntemplatesignatureMaxlength"),
            "s_ezsigntemplatesignature_regexp": obj.get("sEzsigntemplatesignatureRegexp"),
            "e_ezsigntemplatesignature_textvalidation": obj.get("eEzsigntemplatesignatureTextvalidation"),
            "b_ezsigntemplatesignature_customdate": obj.get("bEzsigntemplatesignatureCustomdate"),
            "a_obj_ezsigntemplatesignaturecustomdate": [EzsigntemplatesignaturecustomdateResponseCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplatesignaturecustomdate")] if obj.get("a_objEzsigntemplatesignaturecustomdate") is not None else None
        })
        return _obj


