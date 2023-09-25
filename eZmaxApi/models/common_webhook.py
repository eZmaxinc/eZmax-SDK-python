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
from eZmaxApi.models.attempt_response_compound import AttemptResponseCompound
from eZmaxApi.models.custom_webhook_response import CustomWebhookResponse

class CommonWebhook(BaseModel):
    """
    This is the base Webhook object  # noqa: E501
    """
    obj_webhook: CustomWebhookResponse = Field(..., alias="objWebhook")
    a_obj_attempt: conlist(AttemptResponseCompound) = Field(..., alias="a_objAttempt", description="An array containing details of previous attempts that were made to deliver the message. The array is empty if it's the first attempt.")
    __properties = ["objWebhook", "a_objAttempt"]

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
    def from_json(cls, json_str: str) -> CommonWebhook:
        """Create an instance of CommonWebhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_webhook
        if self.obj_webhook:
            _dict['objWebhook'] = self.obj_webhook.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_attempt (list)
        _items = []
        if self.a_obj_attempt:
            for _item in self.a_obj_attempt:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objAttempt'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommonWebhook:
        """Create an instance of CommonWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommonWebhook.parse_obj(obj)

        _obj = CommonWebhook.parse_obj({
            "obj_webhook": CustomWebhookResponse.from_dict(obj.get("objWebhook")) if obj.get("objWebhook") is not None else None,
            "a_obj_attempt": [AttemptResponseCompound.from_dict(_item) for _item in obj.get("a_objAttempt")] if obj.get("a_objAttempt") is not None else None
        })
        return _obj


