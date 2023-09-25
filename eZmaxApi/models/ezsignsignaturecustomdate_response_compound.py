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



from pydantic import BaseModel, Field, StrictStr, conint

class EzsignsignaturecustomdateResponseCompound(BaseModel):
    """
    An Ezsignsignaturecustomdate Object and children to create a complete structure  # noqa: E501
    """
    pki_ezsignsignaturecustomdate_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsignsignaturecustomdateID", description="The unique ID of the Ezsignsignaturecustomdate")
    i_ezsignsignaturecustomdate_x: conint(strict=True, ge=0) = Field(..., alias="iEzsignsignaturecustomdateX", description="The X coordinate (Horizontal) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 2 inches from the left border of the page, you would use \"200\" for the X coordinate.")
    i_ezsignsignaturecustomdate_y: conint(strict=True, ge=0) = Field(..., alias="iEzsignsignaturecustomdateY", description="The Y coordinate (Vertical) where to put the Ezsignsignaturecustomdate on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignaturecustomdate block 3 inches from the top border of the page, you would use \"300\" for the Y coordinate.")
    s_ezsignsignaturecustomdate_format: StrictStr = Field(..., alias="sEzsignsignaturecustomdateFormat", description="The custom date format to use  You can use the codes below and they will be replaced at signature time. Text values like month and day names will be rendered in the proper language. Other text will be left as-is.  The codes examples below are based on the following datetime: Thursday, January 6, 2022 at 08:07:09 EST  For example, the format \"Signature date: {MM}/{DD}/{YYYY} {hh}:{mm}\" would become \"Signature date: 01/06/2022 08:07\"  **Year**  | Code | Example | | - | - | | {YYYY} | 2022 | | {YY} | 22 |  **Month**  | Code | Example | | - | - | | {MonthCapitalize} | Janvier | | {Month} | janvier | | {MM} | 01 | | {M} | 1 |  **Day**  | Code | Example | | - | - | | {DayCapitalize} | Jeudi | | {Day} | jeudi | | {DD} | 06 | | {D} | 6 |  **Hour**  | Code | Example | | - | - | | {hh} | 08 |  **Minute**  | Code | Example | | - | - | | {mm} | 07 |  **Second**  | Code | Example | | - | - | | {ss} | 09 |        **Timezone**  | Code | Example | | - | - | | {Z} | EST |       **Time**  | Code | Example | | - | - | | {Time} | 08:07:09 |   | {TimeZ} | 08:07:09 EST |     **Date**  | Code | Example | | - | - | | {Date} | 2022-01-06 |   | {DateText} | 1er Janvier 2022 |  **Full**  | Code | Example | | - | - | | {DateTime} | 2022-01-06 08:07:09 |   | {DateTimeZ} | 2022-01-06 08:07:09 EST | ")
    __properties = ["pkiEzsignsignaturecustomdateID", "iEzsignsignaturecustomdateX", "iEzsignsignaturecustomdateY", "sEzsignsignaturecustomdateFormat"]

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
    def from_json(cls, json_str: str) -> EzsignsignaturecustomdateResponseCompound:
        """Create an instance of EzsignsignaturecustomdateResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignaturecustomdateResponseCompound:
        """Create an instance of EzsignsignaturecustomdateResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignaturecustomdateResponseCompound.parse_obj(obj)

        _obj = EzsignsignaturecustomdateResponseCompound.parse_obj({
            "pki_ezsignsignaturecustomdate_id": obj.get("pkiEzsignsignaturecustomdateID"),
            "i_ezsignsignaturecustomdate_x": obj.get("iEzsignsignaturecustomdateX"),
            "i_ezsignsignaturecustomdate_y": obj.get("iEzsignsignaturecustomdateY"),
            "s_ezsignsignaturecustomdate_format": obj.get("sEzsignsignaturecustomdateFormat")
        })
        return _obj


