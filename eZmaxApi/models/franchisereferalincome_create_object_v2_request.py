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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.franchisereferalincome_request_compound import FranchisereferalincomeRequestCompound
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FranchisereferalincomeCreateObjectV2Request(BaseModel):
    """
    Request for POST /2/object/franchisereferalincome
    """ # noqa: E501
    a_obj_franchisereferalincome: Annotated[List[FranchisereferalincomeRequestCompound], Field(min_length=1)] = Field(alias="a_objFranchisereferalincome")
    __properties: ClassVar[List[str]] = ["a_objFranchisereferalincome"]

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
        """Create an instance of FranchisereferalincomeCreateObjectV2Request from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_franchisereferalincome (list)
        _items = []
        if self.a_obj_franchisereferalincome:
            for _item in self.a_obj_franchisereferalincome:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objFranchisereferalincome'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FranchisereferalincomeCreateObjectV2Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "a_objFranchisereferalincome": [FranchisereferalincomeRequestCompound.from_dict(_item) for _item in obj.get("a_objFranchisereferalincome")] if obj.get("a_objFranchisereferalincome") is not None else None
        })
        return _obj


