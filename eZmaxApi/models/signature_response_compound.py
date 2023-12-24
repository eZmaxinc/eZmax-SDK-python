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
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SignatureResponseCompound(BaseModel):
    """
    A Signature Object
    """ # noqa: E501
    pki_signature_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Signature", alias="pkiSignatureID")
    s_signature_url: Annotated[str, Field(strict=True)] = Field(description="The URL of the SVG file for the Signature", alias="sSignatureUrl")
    __properties: ClassVar[List[str]] = ["pkiSignatureID", "sSignatureUrl"]

    @field_validator('s_signature_url')
    def s_signature_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,2048}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,2048}$/")
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SignatureResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSignatureID": obj.get("pkiSignatureID"),
            "sSignatureUrl": obj.get("sSignatureUrl")
        })
        return _obj


