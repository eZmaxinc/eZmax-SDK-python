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

class EzmaxproductAutocompleteElementResponse(BaseModel):
    """
    A Ezmaxproduct AutocompleteElement Response  # noqa: E501
    """
    pki_ezmaxproduct_id: conint(strict=True, ge=1) = Field(..., alias="pkiEzmaxproductID", description="The unique ID of the Ezmaxproduct")
    s_ezmaxproduct_description_x: StrictStr = Field(..., alias="sEzmaxproductDescriptionX", description="The description of the Ezmaxproduct in the language of the requester")
    b_ezmaxproduct_isactive: StrictBool = Field(..., alias="bEzmaxproductIsactive", description="Whether the Ezmaxproduct is active or not")
    __properties = ["pkiEzmaxproductID", "sEzmaxproductDescriptionX", "bEzmaxproductIsactive"]

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
    def from_json(cls, json_str: str) -> EzmaxproductAutocompleteElementResponse:
        """Create an instance of EzmaxproductAutocompleteElementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzmaxproductAutocompleteElementResponse:
        """Create an instance of EzmaxproductAutocompleteElementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzmaxproductAutocompleteElementResponse.parse_obj(obj)

        _obj = EzmaxproductAutocompleteElementResponse.parse_obj({
            "pki_ezmaxproduct_id": obj.get("pkiEzmaxproductID"),
            "s_ezmaxproduct_description_x": obj.get("sEzmaxproductDescriptionX"),
            "b_ezmaxproduct_isactive": obj.get("bEzmaxproductIsactive")
        })
        return _obj


