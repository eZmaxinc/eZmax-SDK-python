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



from pydantic import BaseModel, Field, StrictStr

class WebsocketResponseInformationV1MPayload(BaseModel):
    """
    Payload for Websocket Information V1  # noqa: E501
    """
    s_information_message: StrictStr = Field(..., alias="sInformationMessage", description="Information message")
    __properties = ["sInformationMessage"]

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
    def from_json(cls, json_str: str) -> WebsocketResponseInformationV1MPayload:
        """Create an instance of WebsocketResponseInformationV1MPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebsocketResponseInformationV1MPayload:
        """Create an instance of WebsocketResponseInformationV1MPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebsocketResponseInformationV1MPayload.parse_obj(obj)

        _obj = WebsocketResponseInformationV1MPayload.parse_obj({
            "s_information_message": obj.get("sInformationMessage")
        })
        return _obj


