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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EmailRequestCompound(BaseModel):
    """
    An Email Object and children to create a complete structure
    """ # noqa: E501
    pki_email_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Email", alias="pkiEmailID")
    fki_emailtype_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home|", alias="fkiEmailtypeID")
    s_email_address: Annotated[str, Field(strict=True)] = Field(description="The email address.", alias="sEmailAddress")
    __properties: ClassVar[List[str]] = ["pkiEmailID", "fkiEmailtypeID", "sEmailAddress"]

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
        """Create an instance of EmailRequestCompound from a JSON string"""
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
        """Create an instance of EmailRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEmailID": obj.get("pkiEmailID"),
            "fkiEmailtypeID": obj.get("fkiEmailtypeID"),
            "sEmailAddress": obj.get("sEmailAddress")
        })
        return _obj


