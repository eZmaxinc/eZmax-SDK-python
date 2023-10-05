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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, constr, validator
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.field_e_ezsignsignature_attachmentnamesource import FieldEEzsignsignatureAttachmentnamesource
from eZmaxApi.models.field_e_ezsignsignature_dependencyrequirement import FieldEEzsignsignatureDependencyrequirement
from eZmaxApi.models.field_e_ezsignsignature_font import FieldEEzsignsignatureFont
from eZmaxApi.models.field_e_ezsignsignature_tooltipposition import FieldEEzsignsignatureTooltipposition
from eZmaxApi.models.field_e_ezsignsignature_type import FieldEEzsignsignatureType

class EzsignsignatureRequest(BaseModel):
    """
    An Ezsignsignature Object  # noqa: E501
    """
    pki_ezsignsignature_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignsignatureID", description="The unique ID of the Ezsignsignature")
    fki_ezsignfoldersignerassociation_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfoldersignerassociationID", description="The unique ID of the Ezsignfoldersignerassociation")
    i_ezsignpage_pagenumber: conint(strict=True, ge=1) = Field(..., alias="iEzsignpagePagenumber", description="The page number in the Ezsigndocument")
    i_ezsignsignature_x: conint(strict=True, ge=0) = Field(..., alias="iEzsignsignatureX", description="The X coordinate (Horizontal) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 2 inches from the left border of the page, you would use \"200\" for the X coordinate.")
    i_ezsignsignature_y: conint(strict=True, ge=0) = Field(..., alias="iEzsignsignatureY", description="The Y coordinate (Vertical) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.")
    i_ezsignsignature_width: Optional[conint(strict=True, ge=0)] = Field(None, alias="iEzsignsignatureWidth", description="The width of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have a width of 2 inches, you would use \"200\" for the iEzsignsignatureWidth.")
    i_ezsignsignature_height: Optional[conint(strict=True, ge=0)] = Field(None, alias="iEzsignsignatureHeight", description="The height of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have an height of 2 inches, you would use \"200\" for the iEzsignsignatureHeight.")
    i_ezsignsignature_step: StrictInt = Field(..., alias="iEzsignsignatureStep", description="The step when the Ezsignsigner will be invited to sign")
    e_ezsignsignature_type: FieldEEzsignsignatureType = Field(..., alias="eEzsignsignatureType")
    fki_ezsigndocument_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigndocumentID", description="The unique ID of the Ezsigndocument")
    t_ezsignsignature_tooltip: Optional[StrictStr] = Field(None, alias="tEzsignsignatureTooltip", description="A tooltip that will be presented to Ezsignsigner about the Ezsignsignature")
    e_ezsignsignature_tooltipposition: Optional[FieldEEzsignsignatureTooltipposition] = Field(None, alias="eEzsignsignatureTooltipposition")
    e_ezsignsignature_font: Optional[FieldEEzsignsignatureFont] = Field(None, alias="eEzsignsignatureFont")
    fki_ezsignfoldersignerassociation_id_validation: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsignfoldersignerassociationIDValidation", description="The unique ID of the Ezsignfoldersignerassociation")
    b_ezsignsignature_required: Optional[StrictBool] = Field(None, alias="bEzsignsignatureRequired", description="Whether the Ezsignsignature is required or not. This field is relevant only with Ezsignsignature with eEzsignsignatureType = Attachments.")
    e_ezsignsignature_attachmentnamesource: Optional[FieldEEzsignsignatureAttachmentnamesource] = Field(None, alias="eEzsignsignatureAttachmentnamesource")
    s_ezsignsignature_attachmentdescription: Optional[StrictStr] = Field(None, alias="sEzsignsignatureAttachmentdescription", description="The description attached to the attachment name added in Ezsignsignature of eEzsignsignatureType Attachments")
    i_ezsignsignature_validationstep: Optional[StrictInt] = Field(None, alias="iEzsignsignatureValidationstep", description="The step when the Ezsignsigner will be invited to validate the Ezsignsignature of eEzsignsignatureType Attachments")
    i_ezsignsignature_maxlength: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="iEzsignsignatureMaxlength", description="The maximum length for the value in the Ezsignsignature  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea**")
    e_ezsignsignature_textvalidation: Optional[EnumTextvalidation] = Field(None, alias="eEzsignsignatureTextvalidation")
    s_ezsignsignature_regexp: Optional[constr(strict=True)] = Field(None, alias="sEzsignsignatureRegexp", description="A regular expression to indicate what values are acceptable for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea** and eEzsignsignatureTextvalidation is **Custom**")
    e_ezsignsignature_dependencyrequirement: Optional[FieldEEzsignsignatureDependencyrequirement] = Field(None, alias="eEzsignsignatureDependencyrequirement")
    __properties = ["pkiEzsignsignatureID", "fkiEzsignfoldersignerassociationID", "iEzsignpagePagenumber", "iEzsignsignatureX", "iEzsignsignatureY", "iEzsignsignatureWidth", "iEzsignsignatureHeight", "iEzsignsignatureStep", "eEzsignsignatureType", "fkiEzsigndocumentID", "tEzsignsignatureTooltip", "eEzsignsignatureTooltipposition", "eEzsignsignatureFont", "fkiEzsignfoldersignerassociationIDValidation", "bEzsignsignatureRequired", "eEzsignsignatureAttachmentnamesource", "sEzsignsignatureAttachmentdescription", "iEzsignsignatureValidationstep", "iEzsignsignatureMaxlength", "eEzsignsignatureTextvalidation", "sEzsignsignatureRegexp", "eEzsignsignatureDependencyrequirement"]

    @validator('s_ezsignsignature_regexp')
    def s_ezsignsignature_regexp_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> EzsignsignatureRequest:
        """Create an instance of EzsignsignatureRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignatureRequest:
        """Create an instance of EzsignsignatureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignatureRequest.parse_obj(obj)

        _obj = EzsignsignatureRequest.parse_obj({
            "pki_ezsignsignature_id": obj.get("pkiEzsignsignatureID"),
            "fki_ezsignfoldersignerassociation_id": obj.get("fkiEzsignfoldersignerassociationID"),
            "i_ezsignpage_pagenumber": obj.get("iEzsignpagePagenumber"),
            "i_ezsignsignature_x": obj.get("iEzsignsignatureX"),
            "i_ezsignsignature_y": obj.get("iEzsignsignatureY"),
            "i_ezsignsignature_width": obj.get("iEzsignsignatureWidth"),
            "i_ezsignsignature_height": obj.get("iEzsignsignatureHeight"),
            "i_ezsignsignature_step": obj.get("iEzsignsignatureStep"),
            "e_ezsignsignature_type": obj.get("eEzsignsignatureType"),
            "fki_ezsigndocument_id": obj.get("fkiEzsigndocumentID"),
            "t_ezsignsignature_tooltip": obj.get("tEzsignsignatureTooltip"),
            "e_ezsignsignature_tooltipposition": obj.get("eEzsignsignatureTooltipposition"),
            "e_ezsignsignature_font": obj.get("eEzsignsignatureFont"),
            "fki_ezsignfoldersignerassociation_id_validation": obj.get("fkiEzsignfoldersignerassociationIDValidation"),
            "b_ezsignsignature_required": obj.get("bEzsignsignatureRequired"),
            "e_ezsignsignature_attachmentnamesource": obj.get("eEzsignsignatureAttachmentnamesource"),
            "s_ezsignsignature_attachmentdescription": obj.get("sEzsignsignatureAttachmentdescription"),
            "i_ezsignsignature_validationstep": obj.get("iEzsignsignatureValidationstep"),
            "i_ezsignsignature_maxlength": obj.get("iEzsignsignatureMaxlength"),
            "e_ezsignsignature_textvalidation": obj.get("eEzsignsignatureTextvalidation"),
            "s_ezsignsignature_regexp": obj.get("sEzsignsignatureRegexp"),
            "e_ezsignsignature_dependencyrequirement": obj.get("eEzsignsignatureDependencyrequirement")
        })
        return _obj


