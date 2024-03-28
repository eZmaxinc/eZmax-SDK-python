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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class WebhookheaderRequest(BaseModel):
    """
    A webhookheader object
    """ # noqa: E501
    pki_webhookheader_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the Webhookheader", alias="pkiWebhookheaderID")
    s_webhookheader_name: Annotated[str, Field(strict=True)] = Field(description="The Name of the Webhookheader", alias="sWebhookheaderName")
    s_webhookheader_value: Annotated[str, Field(strict=True)] = Field(description="The Value of the Webhookheader", alias="sWebhookheaderValue")
    __properties: ClassVar[List[str]] = ["pkiWebhookheaderID", "sWebhookheaderName", "sWebhookheaderValue"]

    @field_validator('s_webhookheader_name')
    def s_webhookheader_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?!(?:e|E)(?:z|Z)(?:m|M)(?:a|A)(?:x|X))(?!(?:h|H)(?:o|O)(?:s|S)(?:t|T)$|(?:u|U)(?:s|S)(?:e|E)(?:r|R)-(?:a|A)(?:g|G)(?:e|E)(?:n|N)(?:t|T)$)(?!\s)[^\s].*$", value):
            raise ValueError(r"must validate the regular expression /^(?!(?:e|E)(?:z|Z)(?:m|M)(?:a|A)(?:x|X))(?!(?:h|H)(?:o|O)(?:s|S)(?:t|T)$|(?:u|U)(?:s|S)(?:e|E)(?:r|R)-(?:a|A)(?:g|G)(?:e|E)(?:n|N)(?:t|T)$)(?!\s)[^\s].*$/")
        return value

    @field_validator('s_webhookheader_value')
    def s_webhookheader_value_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,255}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,255}$/")
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
        """Create an instance of WebhookheaderRequest from a JSON string"""
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
        """Create an instance of WebhookheaderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiWebhookheaderID": obj.get("pkiWebhookheaderID"),
            "sWebhookheaderName": obj.get("sWebhookheaderName"),
            "sWebhookheaderValue": obj.get("sWebhookheaderValue")
        })
        return _obj


