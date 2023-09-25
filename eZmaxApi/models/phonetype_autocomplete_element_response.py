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



from pydantic import BaseModel, Field, StrictBool, conint, constr, validator

class PhonetypeAutocompleteElementResponse(BaseModel):
    """
    A Phonetype AutocompleteElement Response  # noqa: E501
    """
    pki_phonetype_id: conint(strict=True, ge=0) = Field(..., alias="pkiPhonetypeID", description="The unique ID of the Phonetype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Mobile| |4|Fax| |5|Pager| |6|Toll Free|")
    s_phonetype_name_x: constr(strict=True) = Field(..., alias="sPhonetypeNameX", description="The name of the Phonetype in the language of the requester")
    b_phonetype_isactive: StrictBool = Field(..., alias="bPhonetypeIsactive", description="Whether the Phonetype is active or not")
    __properties = ["pkiPhonetypeID", "sPhonetypeNameX", "bPhonetypeIsactive"]

    @validator('s_phonetype_name_x')
    def s_phonetype_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,20}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,20}$/")
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
    def from_json(cls, json_str: str) -> PhonetypeAutocompleteElementResponse:
        """Create an instance of PhonetypeAutocompleteElementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PhonetypeAutocompleteElementResponse:
        """Create an instance of PhonetypeAutocompleteElementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PhonetypeAutocompleteElementResponse.parse_obj(obj)

        _obj = PhonetypeAutocompleteElementResponse.parse_obj({
            "pki_phonetype_id": obj.get("pkiPhonetypeID"),
            "s_phonetype_name_x": obj.get("sPhonetypeNameX"),
            "b_phonetype_isactive": obj.get("bPhonetypeIsactive")
        })
        return _obj


