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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UserstagedResponseCompound(BaseModel):
    """
    A Userstaged Object
    """ # noqa: E501
    pki_userstaged_id: Annotated[int, Field(le=65535, strict=True, ge=1)] = Field(description="The unique ID of the Userstaged", alias="pkiUserstagedID")
    fki_email_id: Annotated[int, Field(le=16777215, strict=True, ge=1)] = Field(description="The unique ID of the Email", alias="fkiEmailID")
    s_email_address: Annotated[str, Field(strict=True)] = Field(description="The email address.", alias="sEmailAddress")
    s_userstaged_firstname: Annotated[str, Field(strict=True)] = Field(description="The firstname of the Userstaged", alias="sUserstagedFirstname")
    s_userstaged_lastname: Annotated[str, Field(strict=True)] = Field(description="The lastname of the Userstaged", alias="sUserstagedLastname")
    s_userstaged_externalid: Annotated[str, Field(strict=True)] = Field(description="The externalid of the Userstaged", alias="sUserstagedExternalid")
    __properties: ClassVar[List[str]] = ["pkiUserstagedID", "fkiEmailID", "sEmailAddress", "sUserstagedFirstname", "sUserstagedLastname", "sUserstagedExternalid"]

    @field_validator('s_email_address')
    def s_email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$", value):
            raise ValueError(r"must validate the regular expression /^[\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$/")
        return value

    @field_validator('s_userstaged_firstname')
    def s_userstaged_firstname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,20}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,20}$/")
        return value

    @field_validator('s_userstaged_lastname')
    def s_userstaged_lastname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,25}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,25}$/")
        return value

    @field_validator('s_userstaged_externalid')
    def s_userstaged_externalid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,60}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,60}$/")
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
        """Create an instance of UserstagedResponseCompound from a JSON string"""
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
        """Create an instance of UserstagedResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiUserstagedID": obj.get("pkiUserstagedID"),
            "fkiEmailID": obj.get("fkiEmailID"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sUserstagedFirstname": obj.get("sUserstagedFirstname"),
            "sUserstagedLastname": obj.get("sUserstagedLastname"),
            "sUserstagedExternalid": obj.get("sUserstagedExternalid")
        })
        return _obj


