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


from typing import List
from pydantic import BaseModel, Field, conint, conlist

class EzsigntemplateCopyV1ResponseMPayload(BaseModel):
    """
    Payload for POST /1/object/ezsigntemplate/{pkiEzsigntemplateID}/copy  # noqa: E501
    """
    a_pki_ezsigntemplate_id: conlist(conint(strict=True, ge=0)) = Field(..., alias="a_pkiEzsigntemplateID", description="An array of unique IDs representing the object that were requested to be copied.  They are returned in the same order as the array containing the objects to be created that was sent in the request.")
    __properties = ["a_pkiEzsigntemplateID"]

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
    def from_json(cls, json_str: str) -> EzsigntemplateCopyV1ResponseMPayload:
        """Create an instance of EzsigntemplateCopyV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsigntemplateCopyV1ResponseMPayload:
        """Create an instance of EzsigntemplateCopyV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsigntemplateCopyV1ResponseMPayload.parse_obj(obj)

        _obj = EzsigntemplateCopyV1ResponseMPayload.parse_obj({
            "a_pki_ezsigntemplate_id": obj.get("a_pkiEzsigntemplateID")
        })
        return _obj


