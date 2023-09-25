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


from typing import List
from pydantic import BaseModel, Field, conlist
from eZmaxApi.models.webhook_request_compound import WebhookRequestCompound

class WebhookCreateObjectV1Request(BaseModel):
    """
    Request for POST /1/object/webhook  # noqa: E501
    """
    a_obj_webhook: conlist(WebhookRequestCompound, min_items=1) = Field(..., alias="a_objWebhook")
    __properties = ["a_objWebhook"]

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
    def from_json(cls, json_str: str) -> WebhookCreateObjectV1Request:
        """Create an instance of WebhookCreateObjectV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_webhook (list)
        _items = []
        if self.a_obj_webhook:
            for _item in self.a_obj_webhook:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objWebhook'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookCreateObjectV1Request:
        """Create an instance of WebhookCreateObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookCreateObjectV1Request.parse_obj(obj)

        _obj = WebhookCreateObjectV1Request.parse_obj({
            "a_obj_webhook": [WebhookRequestCompound.from_dict(_item) for _item in obj.get("a_objWebhook")] if obj.get("a_objWebhook") is not None else None
        })
        return _obj


