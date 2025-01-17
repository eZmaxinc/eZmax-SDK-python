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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UsergroupexternalRequestCompound(BaseModel):
    """
    A Usergroupexternal Object and children
    """ # noqa: E501
    pki_usergroupexternal_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroupexternal", alias="pkiUsergroupexternalID")
    s_usergroupexternal_name: Annotated[str, Field(strict=True)] = Field(description="The name of the Usergroupexternal", alias="sUsergroupexternalName")
    s_usergroupexternal_id: Annotated[str, Field(strict=True)] = Field(description="The id of the Usergroupexternal", alias="sUsergroupexternalID")
    __properties: ClassVar[List[str]] = ["pkiUsergroupexternalID", "sUsergroupexternalName", "sUsergroupexternalID"]

    @field_validator('s_usergroupexternal_name')
    def s_usergroupexternal_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,64}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,64}$/")
        return value

    @field_validator('s_usergroupexternal_id')
    def s_usergroupexternal_id_validate_regular_expression(cls, value):
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
        """Create an instance of UsergroupexternalRequestCompound from a JSON string"""
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
        """Create an instance of UsergroupexternalRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiUsergroupexternalID": obj.get("pkiUsergroupexternalID"),
            "sUsergroupexternalName": obj.get("sUsergroupexternalName"),
            "sUsergroupexternalID": obj.get("sUsergroupexternalID")
        })
        return _obj


