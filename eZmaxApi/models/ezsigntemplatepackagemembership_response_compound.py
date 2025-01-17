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
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.ezsigntemplate_response_compound import EzsigntemplateResponseCompound
from eZmaxApi.models.ezsigntemplatepackagemembership_response import EzsigntemplatepackagemembershipResponse
from eZmaxApi.models.ezsigntemplatepackagesignermembership_response_compound import EzsigntemplatepackagesignermembershipResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatepackagemembershipResponseCompound(EzsigntemplatepackagemembershipResponse):
    """
    A Ezsigntemplatepackagemembership Object
    """ # noqa: E501
    obj_ezsigntemplate: EzsigntemplateResponseCompound = Field(alias="objEzsigntemplate")
    a_obj_ezsigntemplatepackagesignermembership: List[EzsigntemplatepackagesignermembershipResponseCompound] = Field(alias="a_objEzsigntemplatepackagesignermembership")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatepackagemembershipID", "fkiEzsigntemplatepackageID", "fkiEzsigntemplateID", "iEzsigntemplatepackagemembershipOrder", "objEzsigntemplate", "a_objEzsigntemplatepackagesignermembership"]

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
        """Create an instance of EzsigntemplatepackagemembershipResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplate
        if self.obj_ezsigntemplate:
            _dict['objEzsigntemplate'] = self.obj_ezsigntemplate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplatepackagesignermembership (list)
        _items = []
        if self.a_obj_ezsigntemplatepackagesignermembership:
            for _item_a_obj_ezsigntemplatepackagesignermembership in self.a_obj_ezsigntemplatepackagesignermembership:
                if _item_a_obj_ezsigntemplatepackagesignermembership:
                    _items.append(_item_a_obj_ezsigntemplatepackagesignermembership.to_dict())
            _dict['a_objEzsigntemplatepackagesignermembership'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigntemplatepackagemembershipResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatepackagemembershipID": obj.get("pkiEzsigntemplatepackagemembershipID"),
            "fkiEzsigntemplatepackageID": obj.get("fkiEzsigntemplatepackageID"),
            "fkiEzsigntemplateID": obj.get("fkiEzsigntemplateID"),
            "iEzsigntemplatepackagemembershipOrder": obj.get("iEzsigntemplatepackagemembershipOrder"),
            "objEzsigntemplate": EzsigntemplateResponseCompound.from_dict(obj["objEzsigntemplate"]) if obj.get("objEzsigntemplate") is not None else None,
            "a_objEzsigntemplatepackagesignermembership": [EzsigntemplatepackagesignermembershipResponseCompound.from_dict(_item) for _item in obj["a_objEzsigntemplatepackagesignermembership"]] if obj.get("a_objEzsigntemplatepackagesignermembership") is not None else None
        })
        return _obj


