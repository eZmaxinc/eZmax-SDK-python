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

class UsergroupListElement(BaseModel):
    """
    A Usergroup List Element  # noqa: E501
    """
    pki_usergroup_id: conint(strict=True, le=255, ge=0) = Field(..., alias="pkiUsergroupID", description="The unique ID of the Usergroup")
    s_usergroup_name_x: constr(strict=True) = Field(..., alias="sUsergroupNameX", description="The Name of the Usergroup in the language of the requester")
    i_count_user: conint(strict=True, le=16777215, ge=0) = Field(..., alias="iCountUser", description="Number of users in group")
    __properties = ["pkiUsergroupID", "sUsergroupNameX", "iCountUser"]

    @validator('s_usergroup_name_x')
    def s_usergroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
    def from_json(cls, json_str: str) -> UsergroupListElement:
        """Create an instance of UsergroupListElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsergroupListElement:
        """Create an instance of UsergroupListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsergroupListElement.parse_obj(obj)

        _obj = UsergroupListElement.parse_obj({
            "pki_usergroup_id": obj.get("pkiUsergroupID"),
            "s_usergroup_name_x": obj.get("sUsergroupNameX"),
            "i_count_user": obj.get("iCountUser")
        })
        return _obj

