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
from pydantic import BaseModel, Field, conint, conlist
from eZmaxApi.models.billingentityinternalproduct_request_compound import BillingentityinternalproductRequestCompound
from eZmaxApi.models.multilingual_billingentityinternal_description import MultilingualBillingentityinternalDescription

class BillingentityinternalRequestCompound(BaseModel):
    """
    A Billingentityinternal Object and children  # noqa: E501
    """
    pki_billingentityinternal_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiBillingentityinternalID", description="The unique ID of the Billingentityinternal.")
    obj_billingentityinternal_description: MultilingualBillingentityinternalDescription = Field(..., alias="objBillingentityinternalDescription")
    a_obj_billingentityinternalproduct: conlist(BillingentityinternalproductRequestCompound) = Field(..., alias="a_objBillingentityinternalproduct")
    __properties = ["pkiBillingentityinternalID", "objBillingentityinternalDescription", "a_objBillingentityinternalproduct"]

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
    def from_json(cls, json_str: str) -> BillingentityinternalRequestCompound:
        """Create an instance of BillingentityinternalRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_billingentityinternalproduct (list)
        _items = []
        if self.a_obj_billingentityinternalproduct:
            for _item in self.a_obj_billingentityinternalproduct:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objBillingentityinternalproduct'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingentityinternalRequestCompound:
        """Create an instance of BillingentityinternalRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingentityinternalRequestCompound.parse_obj(obj)

        _obj = BillingentityinternalRequestCompound.parse_obj({
            "pki_billingentityinternal_id": obj.get("pkiBillingentityinternalID"),
            "obj_billingentityinternal_description": MultilingualBillingentityinternalDescription.from_dict(obj.get("objBillingentityinternalDescription")) if obj.get("objBillingentityinternalDescription") is not None else None,
            "a_obj_billingentityinternalproduct": [BillingentityinternalproductRequestCompound.from_dict(_item) for _item in obj.get("a_objBillingentityinternalproduct")] if obj.get("a_objBillingentityinternalproduct") is not None else None
        })
        return _obj


