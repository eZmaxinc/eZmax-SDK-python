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
from eZmaxApi.models.ezsignformfield_request_compound import EzsignformfieldRequestCompound
from eZmaxApi.models.ezsignformfieldgroupsigner_request_compound import EzsignformfieldgroupsignerRequestCompound
from eZmaxApi.models.field_e_ezsignformfieldgroup_signerrequirement import FieldEEzsignformfieldgroupSignerrequirement
from eZmaxApi.models.field_e_ezsignformfieldgroup_tooltipposition import FieldEEzsignformfieldgroupTooltipposition
from eZmaxApi.models.field_e_ezsignformfieldgroup_type import FieldEEzsignformfieldgroupType

class EzsignformfieldgroupRequestCompound(BaseModel):
    """
    An Ezsignformfieldgroup Object and children to create a complete structure  # noqa: E501
    """
    pki_ezsignformfieldgroup_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzsignformfieldgroupID", description="The unique ID of the Ezsignformfieldgroup")
    fki_ezsigndocument_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsigndocumentID", description="The unique ID of the Ezsigndocument")
    e_ezsignformfieldgroup_type: FieldEEzsignformfieldgroupType = Field(..., alias="eEzsignformfieldgroupType")
    e_ezsignformfieldgroup_signerrequirement: FieldEEzsignformfieldgroupSignerrequirement = Field(..., alias="eEzsignformfieldgroupSignerrequirement")
    s_ezsignformfieldgroup_label: constr(strict=True, max_length=50, min_length=1) = Field(..., alias="sEzsignformfieldgroupLabel", description="The Label for the Ezsignformfieldgroup")
    i_ezsignformfieldgroup_step: conint(strict=True, ge=1) = Field(..., alias="iEzsignformfieldgroupStep", description="The step when the Ezsignsigner will be invited to fill the form fields")
    s_ezsignformfieldgroup_defaultvalue: StrictStr = Field(..., alias="sEzsignformfieldgroupDefaultvalue", description="The default value for the Ezsignformfieldgroup")
    i_ezsignformfieldgroup_filledmin: conint(strict=True, ge=0) = Field(..., alias="iEzsignformfieldgroupFilledmin", description="The minimum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup")
    i_ezsignformfieldgroup_filledmax: conint(strict=True, ge=0) = Field(..., alias="iEzsignformfieldgroupFilledmax", description="The maximum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup")
    b_ezsignformfieldgroup_readonly: StrictBool = Field(..., alias="bEzsignformfieldgroupReadonly", description="Whether the Ezsignformfieldgroup is read only or not.")
    i_ezsignformfieldgroup_maxlength: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="iEzsignformfieldgroupMaxlength", description="The maximum length for the value in the Ezsignformfieldgroup  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**")
    b_ezsignformfieldgroup_encrypted: Optional[StrictBool] = Field(None, alias="bEzsignformfieldgroupEncrypted", description="Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**")
    s_ezsignformfieldgroup_regexp: Optional[constr(strict=True)] = Field(None, alias="sEzsignformfieldgroupRegexp", description="A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**")
    t_ezsignformfieldgroup_tooltip: Optional[StrictStr] = Field(None, alias="tEzsignformfieldgroupTooltip", description="A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup")
    e_ezsignformfieldgroup_tooltipposition: Optional[FieldEEzsignformfieldgroupTooltipposition] = Field(None, alias="eEzsignformfieldgroupTooltipposition")
    e_ezsignformfieldgroup_textvalidation: Optional[EnumTextvalidation] = Field(None, alias="eEzsignformfieldgroupTextvalidation")
    a_obj_ezsignformfieldgroupsigner: conlist(EzsignformfieldgroupsignerRequestCompound) = Field(..., alias="a_objEzsignformfieldgroupsigner")
    a_obj_dropdown_element: Optional[conlist(CustomDropdownElementRequestCompound)] = Field(None, alias="a_objDropdownElement")
    a_obj_ezsignformfield: conlist(EzsignformfieldRequestCompound) = Field(..., alias="a_objEzsignformfield")
    __properties = ["pkiEzsignformfieldgroupID", "fkiEzsigndocumentID", "eEzsignformfieldgroupType", "eEzsignformfieldgroupSignerrequirement", "sEzsignformfieldgroupLabel", "iEzsignformfieldgroupStep", "sEzsignformfieldgroupDefaultvalue", "iEzsignformfieldgroupFilledmin", "iEzsignformfieldgroupFilledmax", "bEzsignformfieldgroupReadonly", "iEzsignformfieldgroupMaxlength", "bEzsignformfieldgroupEncrypted", "sEzsignformfieldgroupRegexp", "tEzsignformfieldgroupTooltip", "eEzsignformfieldgroupTooltipposition", "eEzsignformfieldgroupTextvalidation", "a_objEzsignformfieldgroupsigner", "a_objDropdownElement", "a_objEzsignformfield"]

    @validator('s_ezsignformfieldgroup_regexp')
    def s_ezsignformfieldgroup_regexp_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> EzsignformfieldgroupRequestCompound:
        """Create an instance of EzsignformfieldgroupRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignformfieldgroupsigner (list)
        _items = []
        if self.a_obj_ezsignformfieldgroupsigner:
            for _item in self.a_obj_ezsignformfieldgroupsigner:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignformfieldgroupsigner'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_dropdown_element (list)
        _items = []
        if self.a_obj_dropdown_element:
            for _item in self.a_obj_dropdown_element:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objDropdownElement'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignformfield (list)
        _items = []
        if self.a_obj_ezsignformfield:
            for _item in self.a_obj_ezsignformfield:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsignformfield'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignformfieldgroupRequestCompound:
        """Create an instance of EzsignformfieldgroupRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignformfieldgroupRequestCompound.parse_obj(obj)

        _obj = EzsignformfieldgroupRequestCompound.parse_obj({
            "pki_ezsignformfieldgroup_id": obj.get("pkiEzsignformfieldgroupID"),
            "fki_ezsigndocument_id": obj.get("fkiEzsigndocumentID"),
            "e_ezsignformfieldgroup_type": obj.get("eEzsignformfieldgroupType"),
            "e_ezsignformfieldgroup_signerrequirement": obj.get("eEzsignformfieldgroupSignerrequirement"),
            "s_ezsignformfieldgroup_label": obj.get("sEzsignformfieldgroupLabel"),
            "i_ezsignformfieldgroup_step": obj.get("iEzsignformfieldgroupStep"),
            "s_ezsignformfieldgroup_defaultvalue": obj.get("sEzsignformfieldgroupDefaultvalue"),
            "i_ezsignformfieldgroup_filledmin": obj.get("iEzsignformfieldgroupFilledmin"),
            "i_ezsignformfieldgroup_filledmax": obj.get("iEzsignformfieldgroupFilledmax"),
            "b_ezsignformfieldgroup_readonly": obj.get("bEzsignformfieldgroupReadonly"),
            "i_ezsignformfieldgroup_maxlength": obj.get("iEzsignformfieldgroupMaxlength"),
            "b_ezsignformfieldgroup_encrypted": obj.get("bEzsignformfieldgroupEncrypted"),
            "s_ezsignformfieldgroup_regexp": obj.get("sEzsignformfieldgroupRegexp"),
            "t_ezsignformfieldgroup_tooltip": obj.get("tEzsignformfieldgroupTooltip"),
            "e_ezsignformfieldgroup_tooltipposition": obj.get("eEzsignformfieldgroupTooltipposition"),
            "e_ezsignformfieldgroup_textvalidation": obj.get("eEzsignformfieldgroupTextvalidation"),
            "a_obj_ezsignformfieldgroupsigner": [EzsignformfieldgroupsignerRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsignformfieldgroupsigner")] if obj.get("a_objEzsignformfieldgroupsigner") is not None else None,
            "a_obj_dropdown_element": [CustomDropdownElementRequestCompound.from_dict(_item) for _item in obj.get("a_objDropdownElement")] if obj.get("a_objDropdownElement") is not None else None,
            "a_obj_ezsignformfield": [EzsignformfieldRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsignformfield")] if obj.get("a_objEzsignformfield") is not None else None
        })
        return _obj


