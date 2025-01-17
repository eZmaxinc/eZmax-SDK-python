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

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from typing import Optional, Set
from typing_extensions import Self

class EzsignannotationDeleteObjectV1Response(CommonResponse):
    """
    Response for DELETE /1/object/ezsignannotation/{pkiEzsignannotationID}
    """ # noqa: E501
    __properties: ClassVar[List[str]] = ["objDebugPayload", "objDebug"]

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
        """Create an instance of EzsignannotationDeleteObjectV1Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_debug_payload
        if self.obj_debug_payload:
            _dict['objDebugPayload'] = self.obj_debug_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_debug
        if self.obj_debug:
            _dict['objDebug'] = self.obj_debug.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignannotationDeleteObjectV1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objDebugPayload": CommonResponseObjDebugPayload.from_dict(obj["objDebugPayload"]) if obj.get("objDebugPayload") is not None else None,
            "objDebug": CommonResponseObjDebug.from_dict(obj["objDebug"]) if obj.get("objDebug") is not None else None
        })
        return _obj


