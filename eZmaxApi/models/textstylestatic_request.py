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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TextstylestaticRequest(BaseModel):
    """
    A Textstylestatic Object
    """ # noqa: E501
    fki_font_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Font", alias="fkiFontID")
    b_textstylestatic_bold: StrictBool = Field(description="Whether the Textstylestatic is Bold or not", alias="bTextstylestaticBold")
    b_textstylestatic_underline: StrictBool = Field(description="Whether the Textstylestatic is Underline or not", alias="bTextstylestaticUnderline")
    b_textstylestatic_italic: StrictBool = Field(description="Whether the Textstylestatic is Italic or not", alias="bTextstylestaticItalic")
    b_textstylestatic_strikethrough: StrictBool = Field(description="Whether the Textstylestatic is Strikethrough or not", alias="bTextstylestaticStrikethrough")
    i_textstylestatic_fontcolor: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The int32 representation of the Fontcolor. For example, RGB color #39435B would be 3752795", alias="iTextstylestaticFontcolor")
    i_textstylestatic_size: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The Size for the Font of the Textstylestatic", alias="iTextstylestaticSize")
    __properties: ClassVar[List[str]] = ["fkiFontID", "bTextstylestaticBold", "bTextstylestaticUnderline", "bTextstylestaticItalic", "bTextstylestaticStrikethrough", "iTextstylestaticFontcolor", "iTextstylestaticSize"]

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
        """Create an instance of TextstylestaticRequest from a JSON string"""
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
        """Create an instance of TextstylestaticRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiFontID": obj.get("fkiFontID"),
            "bTextstylestaticBold": obj.get("bTextstylestaticBold"),
            "bTextstylestaticUnderline": obj.get("bTextstylestaticUnderline"),
            "bTextstylestaticItalic": obj.get("bTextstylestaticItalic"),
            "bTextstylestaticStrikethrough": obj.get("bTextstylestaticStrikethrough"),
            "iTextstylestaticFontcolor": obj.get("iTextstylestaticFontcolor"),
            "iTextstylestaticSize": obj.get("iTextstylestaticSize")
        })
        return _obj


