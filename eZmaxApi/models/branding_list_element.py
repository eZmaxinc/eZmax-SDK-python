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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BrandingListElement(BaseModel):
    """
    A Branding List Element
    """ # noqa: E501
    pki_branding_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Branding", alias="pkiBrandingID")
    s_branding_description_x: StrictStr = Field(description="The Description of the Branding in the language of the requester", alias="sBrandingDescriptionX")
    i_branding_colortext: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the text. This is a RGB color converted into integer", alias="iBrandingColortext")
    i_branding_colortextlinkbox: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the text in the link box. This is a RGB color converted into integer", alias="iBrandingColortextlinkbox")
    i_branding_colortextbutton: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the text in the button. This is a RGB color converted into integer", alias="iBrandingColortextbutton")
    i_branding_colorbackground: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the background. This is a RGB color converted into integer", alias="iBrandingColorbackground")
    i_branding_colorbackgroundbutton: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the background of the button. This is a RGB color converted into integer", alias="iBrandingColorbackgroundbutton")
    i_branding_colorbackgroundsmallbox: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The color of the background of the small box. This is a RGB color converted into integer", alias="iBrandingColorbackgroundsmallbox")
    b_branding_isactive: StrictBool = Field(description="Whether the Branding is active or not", alias="bBrandingIsactive")
    __properties: ClassVar[List[str]] = ["pkiBrandingID", "sBrandingDescriptionX", "iBrandingColortext", "iBrandingColortextlinkbox", "iBrandingColortextbutton", "iBrandingColorbackground", "iBrandingColorbackgroundbutton", "iBrandingColorbackgroundsmallbox", "bBrandingIsactive"]

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
        """Create an instance of BrandingListElement from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BrandingListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiBrandingID": obj.get("pkiBrandingID"),
            "sBrandingDescriptionX": obj.get("sBrandingDescriptionX"),
            "iBrandingColortext": obj.get("iBrandingColortext"),
            "iBrandingColortextlinkbox": obj.get("iBrandingColortextlinkbox"),
            "iBrandingColortextbutton": obj.get("iBrandingColortextbutton"),
            "iBrandingColorbackground": obj.get("iBrandingColorbackground"),
            "iBrandingColorbackgroundbutton": obj.get("iBrandingColorbackgroundbutton"),
            "iBrandingColorbackgroundsmallbox": obj.get("iBrandingColorbackgroundsmallbox"),
            "bBrandingIsactive": obj.get("bBrandingIsactive")
        })
        return _obj


