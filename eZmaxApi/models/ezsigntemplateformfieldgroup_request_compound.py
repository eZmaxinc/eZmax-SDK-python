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
from eZmaxApi.models.custom_dropdown_element_request_compound import CustomDropdownElementRequestCompound
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.ezsigntemplateformfield_request_compound import EzsigntemplateformfieldRequestCompound
from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_request_compound import EzsigntemplateformfieldgroupsignerRequestCompound
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_signerrequirement import FieldEEzsigntemplateformfieldgroupSignerrequirement
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_tooltipposition import FieldEEzsigntemplateformfieldgroupTooltipposition
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_type import FieldEEzsigntemplateformfieldgroupType

class EzsigntemplateformfieldgroupRequestCompound(BaseModel):
    """
    A Ezsigntemplateformfieldgroup Object and children  # noqa: E501
    """
    pki_ezsigntemplateformfieldgroup_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsigntemplateformfieldgroupID", description="The unique ID of the Ezsigntemplateformfieldgroup")
    fki_ezsigntemplatedocument_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigntemplatedocumentID", description="The unique ID of the Ezsigntemplatedocument")
    e_ezsigntemplateformfieldgroup_type: FieldEEzsigntemplateformfieldgroupType = Field(..., alias="eEzsigntemplateformfieldgroupType")
    e_ezsigntemplateformfieldgroup_signerrequirement: FieldEEzsigntemplateformfieldgroupSignerrequirement = Field(..., alias="eEzsigntemplateformfieldgroupSignerrequirement")
    s_ezsigntemplateformfieldgroup_label: constr(strict=True, max_length=50, min_length=1) = Field(..., alias="sEzsigntemplateformfieldgroupLabel", description="The Label for the Ezsigntemplateformfieldgroup")
    i_ezsigntemplateformfieldgroup_step: conint(strict=True, ge=1) = Field(..., alias="iEzsigntemplateformfieldgroupStep", description="The step when the Ezsigntemplatesigner will be invited to fill the form fields")
    s_ezsigntemplateformfieldgroup_defaultvalue: StrictStr = Field(..., alias="sEzsigntemplateformfieldgroupDefaultvalue", description="The default value for the Ezsigntemplateformfieldgroup")
    i_ezsigntemplateformfieldgroup_filledmin: conint(strict=True, ge=0) = Field(..., alias="iEzsigntemplateformfieldgroupFilledmin", description="The minimum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup")
    i_ezsigntemplateformfieldgroup_filledmax: conint(strict=True, ge=0) = Field(..., alias="iEzsigntemplateformfieldgroupFilledmax", description="The maximum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup")
    b_ezsigntemplateformfieldgroup_readonly: StrictBool = Field(..., alias="bEzsigntemplateformfieldgroupReadonly", description="Whether the Ezsigntemplateformfieldgroup is read only or not.")
    i_ezsigntemplateformfieldgroup_maxlength: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="iEzsigntemplateformfieldgroupMaxlength", description="The maximum length for the value in the Ezsigntemplateformfieldgroup  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**")
    b_ezsigntemplateformfieldgroup_encrypted: Optional[StrictBool] = Field(None, alias="bEzsigntemplateformfieldgroupEncrypted", description="Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**")
    s_ezsigntemplateformfieldgroup_regexp: Optional[constr(strict=True)] = Field(None, alias="sEzsigntemplateformfieldgroupRegexp", description="A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**")
    e_ezsigntemplateformfieldgroup_textvalidation: Optional[EnumTextvalidation] = Field(None, alias="eEzsigntemplateformfieldgroupTextvalidation")
    t_ezsigntemplateformfieldgroup_tooltip: Optional[StrictStr] = Field(None, alias="tEzsigntemplateformfieldgroupTooltip", description="A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup")
    e_ezsigntemplateformfieldgroup_tooltipposition: Optional[FieldEEzsigntemplateformfieldgroupTooltipposition] = Field(None, alias="eEzsigntemplateformfieldgroupTooltipposition")
    a_obj_ezsigntemplateformfieldgroupsigner: conlist(EzsigntemplateformfieldgroupsignerRequestCompound) = Field(..., alias="a_objEzsigntemplateformfieldgroupsigner")
    a_obj_dropdown_element: Optional[conlist(CustomDropdownElementRequestCompound)] = Field(None, alias="a_objDropdownElement")
    a_obj_ezsigntemplateformfield: conlist(EzsigntemplateformfieldRequestCompound) = Field(..., alias="a_objEzsigntemplateformfield")
    __properties = ["pkiEzsigntemplateformfieldgroupID", "fkiEzsigntemplatedocumentID", "eEzsigntemplateformfieldgroupType", "eEzsigntemplateformfieldgroupSignerrequirement", "sEzsigntemplateformfieldgroupLabel", "iEzsigntemplateformfieldgroupStep", "sEzsigntemplateformfieldgroupDefaultvalue", "iEzsigntemplateformfieldgroupFilledmin", "iEzsigntemplateformfieldgroupFilledmax", "bEzsigntemplateformfieldgroupReadonly", "iEzsigntemplateformfieldgroupMaxlength", "bEzsigntemplateformfieldgroupEncrypted", "sEzsigntemplateformfieldgroupRegexp", "eEzsigntemplateformfieldgroupTextvalidation", "tEzsigntemplateformfieldgroupTooltip", "eEzsigntemplateformfieldgroupTooltipposition", "a_objEzsigntemplateformfieldgroupsigner", "a_objDropdownElement", "a_objEzsigntemplateformfield"]

    @validator('s_ezsigntemplateformfieldgroup_regexp')
    def s_ezsigntemplateformfieldgroup_regexp_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> EzsigntemplateformfieldgroupRequestCompound:
        """Create an instance of EzsigntemplateformfieldgroupRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplateformfieldgroupsigner (list)
        _items = []
        if self.a_obj_ezsigntemplateformfieldgroupsigner:
            for _item in self.a_obj_ezsigntemplateformfieldgroupsigner:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplateformfieldgroupsigner'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_dropdown_element (list)
        _items = []
        if self.a_obj_dropdown_element:
            for _item in self.a_obj_dropdown_element:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objDropdownElement'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplateformfield (list)
        _items = []
        if self.a_obj_ezsigntemplateformfield:
            for _item in self.a_obj_ezsigntemplateformfield:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplateformfield'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplateformfieldgroupRequestCompound:
        """Create an instance of EzsigntemplateformfieldgroupRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplateformfieldgroupRequestCompound.parse_obj(obj)

        _obj = EzsigntemplateformfieldgroupRequestCompound.parse_obj({
            "pki_ezsigntemplateformfieldgroup_id": obj.get("pkiEzsigntemplateformfieldgroupID"),
            "fki_ezsigntemplatedocument_id": obj.get("fkiEzsigntemplatedocumentID"),
            "e_ezsigntemplateformfieldgroup_type": obj.get("eEzsigntemplateformfieldgroupType"),
            "e_ezsigntemplateformfieldgroup_signerrequirement": obj.get("eEzsigntemplateformfieldgroupSignerrequirement"),
            "s_ezsigntemplateformfieldgroup_label": obj.get("sEzsigntemplateformfieldgroupLabel"),
            "i_ezsigntemplateformfieldgroup_step": obj.get("iEzsigntemplateformfieldgroupStep"),
            "s_ezsigntemplateformfieldgroup_defaultvalue": obj.get("sEzsigntemplateformfieldgroupDefaultvalue"),
            "i_ezsigntemplateformfieldgroup_filledmin": obj.get("iEzsigntemplateformfieldgroupFilledmin"),
            "i_ezsigntemplateformfieldgroup_filledmax": obj.get("iEzsigntemplateformfieldgroupFilledmax"),
            "b_ezsigntemplateformfieldgroup_readonly": obj.get("bEzsigntemplateformfieldgroupReadonly"),
            "i_ezsigntemplateformfieldgroup_maxlength": obj.get("iEzsigntemplateformfieldgroupMaxlength"),
            "b_ezsigntemplateformfieldgroup_encrypted": obj.get("bEzsigntemplateformfieldgroupEncrypted"),
            "s_ezsigntemplateformfieldgroup_regexp": obj.get("sEzsigntemplateformfieldgroupRegexp"),
            "e_ezsigntemplateformfieldgroup_textvalidation": obj.get("eEzsigntemplateformfieldgroupTextvalidation"),
            "t_ezsigntemplateformfieldgroup_tooltip": obj.get("tEzsigntemplateformfieldgroupTooltip"),
            "e_ezsigntemplateformfieldgroup_tooltipposition": obj.get("eEzsigntemplateformfieldgroupTooltipposition"),
            "a_obj_ezsigntemplateformfieldgroupsigner": [EzsigntemplateformfieldgroupsignerRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplateformfieldgroupsigner")] if obj.get("a_objEzsigntemplateformfieldgroupsigner") is not None else None,
            "a_obj_dropdown_element": [CustomDropdownElementRequestCompound.from_dict(_item) for _item in obj.get("a_objDropdownElement")] if obj.get("a_objDropdownElement") is not None else None,
            "a_obj_ezsigntemplateformfield": [EzsigntemplateformfieldRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsigntemplateformfield")] if obj.get("a_objEzsigntemplateformfield") is not None else None
        })
        return _obj


