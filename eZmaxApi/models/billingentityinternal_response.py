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



from pydantic import BaseModel, Field, conint
from eZmaxApi.models.multilingual_billingentityinternal_description import MultilingualBillingentityinternalDescription

class BillingentityinternalResponse(BaseModel):
    """
    A Billingentityinternal Object  # noqa: E501
    """
    pki_billingentityinternal_id: conint(strict=True, ge=0) = Field(..., alias="pkiBillingentityinternalID", description="The unique ID of the Billingentityinternal.")
    obj_billingentityinternal_description: MultilingualBillingentityinternalDescription = Field(..., alias="objBillingentityinternalDescription")
    __properties = ["pkiBillingentityinternalID", "objBillingentityinternalDescription"]

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
    def from_json(cls, json_str: str) -> BillingentityinternalResponse:
        """Create an instance of BillingentityinternalResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_billingentityinternal_description
        if self.obj_billingentityinternal_description:
            _dict['objBillingentityinternalDescription'] = self.obj_billingentityinternal_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingentityinternalResponse:
        """Create an instance of BillingentityinternalResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingentityinternalResponse.parse_obj(obj)

        _obj = BillingentityinternalResponse.parse_obj({
            "pki_billingentityinternal_id": obj.get("pkiBillingentityinternalID"),
            "obj_billingentityinternal_description": MultilingualBillingentityinternalDescription.from_dict(obj.get("objBillingentityinternalDescription")) if obj.get("objBillingentityinternalDescription") is not None else None
        })
        return _obj

