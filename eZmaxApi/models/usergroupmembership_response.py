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
from pydantic import BaseModel, Field, StrictStr, conint, constr, validator

class UsergroupmembershipResponse(BaseModel):
    """
    A Usergroupmembership Object  # noqa: E501
    """
    pki_usergroupmembership_id: conint(strict=True, le=65535, ge=0) = Field(..., alias="pkiUsergroupmembershipID", description="The unique ID of the Usergroupmembership")
    fki_usergroup_id: conint(strict=True, le=255, ge=0) = Field(..., alias="fkiUsergroupID", description="The unique ID of the Usergroup")
    fki_user_id: conint(strict=True, ge=0) = Field(..., alias="fkiUserID", description="The unique ID of the User")
    s_user_firstname: StrictStr = Field(..., alias="sUserFirstname", description="The first name of the user")
    s_user_lastname: StrictStr = Field(..., alias="sUserLastname", description="The last name of the user")
    s_user_loginname: constr(strict=True) = Field(..., alias="sUserLoginname", description="The login name of the User.")
    s_email_address: Optional[StrictStr] = Field(None, alias="sEmailAddress", description="The email address.")
    s_usergroup_name_x: constr(strict=True) = Field(..., alias="sUsergroupNameX", description="The Name of the Usergroup in the language of the requester")
    __properties = ["pkiUsergroupmembershipID", "fkiUsergroupID", "fkiUserID", "sUserFirstname", "sUserLastname", "sUserLoginname", "sEmailAddress", "sUsergroupNameX"]

    @validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

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
    def from_json(cls, json_str: str) -> UsergroupmembershipResponse:
        """Create an instance of UsergroupmembershipResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsergroupmembershipResponse:
        """Create an instance of UsergroupmembershipResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsergroupmembershipResponse.parse_obj(obj)

        _obj = UsergroupmembershipResponse.parse_obj({
            "pki_usergroupmembership_id": obj.get("pkiUsergroupmembershipID"),
            "fki_usergroup_id": obj.get("fkiUsergroupID"),
            "fki_user_id": obj.get("fkiUserID"),
            "s_user_firstname": obj.get("sUserFirstname"),
            "s_user_lastname": obj.get("sUserLastname"),
            "s_user_loginname": obj.get("sUserLoginname"),
            "s_email_address": obj.get("sEmailAddress"),
            "s_usergroup_name_x": obj.get("sUsergroupNameX")
        })
        return _obj


