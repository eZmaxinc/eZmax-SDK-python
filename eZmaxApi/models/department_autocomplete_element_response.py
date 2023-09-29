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

class DepartmentAutocompleteElementResponse(BaseModel):
    """
    A Department AutocompleteElement Response  # noqa: E501
    """
    s_company_name_x: StrictStr = Field(..., alias="sCompanyNameX", description="The Name of the Company in the language of the requester")
    s_department_name_x: StrictStr = Field(..., alias="sDepartmentNameX", description="The Name of the Department in the language of the requester")
    pki_department_id: conint(strict=True, ge=0) = Field(..., alias="pkiDepartmentID", description="The unique ID of the Department")
    b_department_isactive: StrictBool = Field(..., alias="bDepartmentIsactive", description="Whether the Department is active or not")
    __properties = ["sCompanyNameX", "sDepartmentNameX", "pkiDepartmentID", "bDepartmentIsactive"]

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
    def from_json(cls, json_str: str) -> DepartmentAutocompleteElementResponse:
        """Create an instance of DepartmentAutocompleteElementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DepartmentAutocompleteElementResponse:
        """Create an instance of DepartmentAutocompleteElementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DepartmentAutocompleteElementResponse.parse_obj(obj)

        _obj = DepartmentAutocompleteElementResponse.parse_obj({
            "s_company_name_x": obj.get("sCompanyNameX"),
            "s_department_name_x": obj.get("sDepartmentNameX"),
            "pki_department_id": obj.get("pkiDepartmentID"),
            "b_department_isactive": obj.get("bDepartmentIsactive")
        })
        return _obj

