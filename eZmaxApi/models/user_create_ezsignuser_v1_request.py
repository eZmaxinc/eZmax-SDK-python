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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UserCreateEzsignuserV1Request(BaseModel):
    """
    Request for POST /1/module/user/createEzsignuser
    """ # noqa: E501
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_email_address: Annotated[str, Field(strict=True)] = Field(description="The email address.", alias="sEmailAddress")
    s_phone_region: StrictStr = Field(description="The region of the phone number. (For a North America Number only)  The region is the \"514\" section in this sample phone number: (514) 990-1516 x123", alias="sPhoneRegion")
    s_phone_exchange: StrictStr = Field(description="The exchange of the phone number. (For a North America Number only)  The exchange is the \"990\" section in this sample phone number: (514) 990-1516 x123", alias="sPhoneExchange")
    s_phone_number: StrictStr = Field(description="The number of the phone number. (For a North America Number only)  The number is the \"1516\" section in this sample phone number: (514) 990-1516 x123", alias="sPhoneNumber")
    s_phone_extension: Optional[StrictStr] = Field(default=None, description="The extension of the phone number.  The extension is the \"123\" section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers", alias="sPhoneExtension")
    __properties: ClassVar[List[str]] = ["fkiLanguageID", "sUserFirstname", "sUserLastname", "sEmailAddress", "sPhoneRegion", "sPhoneExchange", "sPhoneNumber", "sPhoneExtension"]

    @field_validator('s_email_address')
    def s_email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of UserCreateEzsignuserV1Request from a JSON string"""
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
        """Create an instance of UserCreateEzsignuserV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sUserLastname": obj.get("sUserLastname"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sPhoneRegion": obj.get("sPhoneRegion"),
            "sPhoneExchange": obj.get("sPhoneExchange"),
            "sPhoneNumber": obj.get("sPhoneNumber"),
            "sPhoneExtension": obj.get("sPhoneExtension")
        })
        return _obj


