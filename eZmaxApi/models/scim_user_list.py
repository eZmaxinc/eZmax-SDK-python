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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.scim_user import ScimUser
from typing import Optional, Set
from typing_extensions import Self

class ScimUserList(BaseModel):
    """
    ScimUserList
    """ # noqa: E501
    total_results: Optional[StrictInt] = Field(default=None, alias="totalResults")
    items_per_page: Optional[StrictInt] = Field(default=None, alias="itemsPerPage")
    start_index: Optional[StrictInt] = Field(default=None, alias="startIndex")
    schemas: Optional[List[StrictStr]] = None
    resources: Optional[List[ScimUser]] = Field(default=None, alias="Resources")
    __properties: ClassVar[List[str]] = ["totalResults", "itemsPerPage", "startIndex", "schemas", "Resources"]

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
        """Create an instance of ScimUserList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScimUserList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalResults": obj.get("totalResults"),
            "itemsPerPage": obj.get("itemsPerPage"),
            "startIndex": obj.get("startIndex"),
            "schemas": obj.get("schemas"),
            "Resources": [ScimUser.from_dict(_item) for _item in obj["Resources"]] if obj.get("Resources") is not None else None
        })
        return _obj


