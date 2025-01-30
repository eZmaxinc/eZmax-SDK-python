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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_communicationexternalrecipient_type import FieldECommunicationexternalrecipientType
from typing import Optional, Set
from typing_extensions import Self

class CommunicationexternalrecipientRequest(BaseModel):
    """
    A Communicationexternalrecipient Object
    """ # noqa: E501
    pki_communicationexternalrecipient_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the Communicationexternalrecipient", alias="pkiCommunicationexternalrecipientID")
    s_email_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email address.", alias="sEmailAddress")
    s_phone_e164: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A phone number in E.164 Format", alias="sPhoneE164")
    e_communicationexternalrecipient_type: Optional[FieldECommunicationexternalrecipientType] = Field(default=None, alias="eCommunicationexternalrecipientType")
    s_communicationexternalrecipient_name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The name of the Communicationexternalrecipient", alias="sCommunicationexternalrecipientName")
    __properties: ClassVar[List[str]] = ["pkiCommunicationexternalrecipientID", "sEmailAddress", "sPhoneE164", "eCommunicationexternalrecipientType", "sCommunicationexternalrecipientName"]

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

    @field_validator('s_communicationexternalrecipient_name')
    def s_communicationexternalrecipient_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
        """Create an instance of CommunicationexternalrecipientRequest from a JSON string"""
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
        """Create an instance of CommunicationexternalrecipientRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiCommunicationexternalrecipientID": obj.get("pkiCommunicationexternalrecipientID"),
            "sEmailAddress": obj.get("sEmailAddress"),
            "sPhoneE164": obj.get("sPhoneE164"),
            "eCommunicationexternalrecipientType": obj.get("eCommunicationexternalrecipientType"),
            "sCommunicationexternalrecipientName": obj.get("sCommunicationexternalrecipientName")
        })
        return _obj


