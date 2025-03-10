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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.common_reportcolumn import CommonReportcolumn
from eZmaxApi.models.common_reportsubsection import CommonReportsubsection
from eZmaxApi.models.enum_horizontalalignment import EnumHorizontalalignment
from typing import Optional, Set
from typing_extensions import Self

class CommonReportsection(BaseModel):
    """
    A section in a Report. Each Reportsection shares Reportcolumns disposition with all its Reportsubsection 
    """ # noqa: E501
    a_obj_reportsubsection: List[CommonReportsubsection] = Field(alias="a_objReportsubsection")
    a_obj_reportcolumn: List[CommonReportcolumn] = Field(alias="a_objReportcolumn")
    e_reportsection_horizontalalignment: EnumHorizontalalignment = Field(alias="eReportsectionHorizontalalignment")
    i_reportsection_columncount: StrictInt = Field(description="The number of Reportcolumns in the Reportsection", alias="iReportsectionColumncount")
    i_reportsection_width: StrictInt = Field(description="The combined width of all the Reportcolumns in the Reportsection", alias="iReportsectionWidth")
    s_reportsection_title: Optional[StrictStr] = Field(default=None, description="The title of this Reportsection", alias="sReportsectionTitle")
    __properties: ClassVar[List[str]] = ["a_objReportsubsection", "a_objReportcolumn", "eReportsectionHorizontalalignment", "iReportsectionColumncount", "iReportsectionWidth", "sReportsectionTitle"]

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
        """Create an instance of CommonReportsection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_reportsubsection (list)
        _items = []
        if self.a_obj_reportsubsection:
            for _item_a_obj_reportsubsection in self.a_obj_reportsubsection:
                if _item_a_obj_reportsubsection:
                    _items.append(_item_a_obj_reportsubsection.to_dict())
            _dict['a_objReportsubsection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_reportcolumn (list)
        _items = []
        if self.a_obj_reportcolumn:
            for _item_a_obj_reportcolumn in self.a_obj_reportcolumn:
                if _item_a_obj_reportcolumn:
                    _items.append(_item_a_obj_reportcolumn.to_dict())
            _dict['a_objReportcolumn'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonReportsection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "a_objReportsubsection": [CommonReportsubsection.from_dict(_item) for _item in obj["a_objReportsubsection"]] if obj.get("a_objReportsubsection") is not None else None,
            "a_objReportcolumn": [CommonReportcolumn.from_dict(_item) for _item in obj["a_objReportcolumn"]] if obj.get("a_objReportcolumn") is not None else None,
            "eReportsectionHorizontalalignment": obj.get("eReportsectionHorizontalalignment"),
            "iReportsectionColumncount": obj.get("iReportsectionColumncount"),
            "iReportsectionWidth": obj.get("iReportsectionWidth"),
            "sReportsectionTitle": obj.get("sReportsectionTitle")
        })
        return _obj


