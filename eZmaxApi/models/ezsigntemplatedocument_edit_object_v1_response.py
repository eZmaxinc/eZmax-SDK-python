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
from pydantic import BaseModel
from pydantic import Field
from eZmaxApi.models.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from eZmaxApi.models.common_response_warning import CommonResponseWarning
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzsigntemplatedocumentEditObjectV1Response(BaseModel):
    """
    Response for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}
    """ # noqa: E501
    obj_debug_payload: CommonResponseObjDebugPayload = Field(alias="objDebugPayload")
    obj_debug: Optional[CommonResponseObjDebug] = Field(default=None, alias="objDebug")
    a_obj_warning: Optional[List[CommonResponseWarning]] = Field(default=None, alias="a_objWarning")
    __properties: ClassVar[List[str]] = ["objDebugPayload", "objDebug", "a_objWarning"]

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
        """Create an instance of EzsigntemplatedocumentEditObjectV1Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_debug_payload
        if self.obj_debug_payload:
            _dict['objDebugPayload'] = self.obj_debug_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_debug
        if self.obj_debug:
            _dict['objDebug'] = self.obj_debug.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_warning (list)
        _items = []
        if self.a_obj_warning:
            for _item in self.a_obj_warning:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objWarning'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EzsigntemplatedocumentEditObjectV1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objDebugPayload": CommonResponseObjDebugPayload.from_dict(obj.get("objDebugPayload")) if obj.get("objDebugPayload") is not None else None,
            "objDebug": CommonResponseObjDebug.from_dict(obj.get("objDebug")) if obj.get("objDebug") is not None else None,
            "a_objWarning": [CommonResponseWarning.from_dict(_item) for _item in obj.get("a_objWarning")] if obj.get("a_objWarning") is not None else None
        })
        return _obj


