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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsigntemplateformfield_dependencyrequirement import FieldEEzsigntemplateformfieldDependencyrequirement
from eZmaxApi.models.field_e_ezsigntemplateformfield_positioning import FieldEEzsigntemplateformfieldPositioning
from eZmaxApi.models.field_e_ezsigntemplateformfield_positioningoccurence import FieldEEzsigntemplateformfieldPositioningoccurence
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateformfieldRequest(BaseModel):
    """
    A Ezsigntemplateformfield Object
    """ # noqa: E501
    pki_ezsigntemplateformfield_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplateformfield", alias="pkiEzsigntemplateformfieldID")
    e_ezsigntemplateformfield_positioning: Optional[FieldEEzsigntemplateformfieldPositioning] = Field(default=None, alias="eEzsigntemplateformfieldPositioning")
    i_ezsigntemplatedocumentpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigntemplatedocument", alias="iEzsigntemplatedocumentpagePagenumber")
    s_ezsigntemplateformfield_label: StrictStr = Field(description="The Label for the Ezsigntemplateformfield", alias="sEzsigntemplateformfieldLabel")
    s_ezsigntemplateformfield_value: Optional[StrictStr] = Field(default=None, description="The value for the Ezsigntemplateformfield", alias="sEzsigntemplateformfieldValue")
    i_ezsigntemplateformfield_x: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The X coordinate (Horizontal) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsigntemplateformfieldX")
    i_ezsigntemplateformfield_y: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The Y coordinate (Vertical) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsigntemplateformfieldY")
    i_ezsigntemplateformfield_width: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Width of the Ezsigntemplateformfield in pixels calculated at 100 DPI  The allowed values are varying based on the eEzsigntemplateformfieldgroupType.  | eEzsigntemplateformfieldgroupType | Valid values | | ------------------------- | ------------ | | Checkbox                  | 22           | | Dropdown                  | 22-65535     | | Radio                     | 22           | | Text                      | 22-65535     | | Textarea                  | 22-65535     |", alias="iEzsigntemplateformfieldWidth")
    i_ezsigntemplateformfield_height: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Height of the Ezsigntemplateformfield in pixels calculated at 100 DPI  The allowed values are varying based on the eEzsigntemplateformfieldgroupType.  | eEzsigntemplateformfieldgroupType | Valid values | | ------------------------- | ------------ | | Checkbox                  | 22           | | Dropdown                  | 22           | | Radio                     | 22           | | Text                      | 22           | | Textarea                  | 22-65535     | ", alias="iEzsigntemplateformfieldHeight")
    b_ezsigntemplateformfield_autocomplete: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplateformfield allows the use of the autocomplete of the browser.  This can only be set if eEzsigntemplateformfieldgroupType is **Text**", alias="bEzsigntemplateformfieldAutocomplete")
    b_ezsigntemplateformfield_selected: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplateformfield is selected or not by default.  This can only be set if eEzsigntemplateformfieldgroupType is **Checkbox** or **Radio**", alias="bEzsigntemplateformfieldSelected")
    e_ezsigntemplateformfield_dependencyrequirement: Optional[FieldEEzsigntemplateformfieldDependencyrequirement] = Field(default=None, alias="eEzsigntemplateformfieldDependencyrequirement")
    s_ezsigntemplateformfield_positioningpattern: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The string pattern to search for the positioning. **This is not a regexp**  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates**", alias="sEzsigntemplateformfieldPositioningpattern")
    i_ezsigntemplateformfield_positioningoffsetx: Optional[StrictInt] = Field(default=None, description="The offset X  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates**", alias="iEzsigntemplateformfieldPositioningoffsetx")
    i_ezsigntemplateformfield_positioningoffsety: Optional[StrictInt] = Field(default=None, description="The offset Y  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates**", alias="iEzsigntemplateformfieldPositioningoffsety")
    e_ezsigntemplateformfield_positioningoccurence: Optional[FieldEEzsigntemplateformfieldPositioningoccurence] = Field(default=None, alias="eEzsigntemplateformfieldPositioningoccurence")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateformfieldID", "eEzsigntemplateformfieldPositioning", "iEzsigntemplatedocumentpagePagenumber", "sEzsigntemplateformfieldLabel", "sEzsigntemplateformfieldValue", "iEzsigntemplateformfieldX", "iEzsigntemplateformfieldY", "iEzsigntemplateformfieldWidth", "iEzsigntemplateformfieldHeight", "bEzsigntemplateformfieldAutocomplete", "bEzsigntemplateformfieldSelected", "eEzsigntemplateformfieldDependencyrequirement", "sEzsigntemplateformfieldPositioningpattern", "iEzsigntemplateformfieldPositioningoffsetx", "iEzsigntemplateformfieldPositioningoffsety", "eEzsigntemplateformfieldPositioningoccurence"]

    @field_validator('s_ezsigntemplateformfield_positioningpattern')
    def s_ezsigntemplateformfield_positioningpattern_validate_regular_expression(cls, value):
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
        """Create an instance of EzsigntemplateformfieldRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigntemplateformfieldRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateformfieldID": obj.get("pkiEzsigntemplateformfieldID"),
            "eEzsigntemplateformfieldPositioning": obj.get("eEzsigntemplateformfieldPositioning"),
            "iEzsigntemplatedocumentpagePagenumber": obj.get("iEzsigntemplatedocumentpagePagenumber"),
            "sEzsigntemplateformfieldLabel": obj.get("sEzsigntemplateformfieldLabel"),
            "sEzsigntemplateformfieldValue": obj.get("sEzsigntemplateformfieldValue"),
            "iEzsigntemplateformfieldX": obj.get("iEzsigntemplateformfieldX"),
            "iEzsigntemplateformfieldY": obj.get("iEzsigntemplateformfieldY"),
            "iEzsigntemplateformfieldWidth": obj.get("iEzsigntemplateformfieldWidth"),
            "iEzsigntemplateformfieldHeight": obj.get("iEzsigntemplateformfieldHeight"),
            "bEzsigntemplateformfieldAutocomplete": obj.get("bEzsigntemplateformfieldAutocomplete"),
            "bEzsigntemplateformfieldSelected": obj.get("bEzsigntemplateformfieldSelected"),
            "eEzsigntemplateformfieldDependencyrequirement": obj.get("eEzsigntemplateformfieldDependencyrequirement"),
            "sEzsigntemplateformfieldPositioningpattern": obj.get("sEzsigntemplateformfieldPositioningpattern"),
            "iEzsigntemplateformfieldPositioningoffsetx": obj.get("iEzsigntemplateformfieldPositioningoffsetx"),
            "iEzsigntemplateformfieldPositioningoffsety": obj.get("iEzsigntemplateformfieldPositioningoffsety"),
            "eEzsigntemplateformfieldPositioningoccurence": obj.get("eEzsigntemplateformfieldPositioningoccurence")
        })
        return _obj


