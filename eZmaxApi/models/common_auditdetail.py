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

class CommonAuditdetail(BaseModel):
    """
    Gives informations about the user that created the object or the last user to have modified it.  If the object was never modified after creation, both Created and Modified informations will be the same. 
    """ # noqa: E501
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    fki_apikey_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Apikey", alias="fkiApikeyID")
    s_user_loginname: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_apikey_description_x: Optional[StrictStr] = Field(default=None, description="The description of the Apikey in the language of the requester", alias="sApikeyDescriptionX")
    dt_auditdetail_date: StrictStr = Field(description="Represent a Date Time. The timezone is the one configured in the User's profile.", alias="dtAuditdetailDate")
    __properties: ClassVar[List[str]] = ["fkiUserID", "fkiApikeyID", "sUserLoginname", "sUserLastname", "sUserFirstname", "sApikeyDescriptionX", "dtAuditdetailDate"]

    @field_validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of CommonAuditdetail from a JSON string"""
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
        """Create an instance of CommonAuditdetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiUserID": obj.get("fkiUserID"),
            "fkiApikeyID": obj.get("fkiApikeyID"),
            "sUserLoginname": obj.get("sUserLoginname"),
            "sUserLastname": obj.get("sUserLastname"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sApikeyDescriptionX": obj.get("sApikeyDescriptionX"),
            "dtAuditdetailDate": obj.get("dtAuditdetailDate")
        })
        return _obj


