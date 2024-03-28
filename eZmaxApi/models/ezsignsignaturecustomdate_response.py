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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignaturecustomdateResponse(BaseModel):
    """
    An Ezsignsignaturecustomdate Object
    """ # noqa: E501
    pki_ezsignsignaturecustomdate_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignsignaturecustomdate", alias="pkiEzsignsignaturecustomdateID")
    i_ezsignsignaturecustomdate_x: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The X coordinate (Horizontal) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 2 inches from the left border of the page, you would use \"200\" for the X coordinate.", alias="iEzsignsignaturecustomdateX")
    i_ezsignsignaturecustomdate_y: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The Y coordinate (Vertical) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.", alias="iEzsignsignaturecustomdateY")
    i_ezsignsignaturecustomdate_offsetx: Optional[StrictInt] = Field(default=None, description="The X coordinate (Horizontal) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 2 inches from the left of the signature, you would use \"200\" for the X coordinate.", alias="iEzsignsignaturecustomdateOffsetx")
    i_ezsignsignaturecustomdate_offsety: Optional[StrictInt] = Field(default=None, description="The Y coordinate (Vertical) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 3 inches from the top of the signature, you would use \"300\" for the Y coordinate.", alias="iEzsignsignaturecustomdateOffsety")
    s_ezsignsignaturecustomdate_format: StrictStr = Field(description="The custom date format to use  You can use the codes below and they will be replaced at signature time. Text values like month and day names will be rendered in the proper language. Other text will be left as-is.  The codes examples below are based on the following datetime: Thursday, January 6, 2022 at 08:07:09 EST  For example, the format \"Signature date: {MM}/{DD}/{YYYY} {hh}:{mm}\" would become \"Signature date: 01/06/2022 08:07\"  **Year**  | Code | Example | | - | - | | {YYYY} | 2022 | | {YY} | 22 |  **Month**  | Code | Example | | - | - | | {MonthCapitalize} | Janvier | | {Month} | janvier | | {MM} | 01 | | {M} | 1 |  **Day**  | Code | Example | | - | - | | {DayCapitalize} | Jeudi | | {Day} | jeudi | | {DD} | 06 | | {D} | 6 |  **Hour**  | Code | Example | | - | - | | {hh} | 08 |  **Minute**  | Code | Example | | - | - | | {mm} | 07 |  **Second**  | Code | Example | | - | - | | {ss} | 09 |        **Timezone**  | Code | Example | | - | - | | {Z} | EST |       **Time**  | Code | Example | | - | - | | {Time} | 08:07:09 |   | {TimeZ} | 08:07:09 EST |     **Date**  | Code | Example | | - | - | | {Date} | 2022-01-06 |   | {DateText} | 1er Janvier 2022 |  **Full**  | Code | Example | | - | - | | {DateTime} | 2022-01-06 08:07:09 |   | {DateTimeZ} | 2022-01-06 08:07:09 EST | ", alias="sEzsignsignaturecustomdateFormat")
    __properties: ClassVar[List[str]] = ["pkiEzsignsignaturecustomdateID", "iEzsignsignaturecustomdateX", "iEzsignsignaturecustomdateY", "iEzsignsignaturecustomdateOffsetx", "iEzsignsignaturecustomdateOffsety", "sEzsignsignaturecustomdateFormat"]

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
        """Create an instance of EzsignsignaturecustomdateResponse from a JSON string"""
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
        """Create an instance of EzsignsignaturecustomdateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignsignaturecustomdateID": obj.get("pkiEzsignsignaturecustomdateID"),
            "iEzsignsignaturecustomdateX": obj.get("iEzsignsignaturecustomdateX"),
            "iEzsignsignaturecustomdateY": obj.get("iEzsignsignaturecustomdateY"),
            "iEzsignsignaturecustomdateOffsetx": obj.get("iEzsignsignaturecustomdateOffsetx"),
            "iEzsignsignaturecustomdateOffsety": obj.get("iEzsignsignaturecustomdateOffsety"),
            "sEzsignsignaturecustomdateFormat": obj.get("sEzsignsignaturecustomdateFormat")
        })
        return _obj


