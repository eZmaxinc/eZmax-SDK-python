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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.multilingual_ezsignsigningreason_description import MultilingualEzsignsigningreasonDescription
from typing import Optional, Set
from typing_extensions import Self

class EzsignsigningreasonRequest(BaseModel):
    """
    A Ezsignsigningreason Object
    """ # noqa: E501
    pki_ezsignsigningreason_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignsigningreason", alias="pkiEzsignsigningreasonID")
    obj_ezsignsigningreason_description: MultilingualEzsignsigningreasonDescription = Field(alias="objEzsignsigningreasonDescription")
    b_ezsignsigningreason_isactive: StrictBool = Field(description="Whether the ezsignsigningreason is active or not", alias="bEzsignsigningreasonIsactive")
    __properties: ClassVar[List[str]] = ["pkiEzsignsigningreasonID", "objEzsignsigningreasonDescription", "bEzsignsigningreasonIsactive"]

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
        """Create an instance of EzsignsigningreasonRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignsigningreason_description
        if self.obj_ezsignsigningreason_description:
            _dict['objEzsignsigningreasonDescription'] = self.obj_ezsignsigningreason_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsigningreasonRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignsigningreasonID": obj.get("pkiEzsignsigningreasonID"),
            "objEzsignsigningreasonDescription": MultilingualEzsignsigningreasonDescription.from_dict(obj["objEzsignsigningreasonDescription"]) if obj.get("objEzsignsigningreasonDescription") is not None else None,
            "bEzsignsigningreasonIsactive": obj.get("bEzsignsigningreasonIsactive")
        })
        return _obj


