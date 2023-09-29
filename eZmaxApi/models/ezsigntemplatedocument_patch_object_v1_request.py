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
from eZmaxApi.models.ezsigntemplatedocument_request_patch import EzsigntemplatedocumentRequestPatch

class EzsigntemplatedocumentPatchObjectV1Request(BaseModel):
    """
    Request for PATCH /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}  # noqa: E501
    """
    obj_ezsigntemplatedocument: EzsigntemplatedocumentRequestPatch = Field(..., alias="objEzsigntemplatedocument")
    __properties = ["objEzsigntemplatedocument"]

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
    def from_json(cls, json_str: str) -> EzsigntemplatedocumentPatchObjectV1Request:
        """Create an instance of EzsigntemplatedocumentPatchObjectV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplatedocument
        if self.obj_ezsigntemplatedocument:
            _dict['objEzsigntemplatedocument'] = self.obj_ezsigntemplatedocument.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatedocumentPatchObjectV1Request:
        """Create an instance of EzsigntemplatedocumentPatchObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatedocumentPatchObjectV1Request.parse_obj(obj)

        _obj = EzsigntemplatedocumentPatchObjectV1Request.parse_obj({
            "obj_ezsigntemplatedocument": EzsigntemplatedocumentRequestPatch.from_dict(obj.get("objEzsigntemplatedocument")) if obj.get("objEzsigntemplatedocument") is not None else None
        })
        return _obj

