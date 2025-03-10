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
from eZmaxApi.models.field_e_signature_preference import FieldESignaturePreference
from typing import Optional, Set
from typing_extensions import Self

class SignatureRequest(BaseModel):
    """
    A Signature Object
    """ # noqa: E501
    pki_signature_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Signature", alias="pkiSignatureID")
    fki_font_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Font", alias="fkiFontID")
    e_signature_preference: FieldESignaturePreference = Field(alias="eSignaturePreference")
    t_signature_svg: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The svg of the Signature", alias="tSignatureSvg")
    t_signature_svginitials: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The svg of the Initials", alias="tSignatureSvginitials")
    __properties: ClassVar[List[str]] = ["pkiSignatureID", "fkiFontID", "eSignaturePreference", "tSignatureSvg", "tSignatureSvginitials"]

    @field_validator('t_signature_svg')
    def t_signature_svg_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{60,65535}$", value):
            raise ValueError(r"must validate the regular expression /^.{60,65535}$/")
        return value

    @field_validator('t_signature_svginitials')
    def t_signature_svginitials_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{60,65535}$", value):
            raise ValueError(r"must validate the regular expression /^.{60,65535}$/")
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
        """Create an instance of SignatureRequest from a JSON string"""
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
        """Create an instance of SignatureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSignatureID": obj.get("pkiSignatureID"),
            "fkiFontID": obj.get("fkiFontID"),
            "eSignaturePreference": obj.get("eSignaturePreference"),
            "tSignatureSvg": obj.get("tSignatureSvg"),
            "tSignatureSvginitials": obj.get("tSignatureSvginitials")
        })
        return _obj


