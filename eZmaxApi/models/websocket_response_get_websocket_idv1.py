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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.websocket_response_get_websocket_idv1_m_payload import WebsocketResponseGetWebsocketIDV1MPayload
from typing import Optional, Set
from typing_extensions import Self

class WebsocketResponseGetWebsocketIDV1(BaseModel):
    """
    Response for Websocket GetWebsocketID V1
    """ # noqa: E501
    e_websocket_messagetype: StrictStr = Field(description="The Type of message", alias="eWebsocketMessagetype")
    m_payload: WebsocketResponseGetWebsocketIDV1MPayload = Field(alias="mPayload")
    __properties: ClassVar[List[str]] = ["eWebsocketMessagetype", "mPayload"]

    @field_validator('e_websocket_messagetype')
    def e_websocket_messagetype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Response-GetWebsocketID-V1']):
            raise ValueError("must be one of enum values ('Response-GetWebsocketID-V1')")
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
        """Create an instance of WebsocketResponseGetWebsocketIDV1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of m_payload
        if self.m_payload:
            _dict['mPayload'] = self.m_payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebsocketResponseGetWebsocketIDV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eWebsocketMessagetype": obj.get("eWebsocketMessagetype"),
            "mPayload": WebsocketResponseGetWebsocketIDV1MPayload.from_dict(obj["mPayload"]) if obj.get("mPayload") is not None else None
        })
        return _obj


