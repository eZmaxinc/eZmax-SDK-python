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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_sessionhistory_endby import FieldESessionhistoryEndby
from typing import Optional, Set
from typing_extensions import Self

class SessionhistoryListElement(BaseModel):
    """
    A Sessionhistory List Element
    """ # noqa: E501
    pki_sessionhistory_id: Annotated[int, Field(le=2147483647, strict=True, ge=1)] = Field(description="The unique ID of the Sessionhistory", alias="pkiSessionhistoryID")
    fki_computer_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Computer", alias="fkiComputerID")
    fki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserID")
    dt_sessionhistory_firsthit: Annotated[str, Field(strict=True)] = Field(description="The first hit of the Sessionhistory", alias="dtSessionhistoryFirsthit")
    dt_sessionhistory_lasthit: Annotated[str, Field(strict=True)] = Field(description="The last hit of the Sessionhistory", alias="dtSessionhistoryLasthit")
    e_sessionhistory_endby: FieldESessionhistoryEndby = Field(alias="eSessionhistoryEndby")
    s_computer_description: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The description of the Computer", alias="sComputerDescription")
    s_sessionhistory_duration: Annotated[str, Field(strict=True)] = Field(description="The duration of the session", alias="sSessionhistoryDuration")
    s_sessionhistory_ip: StrictStr = Field(description="Represent an IP address.", alias="sSessionhistoryIP")
    s_user_loginname: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The login name of the User.", alias="sUserLoginname")
    __properties: ClassVar[List[str]] = ["pkiSessionhistoryID", "fkiComputerID", "fkiUserID", "dtSessionhistoryFirsthit", "dtSessionhistoryLasthit", "eSessionhistoryEndby", "sComputerDescription", "sSessionhistoryDuration", "sSessionhistoryIP", "sUserLoginname"]

    @field_validator('dt_sessionhistory_firsthit')
    def dt_sessionhistory_firsthit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('dt_sessionhistory_lasthit')
    def dt_sessionhistory_lasthit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('s_computer_description')
    def s_computer_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_sessionhistory_duration')
    def s_sessionhistory_duration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0[0-9]{1}|\d{2,}):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^(0[0-9]{1}|\d{2,}):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:([\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$/")
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
        """Create an instance of SessionhistoryListElement from a JSON string"""
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
        """Create an instance of SessionhistoryListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSessionhistoryID": obj.get("pkiSessionhistoryID"),
            "fkiComputerID": obj.get("fkiComputerID"),
            "fkiUserID": obj.get("fkiUserID"),
            "dtSessionhistoryFirsthit": obj.get("dtSessionhistoryFirsthit"),
            "dtSessionhistoryLasthit": obj.get("dtSessionhistoryLasthit"),
            "eSessionhistoryEndby": obj.get("eSessionhistoryEndby"),
            "sComputerDescription": obj.get("sComputerDescription"),
            "sSessionhistoryDuration": obj.get("sSessionhistoryDuration"),
            "sSessionhistoryIP": obj.get("sSessionhistoryIP"),
            "sUserLoginname": obj.get("sUserLoginname")
        })
        return _obj


