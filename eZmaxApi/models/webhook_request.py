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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint
from eZmaxApi.models.field_e_webhook_ezsignevent import FieldEWebhookEzsignevent
from eZmaxApi.models.field_e_webhook_managementevent import FieldEWebhookManagementevent
from eZmaxApi.models.field_e_webhook_module import FieldEWebhookModule

class WebhookRequest(BaseModel):
    """
    A Webhook Object  # noqa: E501
    """
    pki_webhook_id: Optional[StrictInt] = Field(None, alias="pkiWebhookID", description="The unique ID of the Webhook")
    fki_ezsignfoldertype_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsignfoldertypeID", description="The unique ID of the Ezsignfoldertype.")
    s_webhook_description: StrictStr = Field(..., alias="sWebhookDescription", description="The description of the Webhook")
    e_webhook_module: FieldEWebhookModule = Field(..., alias="eWebhookModule")
    e_webhook_ezsignevent: Optional[FieldEWebhookEzsignevent] = Field(None, alias="eWebhookEzsignevent")
    e_webhook_managementevent: Optional[FieldEWebhookManagementevent] = Field(None, alias="eWebhookManagementevent")
    s_webhook_url: StrictStr = Field(..., alias="sWebhookUrl", description="The URL of the Webhook callback")
    s_webhook_emailfailed: StrictStr = Field(..., alias="sWebhookEmailfailed", description="The email that will receive the Webhook in case all attempts fail")
    b_webhook_isactive: StrictBool = Field(..., alias="bWebhookIsactive", description="Whether the Webhook is active or not")
    b_webhook_skipsslvalidation: StrictBool = Field(..., alias="bWebhookSkipsslvalidation", description="Wheter the server's SSL certificate should be validated or not. Not recommended to skip for production use")
    __properties = ["pkiWebhookID", "fkiEzsignfoldertypeID", "sWebhookDescription", "eWebhookModule", "eWebhookEzsignevent", "eWebhookManagementevent", "sWebhookUrl", "sWebhookEmailfailed", "bWebhookIsactive", "bWebhookSkipsslvalidation"]

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
    def from_json(cls, json_str: str) -> WebhookRequest:
        """Create an instance of WebhookRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookRequest:
        """Create an instance of WebhookRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookRequest.parse_obj(obj)

        _obj = WebhookRequest.parse_obj({
            "pki_webhook_id": obj.get("pkiWebhookID"),
            "fki_ezsignfoldertype_id": obj.get("fkiEzsignfoldertypeID"),
            "s_webhook_description": obj.get("sWebhookDescription"),
            "e_webhook_module": obj.get("eWebhookModule"),
            "e_webhook_ezsignevent": obj.get("eWebhookEzsignevent"),
            "e_webhook_managementevent": obj.get("eWebhookManagementevent"),
            "s_webhook_url": obj.get("sWebhookUrl"),
            "s_webhook_emailfailed": obj.get("sWebhookEmailfailed"),
            "b_webhook_isactive": obj.get("bWebhookIsactive"),
            "b_webhook_skipsslvalidation": obj.get("bWebhookSkipsslvalidation")
        })
        return _obj


