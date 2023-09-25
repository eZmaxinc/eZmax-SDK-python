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
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound import EzsignfoldersignerassociationResponseCompound

class EzsignfoldersignerassociationGetObjectV2ResponseMPayload(BaseModel):
    """
    Payload for GET /2/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}  # noqa: E501
    """
    obj_ezsignfoldersignerassociation: EzsignfoldersignerassociationResponseCompound = Field(..., alias="objEzsignfoldersignerassociation")
    __properties = ["objEzsignfoldersignerassociation"]

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
    def from_json(cls, json_str: str) -> EzsignfoldersignerassociationGetObjectV2ResponseMPayload:
        """Create an instance of EzsignfoldersignerassociationGetObjectV2ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldersignerassociation
        if self.obj_ezsignfoldersignerassociation:
            _dict['objEzsignfoldersignerassociation'] = self.obj_ezsignfoldersignerassociation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfoldersignerassociationGetObjectV2ResponseMPayload:
        """Create an instance of EzsignfoldersignerassociationGetObjectV2ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfoldersignerassociationGetObjectV2ResponseMPayload.parse_obj(obj)

        _obj = EzsignfoldersignerassociationGetObjectV2ResponseMPayload.parse_obj({
            "obj_ezsignfoldersignerassociation": EzsignfoldersignerassociationResponseCompound.from_dict(obj.get("objEzsignfoldersignerassociation")) if obj.get("objEzsignfoldersignerassociation") is not None else None
        })
        return _obj


