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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound_user import EzsignfoldersignerassociationResponseCompoundUser
from eZmaxApi.models.ezsignsigner_response_compound import EzsignsignerResponseCompound
from eZmaxApi.models.ezsignsignergroup_response_compound import EzsignsignergroupResponseCompound

class EzsignfoldersignerassociationGetObjectV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}  # noqa: E501
    """
    pki_ezsignfoldersignerassociation_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsignfoldersignerassociationID", description="The unique ID of the Ezsignfoldersignerassociation")
    fki_ezsignfolder_id: conint(strict=True, ge=0) = Field(..., alias="fkiEzsignfolderID", description="The unique ID of the Ezsignfolder")
    b_ezsignfoldersignerassociation_delayedsend: StrictBool = Field(..., alias="bEzsignfoldersignerassociationDelayedsend", description="If this flag is true the signatory is part of a delayed send.")
    b_ezsignfoldersignerassociation_receivecopy: StrictBool = Field(..., alias="bEzsignfoldersignerassociationReceivecopy", description="If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain't required to sign the document.")
    t_ezsignfoldersignerassociation_message: StrictStr = Field(..., alias="tEzsignfoldersignerassociationMessage", description="A custom text message that will be added to the email sent.")
    obj_ezsignsignergroup: Optional[EzsignsignergroupResponseCompound] = Field(None, alias="objEzsignsignergroup")
    obj_user: Optional[EzsignfoldersignerassociationResponseCompoundUser] = Field(None, alias="objUser")
    obj_ezsignsigner: Optional[EzsignsignerResponseCompound] = Field(None, alias="objEzsignsigner")
    __properties = ["pkiEzsignfoldersignerassociationID", "fkiEzsignfolderID", "bEzsignfoldersignerassociationDelayedsend", "bEzsignfoldersignerassociationReceivecopy", "tEzsignfoldersignerassociationMessage", "objEzsignsignergroup", "objUser", "objEzsignsigner"]

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
    def from_json(cls, json_str: str) -> EzsignfoldersignerassociationGetObjectV1ResponseMPayload:
        """Create an instance of EzsignfoldersignerassociationGetObjectV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignsignergroup
        if self.obj_ezsignsignergroup:
            _dict['objEzsignsignergroup'] = self.obj_ezsignsignergroup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_user
        if self.obj_user:
            _dict['objUser'] = self.obj_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignsigner
        if self.obj_ezsignsigner:
            _dict['objEzsignsigner'] = self.obj_ezsignsigner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignfoldersignerassociationGetObjectV1ResponseMPayload:
        """Create an instance of EzsignfoldersignerassociationGetObjectV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignfoldersignerassociationGetObjectV1ResponseMPayload.parse_obj(obj)

        _obj = EzsignfoldersignerassociationGetObjectV1ResponseMPayload.parse_obj({
            "pki_ezsignfoldersignerassociation_id": obj.get("pkiEzsignfoldersignerassociationID"),
            "fki_ezsignfolder_id": obj.get("fkiEzsignfolderID"),
            "b_ezsignfoldersignerassociation_delayedsend": obj.get("bEzsignfoldersignerassociationDelayedsend"),
            "b_ezsignfoldersignerassociation_receivecopy": obj.get("bEzsignfoldersignerassociationReceivecopy"),
            "t_ezsignfoldersignerassociation_message": obj.get("tEzsignfoldersignerassociationMessage"),
            "obj_ezsignsignergroup": EzsignsignergroupResponseCompound.from_dict(obj.get("objEzsignsignergroup")) if obj.get("objEzsignsignergroup") is not None else None,
            "obj_user": EzsignfoldersignerassociationResponseCompoundUser.from_dict(obj.get("objUser")) if obj.get("objUser") is not None else None,
            "obj_ezsignsigner": EzsignsignerResponseCompound.from_dict(obj.get("objEzsignsigner")) if obj.get("objEzsignsigner") is not None else None
        })
        return _obj

