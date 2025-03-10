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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from eZmaxApi.models.custom_form_data_ezsignformfield_response import CustomFormDataEzsignformfieldResponse
from typing import Optional, Set
from typing_extensions import Self

class CustomFormDataEzsignformfieldgroupResponse(BaseModel):
    """
    An FormDataSigner->Ezsignformfieldgroup Object and children to create a complete structure
    """ # noqa: E501
    s_ezsignformfieldgroup_label: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The Label for the Ezsignformfieldgroup", alias="sEzsignformfieldgroupLabel")
    a_obj_ezsignformfield: List[CustomFormDataEzsignformfieldResponse] = Field(alias="a_objEzsignformfield")
    __properties: ClassVar[List[str]] = ["sEzsignformfieldgroupLabel", "a_objEzsignformfield"]

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
        """Create an instance of CustomFormDataEzsignformfieldgroupResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignformfield (list)
        _items = []
        if self.a_obj_ezsignformfield:
            for _item_a_obj_ezsignformfield in self.a_obj_ezsignformfield:
                if _item_a_obj_ezsignformfield:
                    _items.append(_item_a_obj_ezsignformfield.to_dict())
            _dict['a_objEzsignformfield'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomFormDataEzsignformfieldgroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sEzsignformfieldgroupLabel": obj.get("sEzsignformfieldgroupLabel"),
            "a_objEzsignformfield": [CustomFormDataEzsignformfieldResponse.from_dict(_item) for _item in obj["a_objEzsignformfield"]] if obj.get("a_objEzsignformfield") is not None else None
        })
        return _obj


