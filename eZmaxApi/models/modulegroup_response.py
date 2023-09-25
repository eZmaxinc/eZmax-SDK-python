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



from pydantic import BaseModel, Field, conint, constr, validator

class ModulegroupResponse(BaseModel):
    """
    A Modulegroup Object  # noqa: E501
    """
    pki_modulegroup_id: conint(strict=True, le=255, ge=1) = Field(..., alias="pkiModulegroupID", description="The unique ID of the Modulegroup")
    s_modulegroup_name_x: constr(strict=True) = Field(..., alias="sModulegroupNameX", description="The name of the Modulegroup in the language of the requester")
    __properties = ["pkiModulegroupID", "sModulegroupNameX"]

    @validator('s_modulegroup_name_x')
    def s_modulegroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,25}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,25}$/")
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
    def from_json(cls, json_str: str) -> ModulegroupResponse:
        """Create an instance of ModulegroupResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModulegroupResponse:
        """Create an instance of ModulegroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModulegroupResponse.parse_obj(obj)

        _obj = ModulegroupResponse.parse_obj({
            "pki_modulegroup_id": obj.get("pkiModulegroupID"),
            "s_modulegroup_name_x": obj.get("sModulegroupNameX")
        })
        return _obj


