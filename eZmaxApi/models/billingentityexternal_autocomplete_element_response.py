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



from pydantic import BaseModel, Field, StrictBool, StrictStr, conint

class BillingentityexternalAutocompleteElementResponse(BaseModel):
    """
    A Billingentityexternal AutocompleteElement Response  # noqa: E501
    """
    pki_billingentityexternal_id: conint(strict=True, ge=1) = Field(..., alias="pkiBillingentityexternalID", description="The unique ID of the Billingentityexternal")
    s_billingentityexternal_description: StrictStr = Field(..., alias="sBillingentityexternalDescription", description="The description of the Billingentityexternal")
    b_billingentityexternal_isactive: StrictBool = Field(..., alias="bBillingentityexternalIsactive", description="Whether the Billingentityexternal is active or not")
    __properties = ["pkiBillingentityexternalID", "sBillingentityexternalDescription", "bBillingentityexternalIsactive"]

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
    def from_json(cls, json_str: str) -> BillingentityexternalAutocompleteElementResponse:
        """Create an instance of BillingentityexternalAutocompleteElementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingentityexternalAutocompleteElementResponse:
        """Create an instance of BillingentityexternalAutocompleteElementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingentityexternalAutocompleteElementResponse.parse_obj(obj)

        _obj = BillingentityexternalAutocompleteElementResponse.parse_obj({
            "pki_billingentityexternal_id": obj.get("pkiBillingentityexternalID"),
            "s_billingentityexternal_description": obj.get("sBillingentityexternalDescription"),
            "b_billingentityexternal_isactive": obj.get("bBillingentityexternalIsactive")
        })
        return _obj


