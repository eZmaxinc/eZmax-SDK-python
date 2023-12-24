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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.multilingual_apikey_description import MultilingualApikeyDescription
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApikeyRequestCompound(BaseModel):
    """
    An Apikey Object and children to create a complete structure
    """ # noqa: E501
    pki_apikey_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Apikey", alias="pkiApikeyID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    obj_apikey_description: MultilingualApikeyDescription = Field(alias="objApikeyDescription")
    b_apikey_isactive: Optional[StrictBool] = Field(default=None, description="Whether the apikey is active or not", alias="bApikeyIsactive")
    b_apikey_issigned: Optional[StrictBool] = Field(default=None, description="Whether the apikey is signed or not", alias="bApikeyIssigned")
    __properties: ClassVar[List[str]] = ["pkiApikeyID", "fkiUserID", "objApikeyDescription", "bApikeyIsactive", "bApikeyIssigned"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApikeyRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of obj_apikey_description
        if self.obj_apikey_description:
            _dict['objApikeyDescription'] = self.obj_apikey_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApikeyRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiApikeyID": obj.get("pkiApikeyID"),
            "fkiUserID": obj.get("fkiUserID"),
            "objApikeyDescription": MultilingualApikeyDescription.from_dict(obj.get("objApikeyDescription")) if obj.get("objApikeyDescription") is not None else None,
            "bApikeyIsactive": obj.get("bApikeyIsactive"),
            "bApikeyIssigned": obj.get("bApikeyIssigned")
        })
        return _obj


