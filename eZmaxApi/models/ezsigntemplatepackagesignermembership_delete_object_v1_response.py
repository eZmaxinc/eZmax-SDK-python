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


from typing import Optional
from pydantic import BaseModel, Field
from eZmaxApi.models.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from eZmaxApi.models.ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload import EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload

class EzsigntemplatepackagesignermembershipDeleteObjectV1Response(BaseModel):
    """
    Response for DELETE /1/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID}  # noqa: E501
    """
    obj_debug_payload: CommonResponseObjDebugPayload = Field(..., alias="objDebugPayload")
    obj_debug: Optional[CommonResponseObjDebug] = Field(None, alias="objDebug")
    m_payload: EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload = Field(..., alias="mPayload")
    __properties = ["objDebugPayload", "objDebug", "mPayload"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EzsigntemplatepackagesignermembershipDeleteObjectV1Response:
        """Create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> EzsigntemplatepackagesignermembershipDeleteObjectV1Response:
        """Create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatepackagesignermembershipDeleteObjectV1Response.parse_obj(obj)

        _obj = EzsigntemplatepackagesignermembershipDeleteObjectV1Response.parse_obj({
            "obj_debug_payload": CommonResponseObjDebugPayload.from_dict(obj.get("objDebugPayload")) if obj.get("objDebugPayload") is not None else None,
            "obj_debug": CommonResponseObjDebug.from_dict(obj.get("objDebug")) if obj.get("objDebug") is not None else None,
            "m_payload": EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload.from_dict(obj.get("mPayload")) if obj.get("mPayload") is not None else None
        })
        return _obj


