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
from eZmaxApi.models.custom_timezone_with_code_response import CustomTimezoneWithCodeResponse
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignatureSignV1ResponseMPayload(BaseModel):
    """
    Response for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign
    """ # noqa: E501
    dt_ezsignsignature_date_in_folder_timezone: Annotated[str, Field(strict=True)] = Field(description="The date the Ezsignsignature was signed in folder's timezone", alias="dtEzsignsignatureDateInFolderTimezone")
    obj_timezone: Optional[CustomTimezoneWithCodeResponse] = Field(default=None, alias="objTimezone")
    __properties: ClassVar[List[str]] = ["dtEzsignsignatureDateInFolderTimezone", "objTimezone"]

    @field_validator('dt_ezsignsignature_date_in_folder_timezone')
    def dt_ezsignsignature_date_in_folder_timezone_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
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
        """Create an instance of EzsignsignatureSignV1ResponseMPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_timezone
        if self.obj_timezone:
            _dict['objTimezone'] = self.obj_timezone.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignatureSignV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dtEzsignsignatureDateInFolderTimezone": obj.get("dtEzsignsignatureDateInFolderTimezone"),
            "objTimezone": CustomTimezoneWithCodeResponse.from_dict(obj["objTimezone"]) if obj.get("objTimezone") is not None else None
        })
        return _obj


