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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.module_response_compound import ModuleResponseCompound
from eZmaxApi.models.modulegroup_response import ModulegroupResponse
from typing import Optional, Set
from typing_extensions import Self

class ModulegroupResponseCompound(ModulegroupResponse):
    """
    A Modulegroup Object
    """ # noqa: E501
    a_obj_module: Optional[List[ModuleResponseCompound]] = Field(default=None, alias="a_objModule")
    __properties: ClassVar[List[str]] = ["pkiModulegroupID", "sModulegroupNameX", "a_objModule"]

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
        """Create an instance of ModulegroupResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_module (list)
        _items = []
        if self.a_obj_module:
            for _item_a_obj_module in self.a_obj_module:
                if _item_a_obj_module:
                    _items.append(_item_a_obj_module.to_dict())
            _dict['a_objModule'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModulegroupResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiModulegroupID": obj.get("pkiModulegroupID"),
            "sModulegroupNameX": obj.get("sModulegroupNameX"),
            "a_objModule": [ModuleResponseCompound.from_dict(_item) for _item in obj["a_objModule"]] if obj.get("a_objModule") is not None else None
        })
        return _obj


