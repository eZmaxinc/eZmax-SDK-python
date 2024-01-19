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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.custom_create_ezsignelements_positioned_by_word_request import CustomCreateEzsignelementsPositionedByWordRequest
from eZmaxApi.models.custom_dropdown_element_request_compound import CustomDropdownElementRequestCompound
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.ezsignformfield_request_compound import EzsignformfieldRequestCompound
from eZmaxApi.models.ezsignformfieldgroupsigner_request_compound import EzsignformfieldgroupsignerRequestCompound
from eZmaxApi.models.field_e_ezsignformfieldgroup_signerrequirement import FieldEEzsignformfieldgroupSignerrequirement
from eZmaxApi.models.field_e_ezsignformfieldgroup_tooltipposition import FieldEEzsignformfieldgroupTooltipposition
from eZmaxApi.models.field_e_ezsignformfieldgroup_type import FieldEEzsignformfieldgroupType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest(BaseModel):
    """
    An Ezsignformfieldgroup Object in the context of a createEzsignelementsPositionedByWord path
    """ # noqa: E501
    pki_ezsignformfieldgroup_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignformfieldgroup", alias="pkiEzsignformfieldgroupID")
    fki_ezsigndocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentID")
    e_ezsignformfieldgroup_type: FieldEEzsignformfieldgroupType = Field(alias="eEzsignformfieldgroupType")
    e_ezsignformfieldgroup_signerrequirement: FieldEEzsignformfieldgroupSignerrequirement = Field(alias="eEzsignformfieldgroupSignerrequirement")
    s_ezsignformfieldgroup_label: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The Label for the Ezsignformfieldgroup", alias="sEzsignformfieldgroupLabel")
    i_ezsignformfieldgroup_step: Annotated[int, Field(strict=True, ge=1)] = Field(description="The step when the Ezsignsigner will be invited to fill the form fields", alias="iEzsignformfieldgroupStep")
    s_ezsignformfieldgroup_defaultvalue: Optional[StrictStr] = Field(default=None, description="The default value for the Ezsignformfieldgroup", alias="sEzsignformfieldgroupDefaultvalue")
    i_ezsignformfieldgroup_filledmin: Annotated[int, Field(strict=True, ge=0)] = Field(description="The minimum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup", alias="iEzsignformfieldgroupFilledmin")
    i_ezsignformfieldgroup_filledmax: Annotated[int, Field(strict=True, ge=0)] = Field(description="The maximum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup", alias="iEzsignformfieldgroupFilledmax")
    b_ezsignformfieldgroup_readonly: StrictBool = Field(description="Whether the Ezsignformfieldgroup is read only or not.", alias="bEzsignformfieldgroupReadonly")
    i_ezsignformfieldgroup_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsignformfieldgroup  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="iEzsignformfieldgroupMaxlength")
    b_ezsignformfieldgroup_encrypted: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="bEzsignformfieldgroupEncrypted")
    s_ezsignformfieldgroup_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="sEzsignformfieldgroupRegexp")
    t_ezsignformfieldgroup_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup", alias="tEzsignformfieldgroupTooltip")
    e_ezsignformfieldgroup_tooltipposition: Optional[FieldEEzsignformfieldgroupTooltipposition] = Field(default=None, alias="eEzsignformfieldgroupTooltipposition")
    e_ezsignformfieldgroup_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsignformfieldgroupTextvalidation")
    a_obj_ezsignformfieldgroupsigner: List[EzsignformfieldgroupsignerRequestCompound] = Field(alias="a_objEzsignformfieldgroupsigner")
    a_obj_dropdown_element: Optional[List[CustomDropdownElementRequestCompound]] = Field(default=None, alias="a_objDropdownElement")
    a_obj_ezsignformfield: List[EzsignformfieldRequestCompound] = Field(alias="a_objEzsignformfield")
    obj_createezsignelementspositionedbyword: CustomCreateEzsignelementsPositionedByWordRequest = Field(alias="objCreateezsignelementspositionedbyword")
    __properties: ClassVar[List[str]] = ["pkiEzsignformfieldgroupID", "fkiEzsigndocumentID", "eEzsignformfieldgroupType", "eEzsignformfieldgroupSignerrequirement", "sEzsignformfieldgroupLabel", "iEzsignformfieldgroupStep", "sEzsignformfieldgroupDefaultvalue", "iEzsignformfieldgroupFilledmin", "iEzsignformfieldgroupFilledmax", "bEzsignformfieldgroupReadonly", "iEzsignformfieldgroupMaxlength", "bEzsignformfieldgroupEncrypted", "sEzsignformfieldgroupRegexp", "tEzsignformfieldgroupTooltip", "eEzsignformfieldgroupTooltipposition", "eEzsignformfieldgroupTextvalidation", "a_objEzsignformfieldgroupsigner", "a_objDropdownElement", "a_objEzsignformfield", "objCreateezsignelementspositionedbyword"]

    @field_validator('s_ezsignformfieldgroup_regexp')
    def s_ezsignformfieldgroup_regexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\^.*\$$|^$", value):
            raise ValueError(r"must validate the regular expression /^\^.*\$$|^$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of obj_createezsignelementspositionedbyword
        if self.obj_createezsignelementspositionedbyword:
            _dict['objCreateezsignelementspositionedbyword'] = self.obj_createezsignelementspositionedbyword.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignformfieldgroupID": obj.get("pkiEzsignformfieldgroupID"),
            "fkiEzsigndocumentID": obj.get("fkiEzsigndocumentID"),
            "eEzsignformfieldgroupType": obj.get("eEzsignformfieldgroupType"),
            "eEzsignformfieldgroupSignerrequirement": obj.get("eEzsignformfieldgroupSignerrequirement"),
            "sEzsignformfieldgroupLabel": obj.get("sEzsignformfieldgroupLabel"),
            "iEzsignformfieldgroupStep": obj.get("iEzsignformfieldgroupStep"),
            "sEzsignformfieldgroupDefaultvalue": obj.get("sEzsignformfieldgroupDefaultvalue"),
            "iEzsignformfieldgroupFilledmin": obj.get("iEzsignformfieldgroupFilledmin"),
            "iEzsignformfieldgroupFilledmax": obj.get("iEzsignformfieldgroupFilledmax"),
            "bEzsignformfieldgroupReadonly": obj.get("bEzsignformfieldgroupReadonly"),
            "iEzsignformfieldgroupMaxlength": obj.get("iEzsignformfieldgroupMaxlength"),
            "bEzsignformfieldgroupEncrypted": obj.get("bEzsignformfieldgroupEncrypted"),
            "sEzsignformfieldgroupRegexp": obj.get("sEzsignformfieldgroupRegexp"),
            "tEzsignformfieldgroupTooltip": obj.get("tEzsignformfieldgroupTooltip"),
            "eEzsignformfieldgroupTooltipposition": obj.get("eEzsignformfieldgroupTooltipposition"),
            "eEzsignformfieldgroupTextvalidation": obj.get("eEzsignformfieldgroupTextvalidation"),
            "a_objEzsignformfieldgroupsigner": [EzsignformfieldgroupsignerRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsignformfieldgroupsigner")] if obj.get("a_objEzsignformfieldgroupsigner") is not None else None,
            "a_objDropdownElement": [CustomDropdownElementRequestCompound.from_dict(_item) for _item in obj.get("a_objDropdownElement")] if obj.get("a_objDropdownElement") is not None else None,
            "a_objEzsignformfield": [EzsignformfieldRequestCompound.from_dict(_item) for _item in obj.get("a_objEzsignformfield")] if obj.get("a_objEzsignformfield") is not None else None,
            "objCreateezsignelementspositionedbyword": CustomCreateEzsignelementsPositionedByWordRequest.from_dict(obj.get("objCreateezsignelementspositionedbyword")) if obj.get("objCreateezsignelementspositionedbyword") is not None else None
        })
        return _obj


