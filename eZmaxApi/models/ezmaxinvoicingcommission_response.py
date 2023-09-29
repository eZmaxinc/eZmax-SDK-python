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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, constr, validator

class EzmaxinvoicingcommissionResponse(BaseModel):
    """
    A Ezmaxinvoicingcommission Object  # noqa: E501
    """
    pki_ezmaxinvoicingcommission_id: Optional[StrictInt] = Field(None, alias="pkiEzmaxinvoicingcommissionID", description="The unique ID of the Ezmaxinvoicingcommission")
    fki_ezmaxinvoicingsummaryglobal_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzmaxinvoicingsummaryglobalID", description="The unique ID of the Ezmaxinvoicingsummaryglobal")
    fki_ezmaxpartner_id: Optional[conint(strict=True, ge=1)] = Field(None, alias="fkiEzmaxpartnerID", description="The unique ID of the Ezmaxpartner")
    fki_ezmaxrepresentative_id: Optional[conint(strict=True, ge=1)] = Field(None, alias="fkiEzmaxrepresentativeID", description="The unique ID of the Ezmaxrepresentative")
    dt_ezmaxinvoicingcommission_start: StrictStr = Field(..., alias="dtEzmaxinvoicingcommissionStart", description="The start date for the Ezmaxinvoicingcommission")
    dt_ezmaxinvoicingcommission_end: StrictStr = Field(..., alias="dtEzmaxinvoicingcommissionEnd", description="The end date for the Ezmaxinvoicingcommission")
    i_ezmaxinvoicingcommission_days: conint(strict=True, ge=0) = Field(..., alias="iEzmaxinvoicingcommissionDays", description="This is the number of days during the month on which the Ezmaxinvoigcommission applies")
    d_ezmaxinvoicingcommission_amount: constr(strict=True) = Field(..., alias="dEzmaxinvoicingcommissionAmount", description="The amount of Ezmaxinvoicingcommission")
    __properties = ["pkiEzmaxinvoicingcommissionID", "fkiEzmaxinvoicingsummaryglobalID", "fkiEzmaxpartnerID", "fkiEzmaxrepresentativeID", "dtEzmaxinvoicingcommissionStart", "dtEzmaxinvoicingcommissionEnd", "iEzmaxinvoicingcommissionDays", "dEzmaxinvoicingcommissionAmount"]

    @validator('d_ezmaxinvoicingcommission_amount')
    def d_ezmaxinvoicingcommission_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
        return value

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
    def from_json(cls, json_str: str) -> EzmaxinvoicingcommissionResponse:
        """Create an instance of EzmaxinvoicingcommissionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzmaxinvoicingcommissionResponse:
        """Create an instance of EzmaxinvoicingcommissionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzmaxinvoicingcommissionResponse.parse_obj(obj)

        _obj = EzmaxinvoicingcommissionResponse.parse_obj({
            "pki_ezmaxinvoicingcommission_id": obj.get("pkiEzmaxinvoicingcommissionID"),
            "fki_ezmaxinvoicingsummaryglobal_id": obj.get("fkiEzmaxinvoicingsummaryglobalID"),
            "fki_ezmaxpartner_id": obj.get("fkiEzmaxpartnerID"),
            "fki_ezmaxrepresentative_id": obj.get("fkiEzmaxrepresentativeID"),
            "dt_ezmaxinvoicingcommission_start": obj.get("dtEzmaxinvoicingcommissionStart"),
            "dt_ezmaxinvoicingcommission_end": obj.get("dtEzmaxinvoicingcommissionEnd"),
            "i_ezmaxinvoicingcommission_days": obj.get("iEzmaxinvoicingcommissionDays"),
            "d_ezmaxinvoicingcommission_amount": obj.get("dEzmaxinvoicingcommissionAmount")
        })
        return _obj

