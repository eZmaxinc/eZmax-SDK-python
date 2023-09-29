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



from pydantic import BaseModel, Field
from eZmaxApi.models.ezsignbulksend_response_compound import EzsignbulksendResponseCompound

class EzsignbulksendGetObjectV2ResponseMPayload(BaseModel):
    """
    Payload for GET /2/object/ezsignbulksend/{pkiEzsignbulksendID}  # noqa: E501
    """
    obj_ezsignbulksend: EzsignbulksendResponseCompound = Field(..., alias="objEzsignbulksend")
    __properties = ["objEzsignbulksend"]

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
    def from_json(cls, json_str: str) -> EzsignbulksendGetObjectV2ResponseMPayload:
        """Create an instance of EzsignbulksendGetObjectV2ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignbulksend
        if self.obj_ezsignbulksend:
            _dict['objEzsignbulksend'] = self.obj_ezsignbulksend.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignbulksendGetObjectV2ResponseMPayload:
        """Create an instance of EzsignbulksendGetObjectV2ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignbulksendGetObjectV2ResponseMPayload.parse_obj(obj)

        _obj = EzsignbulksendGetObjectV2ResponseMPayload.parse_obj({
            "obj_ezsignbulksend": EzsignbulksendResponseCompound.from_dict(obj.get("objEzsignbulksend")) if obj.get("objEzsignbulksend") is not None else None
        })
        return _obj

