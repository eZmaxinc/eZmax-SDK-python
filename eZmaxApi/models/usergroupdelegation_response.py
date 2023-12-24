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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UsergroupdelegationResponse(BaseModel):
    """
    A Usergroupdelegation Object
    """ # noqa: E501
    pki_usergroupdelegation_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Usergroupdelegation", alias="pkiUsergroupdelegationID")
    fki_usergroup_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Usergroup", alias="fkiUsergroupID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_user_loginname: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginname")
    s_email_address: Optional[StrictStr] = Field(default=None, description="The email address.", alias="sEmailAddress")
    s_usergroup_name_x: Annotated[str, Field(strict=True)] = Field(description="The Name of the Usergroup in the language of the requester", alias="sUsergroupNameX")
    __properties: ClassVar[List[str]] = ["pkiUsergroupdelegationID", "fkiUsergroupID", "fkiUserID", "sUserFirstname", "sUserLastname", "sUserLoginname", "sEmailAddress", "sUsergroupNameX"]

    @field_validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

    @field_validator('s_usergroup_name_x')
    def s_usergroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UsergroupdelegationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UsergroupdelegationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiUsergroupdelegationID": obj.get("pkiUsergroupdelegationID"),
            "fkiUsergroupID": obj.get("fkiUsergroupID"),
            "fkiUserID": obj.get("fkiUserID"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sUserLastname": obj.get("sUserLastname"),
            "sUserLoginname": obj.get("sUserLoginname"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sUsergroupNameX": obj.get("sUsergroupNameX")
        })
        return _obj


