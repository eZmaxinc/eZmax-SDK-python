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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_file import CommonFile
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignatureSignV1Request(BaseModel):
    """
    Request for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign
    """ # noqa: E501
    fki_ezsignsigningreason_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignsigningreason", alias="fkiEzsignsigningreasonID")
    fki_font_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Font", alias="fkiFontID")
    s_value: Optional[StrictStr] = Field(default=None, description="The value required for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **City**, **FieldText** or **FieldTextarea**", alias="sValue")
    e_attachments_confirmation_decision: Optional[StrictStr] = Field(default=None, description="Whether the attachment are accepted or refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation**", alias="eAttachmentsConfirmationDecision")
    s_attachments_refusal_reason: Optional[StrictStr] = Field(default=None, description="The reason of refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation**", alias="sAttachmentsRefusalReason")
    s_svg: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The SVG of the signature.  This can only be set if eEzsignsignatureType is **Signature**/**Initials** and **bIsAutomatic** is false", alias="sSvg")
    a_obj_file: Optional[List[CommonFile]] = Field(default=None, alias="a_objFile")
    b_is_automatic: StrictBool = Field(description="Indicates if the Ezsignsignature was part of an automatic process or not.  This can only be true if eEzsignsignatureType is **Acknowledgement**, **City**, **Signature**, **Initials** or **Stamp**. ", alias="bIsAutomatic")
    __properties: ClassVar[List[str]] = ["fkiEzsignsigningreasonID", "fkiFontID", "sValue", "eAttachmentsConfirmationDecision", "sAttachmentsRefusalReason", "sSvg", "a_objFile", "bIsAutomatic"]

    @field_validator('e_attachments_confirmation_decision')
    def e_attachments_confirmation_decision_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Refused']):
            raise ValueError("must be one of enum values ('Accepted', 'Refused')")
        return value

    @field_validator('s_svg')
    def s_svg_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,65535}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,65535}$/")
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
        """Create an instance of EzsignsignatureSignV1Request from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_file (list)
        _items = []
        if self.a_obj_file:
            for _item_a_obj_file in self.a_obj_file:
                if _item_a_obj_file:
                    _items.append(_item_a_obj_file.to_dict())
            _dict['a_objFile'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignatureSignV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiEzsignsigningreasonID": obj.get("fkiEzsignsigningreasonID"),
            "fkiFontID": obj.get("fkiFontID"),
            "sValue": obj.get("sValue"),
            "eAttachmentsConfirmationDecision": obj.get("eAttachmentsConfirmationDecision"),
            "sAttachmentsRefusalReason": obj.get("sAttachmentsRefusalReason"),
            "sSvg": obj.get("sSvg"),
            "a_objFile": [CommonFile.from_dict(_item) for _item in obj["a_objFile"]] if obj.get("a_objFile") is not None else None,
            "bIsAutomatic": obj.get("bIsAutomatic")
        })
        return _obj


