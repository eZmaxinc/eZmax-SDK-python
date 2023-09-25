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
from pydantic import BaseModel, Field, StrictStr, conint, constr

class EzmaxinvoicingsummaryexternalResponse(BaseModel):
    """
    A Ezmaxinvoicingsummaryexternal Object  # noqa: E501
    """
    pki_ezmaxinvoicingsummaryexternal_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzmaxinvoicingsummaryexternalID", description="The unique ID of the Ezmaxinvoicingsummaryexternal")
    fki_ezmaxinvoicing_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzmaxinvoicingID", description="The unique ID of the Ezmaxinvoicing")
    fki_billingentityexternal_id: conint(strict=True, ge=1) = Field(..., alias="fkiBillingentityexternalID", description="The unique ID of the Billingentityexternal")
    s_billingentityexternal_description: StrictStr = Field(..., alias="sBillingentityexternalDescription", description="The description of the Billingentityexternal")
    s_ezmaxinvoicingsummaryexternal_description: constr(strict=True, max_length=70) = Field(..., alias="sEzmaxinvoicingsummaryexternalDescription", description="The description of the Ezmaxinvoicingsummaryexternal")
    __properties = ["pkiEzmaxinvoicingsummaryexternalID", "fkiEzmaxinvoicingID", "fkiBillingentityexternalID", "sBillingentityexternalDescription", "sEzmaxinvoicingsummaryexternalDescription"]

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
    def from_json(cls, json_str: str) -> EzmaxinvoicingsummaryexternalResponse:
        """Create an instance of EzmaxinvoicingsummaryexternalResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzmaxinvoicingsummaryexternalResponse:
        """Create an instance of EzmaxinvoicingsummaryexternalResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzmaxinvoicingsummaryexternalResponse.parse_obj(obj)

        _obj = EzmaxinvoicingsummaryexternalResponse.parse_obj({
            "pki_ezmaxinvoicingsummaryexternal_id": obj.get("pkiEzmaxinvoicingsummaryexternalID"),
            "fki_ezmaxinvoicing_id": obj.get("fkiEzmaxinvoicingID"),
            "fki_billingentityexternal_id": obj.get("fkiBillingentityexternalID"),
            "s_billingentityexternal_description": obj.get("sBillingentityexternalDescription"),
            "s_ezmaxinvoicingsummaryexternal_description": obj.get("sEzmaxinvoicingsummaryexternalDescription")
        })
        return _obj


