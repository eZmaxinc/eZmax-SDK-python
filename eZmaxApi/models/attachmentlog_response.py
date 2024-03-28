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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_attachmentlog_type import FieldEAttachmentlogType
from typing import Optional, Set
from typing_extensions import Self

class AttachmentlogResponse(BaseModel):
    """
    An Attachmentlog Object
    """ # noqa: E501
    fki_attachment_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Attachment.", alias="fkiAttachmentID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    dt_attachmentlog_datetime: Annotated[str, Field(strict=True)] = Field(description="The created date", alias="dtAttachmentlogDatetime")
    e_attachmentlog_type: FieldEAttachmentlogType = Field(alias="eAttachmentlogType")
    s_attachmentlog_detail: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The additionnal detail", alias="sAttachmentlogDetail")
    __properties: ClassVar[List[str]] = ["fkiAttachmentID", "fkiUserID", "dtAttachmentlogDatetime", "eAttachmentlogType", "sAttachmentlogDetail"]

    @field_validator('dt_attachmentlog_datetime')
    def dt_attachmentlog_datetime_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('s_attachmentlog_detail')
    def s_attachmentlog_detail_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,75}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,75}$/")
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
        """Create an instance of AttachmentlogResponse from a JSON string"""
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
        """Create an instance of AttachmentlogResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiAttachmentID": obj.get("fkiAttachmentID"),
            "fkiUserID": obj.get("fkiUserID"),
            "dtAttachmentlogDatetime": obj.get("dtAttachmentlogDatetime"),
            "eAttachmentlogType": obj.get("eAttachmentlogType"),
            "sAttachmentlogDetail": obj.get("sAttachmentlogDetail")
        })
        return _obj


