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
from eZmaxApi.models.enum_horizontalalignment import EnumHorizontalalignment
from eZmaxApi.models.ezsigntemplateelementdependency_response import EzsigntemplateelementdependencyResponse
from eZmaxApi.models.ezsigntemplateformfield_response import EzsigntemplateformfieldResponse
from eZmaxApi.models.field_e_ezsigntemplateformfield_dependencyrequirement import FieldEEzsigntemplateformfieldDependencyrequirement
from eZmaxApi.models.field_e_ezsigntemplateformfield_positioning import FieldEEzsigntemplateformfieldPositioning
from eZmaxApi.models.field_e_ezsigntemplateformfield_positioningoccurence import FieldEEzsigntemplateformfieldPositioningoccurence
from eZmaxApi.models.textstylestatic_response_compound import TextstylestaticResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateformfieldResponseCompound(EzsigntemplateformfieldResponse):
    """
    An Ezsigntemplateformfield Object and children
    """ # noqa: E501
    a_obj_ezsigntemplateelementdependency: Optional[List[EzsigntemplateelementdependencyResponse]] = Field(default=None, alias="a_objEzsigntemplateelementdependency")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateformfieldID", "eEzsigntemplateformfieldPositioning", "iEzsigntemplatedocumentpagePagenumber", "sEzsigntemplateformfieldLabel", "sEzsigntemplateformfieldValue", "iEzsigntemplateformfieldX", "iEzsigntemplateformfieldY", "iEzsigntemplateformfieldWidth", "iEzsigntemplateformfieldHeight", "bEzsigntemplateformfieldAutocomplete", "bEzsigntemplateformfieldSelected", "eEzsigntemplateformfieldDependencyrequirement", "sEzsigntemplateformfieldPositioningpattern", "iEzsigntemplateformfieldPositioningoffsetx", "iEzsigntemplateformfieldPositioningoffsety", "eEzsigntemplateformfieldPositioningoccurence", "eEzsigntemplateformfieldHorizontalalignment", "objTextstylestatic", "a_objEzsigntemplateelementdependency"]

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
        """Create an instance of EzsigntemplateformfieldResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_textstylestatic
        if self.obj_textstylestatic:
            _dict['objTextstylestatic'] = self.obj_textstylestatic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplateelementdependency (list)
        _items = []
        if self.a_obj_ezsigntemplateelementdependency:
            for _item_a_obj_ezsigntemplateelementdependency in self.a_obj_ezsigntemplateelementdependency:
                if _item_a_obj_ezsigntemplateelementdependency:
                    _items.append(_item_a_obj_ezsigntemplateelementdependency.to_dict())
            _dict['a_objEzsigntemplateelementdependency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigntemplateformfieldResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateformfieldID": obj.get("pkiEzsigntemplateformfieldID"),
            "eEzsigntemplateformfieldPositioning": obj.get("eEzsigntemplateformfieldPositioning") if obj.get("eEzsigntemplateformfieldPositioning") is not None else FieldEEzsigntemplateformfieldPositioning.PERCOORDINATES,
            "iEzsigntemplatedocumentpagePagenumber": obj.get("iEzsigntemplatedocumentpagePagenumber"),
            "sEzsigntemplateformfieldLabel": obj.get("sEzsigntemplateformfieldLabel"),
            "sEzsigntemplateformfieldValue": obj.get("sEzsigntemplateformfieldValue"),
            "iEzsigntemplateformfieldX": obj.get("iEzsigntemplateformfieldX"),
            "iEzsigntemplateformfieldY": obj.get("iEzsigntemplateformfieldY"),
            "iEzsigntemplateformfieldWidth": obj.get("iEzsigntemplateformfieldWidth"),
            "iEzsigntemplateformfieldHeight": obj.get("iEzsigntemplateformfieldHeight"),
            "bEzsigntemplateformfieldAutocomplete": obj.get("bEzsigntemplateformfieldAutocomplete"),
            "bEzsigntemplateformfieldSelected": obj.get("bEzsigntemplateformfieldSelected"),
            "eEzsigntemplateformfieldDependencyrequirement": obj.get("eEzsigntemplateformfieldDependencyrequirement"),
            "sEzsigntemplateformfieldPositioningpattern": obj.get("sEzsigntemplateformfieldPositioningpattern"),
            "iEzsigntemplateformfieldPositioningoffsetx": obj.get("iEzsigntemplateformfieldPositioningoffsetx"),
            "iEzsigntemplateformfieldPositioningoffsety": obj.get("iEzsigntemplateformfieldPositioningoffsety"),
            "eEzsigntemplateformfieldPositioningoccurence": obj.get("eEzsigntemplateformfieldPositioningoccurence"),
            "eEzsigntemplateformfieldHorizontalalignment": obj.get("eEzsigntemplateformfieldHorizontalalignment"),
            "objTextstylestatic": TextstylestaticResponseCompound.from_dict(obj["objTextstylestatic"]) if obj.get("objTextstylestatic") is not None else None,
            "a_objEzsigntemplateelementdependency": [EzsigntemplateelementdependencyResponse.from_dict(_item) for _item in obj["a_objEzsigntemplateelementdependency"]] if obj.get("a_objEzsigntemplateelementdependency") is not None else None
        })
        return _obj


