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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SignatureResponseCompound(BaseModel):
    """
    A Signature Object
    """ # noqa: E501
    pki_signature_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Signature", alias="pkiSignatureID")
    fki_font_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Font", alias="fkiFontID")
    s_signature_url: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The URL of the SVG file for the Signature", alias="sSignatureUrl")
    s_signature_urlinitials: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The URL of the SVG file for the Initials", alias="sSignatureUrlinitials")
    __properties: ClassVar[List[str]] = ["pkiSignatureID", "fkiFontID", "sSignatureUrl", "sSignatureUrlinitials"]

    @field_validator('s_signature_url')
    def s_signature_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(https|http):\/\/[^\s\/$.?#].[^\s]*$", value):
            raise ValueError(r"must validate the regular expression /^(https|http):\/\/[^\s\/$.?#].[^\s]*$/")
        return value

    @field_validator('s_signature_urlinitials')
    def s_signature_urlinitials_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(https|http):\/\/[^\s\/$.?#].[^\s]*$", value):
            raise ValueError(r"must validate the regular expression /^(https|http):\/\/[^\s\/$.?#].[^\s]*$/")
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
        """Create an instance of SignatureResponseCompound from a JSON string"""
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
        """Create an instance of SignatureResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSignatureID": obj.get("pkiSignatureID"),
            "fkiFontID": obj.get("fkiFontID"),
            "sSignatureUrl": obj.get("sSignatureUrl"),
            "sSignatureUrlinitials": obj.get("sSignatureUrlinitials")
        })
        return _obj


