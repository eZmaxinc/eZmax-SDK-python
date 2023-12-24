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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzsigntemplatedocumentpageResponseCompound(BaseModel):
    """
    An Ezsigntemplatedocumentpage Object and children to create a complete structure
    """ # noqa: E501
    pki_ezsigntemplatedocumentpage_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocumentpage", alias="pkiEzsigntemplatedocumentpageID")
    i_ezsigntemplatedocumentpage_widthimage: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Width of the page's image in pixels calculated at 100 DPI", alias="iEzsigntemplatedocumentpageWidthimage")
    i_ezsigntemplatedocumentpage_heightimage: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Height of the page's image in pixels calculated at 100 DPI", alias="iEzsigntemplatedocumentpageHeightimage")
    i_ezsigntemplatedocumentpage_widthpdf: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Width of the page in points calculated at 72 DPI", alias="iEzsigntemplatedocumentpageWidthpdf")
    i_ezsigntemplatedocumentpage_heightpdf: Annotated[int, Field(strict=True, ge=0)] = Field(description="The Height of the page in points calculated at 72 DPI", alias="iEzsigntemplatedocumentpageHeightpdf")
    i_ezsigntemplatedocumentpage_pagenumber: Annotated[int, Field(strict=True, ge=1)] = Field(description="The page number in the Ezsigntemplatedocument", alias="iEzsigntemplatedocumentpagePagenumber")
    s_computed_imageurl: StrictStr = Field(description="The Url to the Ezsigntemplatedocumentpage's rasterized image.  Url will expire after 5 minutes.", alias="sComputedImageurl")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatedocumentpageID", "iEzsigntemplatedocumentpageWidthimage", "iEzsigntemplatedocumentpageHeightimage", "iEzsigntemplatedocumentpageWidthpdf", "iEzsigntemplatedocumentpageHeightpdf", "iEzsigntemplatedocumentpagePagenumber", "sComputedImageurl"]

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
        """Create an instance of EzsigntemplatedocumentpageResponseCompound from a JSON string"""
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
        """Create an instance of EzsigntemplatedocumentpageResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatedocumentpageID": obj.get("pkiEzsigntemplatedocumentpageID"),
            "iEzsigntemplatedocumentpageWidthimage": obj.get("iEzsigntemplatedocumentpageWidthimage"),
            "iEzsigntemplatedocumentpageHeightimage": obj.get("iEzsigntemplatedocumentpageHeightimage"),
            "iEzsigntemplatedocumentpageWidthpdf": obj.get("iEzsigntemplatedocumentpageWidthpdf"),
            "iEzsigntemplatedocumentpageHeightpdf": obj.get("iEzsigntemplatedocumentpageHeightpdf"),
            "iEzsigntemplatedocumentpagePagenumber": obj.get("iEzsigntemplatedocumentpagePagenumber"),
            "sComputedImageurl": obj.get("sComputedImageurl")
        })
        return _obj


