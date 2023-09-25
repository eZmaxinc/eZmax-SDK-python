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
from pydantic import BaseModel, Field, StrictBool, conint, constr, validator
from eZmaxApi.models.field_e_variableexpense_taxable import FieldEVariableexpenseTaxable
from eZmaxApi.models.multilingual_variableexpense_description import MultilingualVariableexpenseDescription

class VariableexpenseRequest(BaseModel):
    """
    A Variableexpense Object  # noqa: E501
    """
    pki_variableexpense_id: Optional[conint(strict=True, le=255, ge=1)] = Field(None, alias="pkiVariableexpenseID", description="The unique ID of the Variableexpense")
    s_variableexpense_code: constr(strict=True) = Field(..., alias="sVariableexpenseCode", description="The code of the Variableexpense")
    obj_variableexpense_description: MultilingualVariableexpenseDescription = Field(..., alias="objVariableexpenseDescription")
    e_variableexpense_taxable: FieldEVariableexpenseTaxable = Field(..., alias="eVariableexpenseTaxable")
    b_variableexpense_isactive: StrictBool = Field(..., alias="bVariableexpenseIsactive", description="Whether the variableexpense is active or not")
    __properties = ["pkiVariableexpenseID", "sVariableexpenseCode", "objVariableexpenseDescription", "eVariableexpenseTaxable", "bVariableexpenseIsactive"]

    @validator('s_variableexpense_code')
    def s_variableexpense_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,5}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,5}$/")
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
    def from_json(cls, json_str: str) -> VariableexpenseRequest:
        """Create an instance of VariableexpenseRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_variableexpense_description
        if self.obj_variableexpense_description:
            _dict['objVariableexpenseDescription'] = self.obj_variableexpense_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VariableexpenseRequest:
        """Create an instance of VariableexpenseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VariableexpenseRequest.parse_obj(obj)

        _obj = VariableexpenseRequest.parse_obj({
            "pki_variableexpense_id": obj.get("pkiVariableexpenseID"),
            "s_variableexpense_code": obj.get("sVariableexpenseCode"),
            "obj_variableexpense_description": MultilingualVariableexpenseDescription.from_dict(obj.get("objVariableexpenseDescription")) if obj.get("objVariableexpenseDescription") is not None else None,
            "e_variableexpense_taxable": obj.get("eVariableexpenseTaxable"),
            "b_variableexpense_isactive": obj.get("bVariableexpenseIsactive")
        })
        return _obj


