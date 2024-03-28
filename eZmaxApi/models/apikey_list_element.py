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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ApikeyListElement(BaseModel):
    """
    A Branding List Element
    """ # noqa: E501
    pki_apikey_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Apikey", alias="pkiApikeyID")
    s_apikey_description_x: StrictStr = Field(description="The description of the Apikey in the language of the requester", alias="sApikeyDescriptionX")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    b_apikey_isactive: StrictBool = Field(description="Whether the apikey is active or not", alias="bApikeyIsactive")
    b_apikey_issigned: StrictBool = Field(description="Whether the apikey is signed or not", alias="bApikeyIssigned")
    __properties: ClassVar[List[str]] = ["pkiApikeyID", "sApikeyDescriptionX", "sUserFirstname", "sUserLastname", "bApikeyIsactive", "bApikeyIssigned"]

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
        """Create an instance of ApikeyListElement from a JSON string"""
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
        """Create an instance of ApikeyListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiApikeyID": obj.get("pkiApikeyID"),
            "sApikeyDescriptionX": obj.get("sApikeyDescriptionX"),
            "sUserFirstname": obj.get("sUserFirstname"),
            "sUserLastname": obj.get("sUserLastname"),
            "bApikeyIsactive": obj.get("bApikeyIsactive"),
            "bApikeyIssigned": obj.get("bApikeyIssigned")
        })
        return _obj


