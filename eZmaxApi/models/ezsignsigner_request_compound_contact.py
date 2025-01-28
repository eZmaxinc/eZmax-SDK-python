# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
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

class EzsignsignerRequestCompoundContact(BaseModel):
    """
    A Ezsignsigner->Contact Object and children to create a complete structure
    """ # noqa: E501
    s_contact_firstname: Annotated[str, Field(strict=True)] = Field(description="The First name of the contact", alias="sContactFirstname")
    s_contact_lastname: Annotated[str, Field(strict=True)] = Field(description="The Last name of the contact", alias="sContactLastname")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_email_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddress")
    s_phone_e164: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A phone number in E.164 Format", alias="sPhoneE164")
    s_phone_extension: Optional[StrictStr] = Field(default=None, description="The extension of the phone number.  The extension is the \"123\" section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers", alias="sPhoneExtension")
    s_phone_e164_cell: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A phone number in E.164 Format", alias="sPhoneE164Cell")
    s_phone_number: Optional[StrictStr] = Field(default=None, alias="sPhoneNumber")
    s_phone_number_cell: Optional[StrictStr] = Field(default=None, alias="sPhoneNumberCell")
    __properties: ClassVar[List[str]] = ["sContactFirstname", "sContactLastname", "fkiLanguageID", "sEmailAddress", "sPhoneE164", "sPhoneExtension", "sPhoneE164Cell", "sPhoneNumber", "sPhoneNumberCell"]

    @field_validator('s_contact_firstname')
    def s_contact_firstname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,20}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,20}$/")
        return value

    @field_validator('s_contact_lastname')
    def s_contact_lastname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,25}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,25}$/")
        return value

    @field_validator('s_email_address')
    def s_email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
        return value

    @field_validator('s_phone_e164')
    def s_phone_e164_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
        return value

    @field_validator('s_phone_e164_cell')
    def s_phone_e164_cell_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
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
        """Create an instance of EzsignsignerRequestCompoundContact from a JSON string"""
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
        """Create an instance of EzsignsignerRequestCompoundContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sContactFirstname": obj.get("sContactFirstname"),
            "sContactLastname": obj.get("sContactLastname"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sPhoneE164": obj.get("sPhoneE164"),
            "sPhoneExtension": obj.get("sPhoneExtension"),
            "sPhoneE164Cell": obj.get("sPhoneE164Cell"),
            "sPhoneNumber": obj.get("sPhoneNumber"),
            "sPhoneNumberCell": obj.get("sPhoneNumberCell")
        })
        return _obj


