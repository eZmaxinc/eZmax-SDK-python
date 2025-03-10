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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.enum_horizontalalignment import EnumHorizontalalignment
from eZmaxApi.models.field_e_ezsignformfield_dependencyrequirement import FieldEEzsignformfieldDependencyrequirement
from eZmaxApi.models.textstylestatic_request_compound import TextstylestaticRequestCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsignformfieldRequest(BaseModel):
    """
    A Ezsignformfield Object
    """ # noqa: E501
    pki_ezsignformfield_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignformfield", alias="pkiEzsignformfieldID")
    i_ezsignpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigndocument", alias="iEzsignpagePagenumber")
    s_ezsignformfield_label: StrictStr = Field(description="The Label for the Ezsignformfield", alias="sEzsignformfieldLabel")
    s_ezsignformfield_value: Optional[StrictStr] = Field(default=None, description="The value for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is Checkbox or Radio", alias="sEzsignformfieldValue")
    i_ezsignformfield_x: Annotated[int, Field(strict=True, ge=0)] = Field(description="The X coordinate (Horizontal) where to put the Ezsignformfield on the Ezsignpage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignformfield 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsignformfieldX")
    i_ezsignformfield_y: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Y coordinate (Vertical) where to put the Ezsignformfield on the Ezsignpage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignformfield 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsignformfieldY")
    i_ezsignformfield_width: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Width of the Ezsignformfield in pixels calculated at 100 DPI", alias="iEzsignformfieldWidth")
    i_ezsignformfield_height: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Height of the Ezsignformfield in pixels calculated at 100 DPI ", alias="iEzsignformfieldHeight")
    b_ezsignformfield_autocomplete: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignformfield allows the use of the autocomplete of the browser.  This can only be set if eEzsignformfieldgroupType is **Text**", alias="bEzsignformfieldAutocomplete")
    b_ezsignformfield_selected: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignformfield is selected or not by default.  This can only be set if eEzsignformfieldgroupType is **Checkbox** or **Radio**", alias="bEzsignformfieldSelected")
    s_ezsignformfield_enteredvalue: Optional[StrictStr] = Field(default=None, description="This is the value enterred for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is **Dropdown**, **Text** or **Textarea**", alias="sEzsignformfieldEnteredvalue")
    e_ezsignformfield_dependencyrequirement: Optional[FieldEEzsignformfieldDependencyrequirement] = Field(default=None, alias="eEzsignformfieldDependencyrequirement")
    e_ezsignformfield_horizontalalignment: Optional[EnumHorizontalalignment] = Field(default=None, alias="eEzsignformfieldHorizontalalignment")
    obj_textstylestatic: Optional[TextstylestaticRequestCompound] = Field(default=None, alias="objTextstylestatic")
    __properties: ClassVar[List[str]] = ["pkiEzsignformfieldID", "iEzsignpagePagenumber", "sEzsignformfieldLabel", "sEzsignformfieldValue", "iEzsignformfieldX", "iEzsignformfieldY", "iEzsignformfieldWidth", "iEzsignformfieldHeight", "bEzsignformfieldAutocomplete", "bEzsignformfieldSelected", "sEzsignformfieldEnteredvalue", "eEzsignformfieldDependencyrequirement", "eEzsignformfieldHorizontalalignment", "objTextstylestatic"]

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
        """Create an instance of EzsignformfieldRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_textstylestatic
        if self.obj_textstylestatic:
            _dict['objTextstylestatic'] = self.obj_textstylestatic.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignformfieldRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignformfieldID": obj.get("pkiEzsignformfieldID"),
            "iEzsignpagePagenumber": obj.get("iEzsignpagePagenumber"),
            "sEzsignformfieldLabel": obj.get("sEzsignformfieldLabel"),
            "sEzsignformfieldValue": obj.get("sEzsignformfieldValue"),
            "iEzsignformfieldX": obj.get("iEzsignformfieldX"),
            "iEzsignformfieldY": obj.get("iEzsignformfieldY"),
            "iEzsignformfieldWidth": obj.get("iEzsignformfieldWidth"),
            "iEzsignformfieldHeight": obj.get("iEzsignformfieldHeight"),
            "bEzsignformfieldAutocomplete": obj.get("bEzsignformfieldAutocomplete"),
            "bEzsignformfieldSelected": obj.get("bEzsignformfieldSelected"),
            "sEzsignformfieldEnteredvalue": obj.get("sEzsignformfieldEnteredvalue"),
            "eEzsignformfieldDependencyrequirement": obj.get("eEzsignformfieldDependencyrequirement"),
            "eEzsignformfieldHorizontalalignment": obj.get("eEzsignformfieldHorizontalalignment"),
            "objTextstylestatic": TextstylestaticRequestCompound.from_dict(obj["objTextstylestatic"]) if obj.get("objTextstylestatic") is not None else None
        })
        return _obj


