# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UsergroupexternalmembershipResponse(BaseModel):
    """
    A Usergroupexternalmembership Object
    """ # noqa: E501
    pki_usergroupexternalmembership_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Usergroupexternalmembership", alias="pkiUsergroupexternalmembershipID")
    fki_usergroupexternal_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Usergroupexternal", alias="fkiUsergroupexternalID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_user_loginname: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginname")
    s_email_address: Annotated[str, Field(strict=True)] = Field(description="The email address.", alias="sEmailAddress")
    s_usergroupexternal_name: Annotated[str, Field(strict=True)] = Field(description="The name of the Usergroupexternal", alias="sUsergroupexternalName")
    __properties: ClassVar[List[str]] = ["pkiUsergroupexternalmembershipID", "fkiUsergroupexternalID", "fkiUserID", "sUserFirstname", "sUserLastname", "sUserLoginname", "sEmailAddress", "sUsergroupexternalName"]

    @field_validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

    @field_validator('s_email_address')
    def s_email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
        return value

    @field_validator('s_usergroupexternal_name')
    def s_usergroupexternal_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,64}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,64}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UsergroupexternalmembershipResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsergroupexternalmembershipResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiUsergroupexternalmembershipID": obj.get("pkiUsergroupexternalmembershipID"),
            "fkiUsergroupexternalID": obj.get("fkiUsergroupexternalID"),
            "fkiUserID": obj.get("fkiUserID"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sUserLastname": obj.get("sUserLastname"),
            "sUserLoginname": obj.get("sUserLoginname"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sUsergroupexternalName": obj.get("sUsergroupexternalName")
        })
        return _obj


