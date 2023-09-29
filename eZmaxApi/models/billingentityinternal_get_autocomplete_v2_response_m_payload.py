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
from eZmaxApi.models.billingentityinternal_autocomplete_element_response import BillingentityinternalAutocompleteElementResponse

class BillingentityinternalGetAutocompleteV2ResponseMPayload(BaseModel):
    """
    Payload for POST /2/object/billingentityinternal/getAutocomplete  # noqa: E501
    """
    a_obj_billingentityinternal: conlist(BillingentityinternalAutocompleteElementResponse) = Field(..., alias="a_objBillingentityinternal", description="An array of Billingentityinternal object containing the description, ID and active status about the element.")
    __properties = ["a_objBillingentityinternal"]

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
    def from_json(cls, json_str: str) -> BillingentityinternalGetAutocompleteV2ResponseMPayload:
        """Create an instance of BillingentityinternalGetAutocompleteV2ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_billingentityinternal (list)
        _items = []
        if self.a_obj_billingentityinternal:
            for _item in self.a_obj_billingentityinternal:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objBillingentityinternal'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingentityinternalGetAutocompleteV2ResponseMPayload:
        """Create an instance of BillingentityinternalGetAutocompleteV2ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingentityinternalGetAutocompleteV2ResponseMPayload.parse_obj(obj)

        _obj = BillingentityinternalGetAutocompleteV2ResponseMPayload.parse_obj({
            "a_obj_billingentityinternal": [BillingentityinternalAutocompleteElementResponse.from_dict(_item) for _item in obj.get("a_objBillingentityinternal")] if obj.get("a_objBillingentityinternal") is not None else None
        })
        return _obj

