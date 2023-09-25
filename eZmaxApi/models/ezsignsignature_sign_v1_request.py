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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from eZmaxApi.models.common_file import CommonFile

class EzsignsignatureSignV1Request(BaseModel):
    """
    Request for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign  # noqa: E501
    """
    s_value: Optional[StrictStr] = Field(None, alias="sValue", description="The value required for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **City**, **FieldText** or **FieldTextarea**")
    e_attachments_confirmation_decision: Optional[StrictStr] = Field(None, alias="eAttachmentsConfirmationDecision", description="Whether the attachment are accepted or refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation**")
    s_attachments_refusal_reason: Optional[StrictStr] = Field(None, alias="sAttachmentsRefusalReason", description="The reason of refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation**")
    s_svg: Optional[constr(strict=True)] = Field(None, alias="sSvg", description="The SVG of the handwritten signature.  This can only be set if eEzsignsignatureType is **Handwritten** and **bIsAutomatic** is false")
    a_obj_file: Optional[conlist(CommonFile)] = Field(None, alias="a_objFile")
    b_is_automatic: StrictBool = Field(..., alias="bIsAutomatic", description="Indicates if the Ezsignsignature was part of an automatic process or not.  This can only be true if eEzsignsignatureType is **Acknowledgement**, **City**, **Handwritten**, **Initials**, **Name** or **Stamp**. ")
    __properties = ["sValue", "eAttachmentsConfirmationDecision", "sAttachmentsRefusalReason", "sSvg", "a_objFile", "bIsAutomatic"]

    @validator('e_attachments_confirmation_decision')
    def e_attachments_confirmation_decision_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Accepted', 'Refused'):
            raise ValueError("must be one of enum values ('Accepted', 'Refused')")
        return value

    @validator('s_svg')
    def s_svg_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,32767}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,32767}$/")
        return value

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
    def from_json(cls, json_str: str) -> EzsignsignatureSignV1Request:
        """Create an instance of EzsignsignatureSignV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_file (list)
        _items = []
        if self.a_obj_file:
            for _item in self.a_obj_file:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objFile'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignatureSignV1Request:
        """Create an instance of EzsignsignatureSignV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignatureSignV1Request.parse_obj(obj)

        _obj = EzsignsignatureSignV1Request.parse_obj({
            "s_value": obj.get("sValue"),
            "e_attachments_confirmation_decision": obj.get("eAttachmentsConfirmationDecision"),
            "s_attachments_refusal_reason": obj.get("sAttachmentsRefusalReason"),
            "s_svg": obj.get("sSvg"),
            "a_obj_file": [CommonFile.from_dict(_item) for _item in obj.get("a_objFile")] if obj.get("a_objFile") is not None else None,
            "b_is_automatic": obj.get("bIsAutomatic")
        })
        return _obj


