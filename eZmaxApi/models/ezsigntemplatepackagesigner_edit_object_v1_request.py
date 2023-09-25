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
from eZmaxApi.models.ezsigntemplatepackagesigner_request_compound import EzsigntemplatepackagesignerRequestCompound

class EzsigntemplatepackagesignerEditObjectV1Request(BaseModel):
    """
    Request for PUT /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}  # noqa: E501
    """
    obj_ezsigntemplatepackagesigner: EzsigntemplatepackagesignerRequestCompound = Field(..., alias="objEzsigntemplatepackagesigner")
    __properties = ["objEzsigntemplatepackagesigner"]

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
    def from_json(cls, json_str: str) -> EzsigntemplatepackagesignerEditObjectV1Request:
        """Create an instance of EzsigntemplatepackagesignerEditObjectV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplatepackagesigner
        if self.obj_ezsigntemplatepackagesigner:
            _dict['objEzsigntemplatepackagesigner'] = self.obj_ezsigntemplatepackagesigner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplatepackagesignerEditObjectV1Request:
        """Create an instance of EzsigntemplatepackagesignerEditObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplatepackagesignerEditObjectV1Request.parse_obj(obj)

        _obj = EzsigntemplatepackagesignerEditObjectV1Request.parse_obj({
            "obj_ezsigntemplatepackagesigner": EzsigntemplatepackagesignerRequestCompound.from_dict(obj.get("objEzsigntemplatepackagesigner")) if obj.get("objEzsigntemplatepackagesigner") is not None else None
        })
        return _obj


