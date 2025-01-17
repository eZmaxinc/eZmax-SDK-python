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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from eZmaxApi.models.ezsignfolder_get_attachment_count_v1_response_m_payload import EzsignfolderGetAttachmentCountV1ResponseMPayload
from typing import Optional, Set
from typing_extensions import Self

class EzsignfolderGetAttachmentCountV1Response(BaseModel):
    """
    Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getAttachmentCount
    """ # noqa: E501
    obj_debug_payload: CommonResponseObjDebugPayload = Field(alias="objDebugPayload")
    obj_debug: Optional[CommonResponseObjDebug] = Field(default=None, alias="objDebug")
    m_payload: EzsignfolderGetAttachmentCountV1ResponseMPayload = Field(alias="mPayload")
    __properties: ClassVar[List[str]] = ["objDebugPayload", "objDebug", "mPayload"]

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
        """Create an instance of EzsignfolderGetAttachmentCountV1Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of m_payload
        if self.m_payload:
            _dict['mPayload'] = self.m_payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignfolderGetAttachmentCountV1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objDebugPayload": CommonResponseObjDebugPayload.from_dict(obj["objDebugPayload"]) if obj.get("objDebugPayload") is not None else None,
            "objDebug": CommonResponseObjDebug.from_dict(obj["objDebug"]) if obj.get("objDebug") is not None else None,
            "mPayload": EzsignfolderGetAttachmentCountV1ResponseMPayload.from_dict(obj["mPayload"]) if obj.get("mPayload") is not None else None
        })
        return _obj


