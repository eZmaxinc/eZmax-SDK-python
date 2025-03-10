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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.common_reportcell import CommonReportcell
from typing import Optional, Set
from typing_extensions import Self

class CommonReportrow(BaseModel):
    """
    A row in a Reportsubsectionpart 
    """ # noqa: E501
    a_obj_reportcell: List[CommonReportcell] = Field(alias="a_objReportcell")
    obj_variableobject: Dict[str, Any] = Field(description="A Variable object without predefined property names", alias="objVariableobject")
    i_reportrow_height: StrictInt = Field(description="The reportrow height in pixels", alias="iReportrowHeight")
    __properties: ClassVar[List[str]] = ["a_objReportcell", "objVariableobject", "iReportrowHeight"]

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
        """Create an instance of CommonReportrow from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_reportcell (list)
        _items = []
        if self.a_obj_reportcell:
            for _item_a_obj_reportcell in self.a_obj_reportcell:
                if _item_a_obj_reportcell:
                    _items.append(_item_a_obj_reportcell.to_dict())
            _dict['a_objReportcell'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonReportrow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "a_objReportcell": [CommonReportcell.from_dict(_item) for _item in obj["a_objReportcell"]] if obj.get("a_objReportcell") is not None else None,
            "objVariableobject": obj.get("objVariableobject"),
            "iReportrowHeight": obj.get("iReportrowHeight")
        })
        return _obj


