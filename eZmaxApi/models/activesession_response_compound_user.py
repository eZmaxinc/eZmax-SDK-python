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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_user_ezsignsendreminderfrequency import FieldEUserEzsignsendreminderfrequency
from typing import Optional, Set
from typing_extensions import Self

class ActivesessionResponseCompoundUser(BaseModel):
    """
    An Activesession->User Object and children to create a complete structure
    """ # noqa: E501
    pki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="pkiUserID")
    fki_timezone_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Timezone", alias="fkiTimezoneID")
    s_avatar_url: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The url of the picture used as avatar", alias="sAvatarUrl")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_email_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddress")
    e_user_ezsignsendreminderfrequency: FieldEUserEzsignsendreminderfrequency = Field(alias="eUserEzsignsendreminderfrequency")
    i_user_interfacecolor: Annotated[int, Field(strict=True, ge=0)] = Field(description="The int32 representation of the interface color. For example, RGB color #39435B would be 3752795", alias="iUserInterfacecolor")
    b_user_interfacedark: StrictBool = Field(description="Whether to use a dark mode interface", alias="bUserInterfacedark")
    i_user_listresult: Annotated[int, Field(le=500, strict=True, ge=5)] = Field(description="The number of rows to return by default in lists", alias="iUserListresult")
    __properties: ClassVar[List[str]] = ["pkiUserID", "fkiTimezoneID", "sAvatarUrl", "sUserFirstname", "sUserLastname", "sEmailAddress", "eUserEzsignsendreminderfrequency", "iUserInterfacecolor", "bUserInterfacedark", "iUserListresult"]

    @field_validator('s_avatar_url')
    def s_avatar_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(https|http):\/\/[^\s\/$.?#].[^\s]*$", value):
            raise ValueError(r"must validate the regular expression /^(https|http):\/\/[^\s\/$.?#].[^\s]*$/")
        return value

    @field_validator('s_email_address')
    def s_email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
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
        """Create an instance of ActivesessionResponseCompoundUser from a JSON string"""
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
        """Create an instance of ActivesessionResponseCompoundUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiUserID": obj.get("pkiUserID"),
            "fkiTimezoneID": obj.get("fkiTimezoneID"),
            "sAvatarUrl": obj.get("sAvatarUrl"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sUserLastname": obj.get("sUserLastname"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "eUserEzsignsendreminderfrequency": obj.get("eUserEzsignsendreminderfrequency"),
            "iUserInterfacecolor": obj.get("iUserInterfacecolor"),
            "bUserInterfacedark": obj.get("bUserInterfacedark"),
            "iUserListresult": obj.get("iUserListresult")
        })
        return _obj


