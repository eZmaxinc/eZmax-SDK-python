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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound_user import EzsignfoldersignerassociationResponseCompoundUser
from eZmaxApi.models.ezsignsigner_response_compound import EzsignsignerResponseCompound
from eZmaxApi.models.ezsignsignergroup_response_compound import EzsignsignergroupResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsignfoldersignerassociationResponseCompound(BaseModel):
    """
    An Ezsignfoldersignerassociation Object
    """ # noqa: E501
    pki_ezsignfoldersignerassociation_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldersignerassociation", alias="pkiEzsignfoldersignerassociationID")
    fki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="fkiEzsignfolderID")
    b_ezsignfoldersignerassociation_delayedsend: StrictBool = Field(description="If this flag is true the signatory is part of a delayed send.", alias="bEzsignfoldersignerassociationDelayedsend")
    b_ezsignfoldersignerassociation_receivecopy: StrictBool = Field(description="If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain't required to sign the document.", alias="bEzsignfoldersignerassociationReceivecopy")
    t_ezsignfoldersignerassociation_message: StrictStr = Field(description="A custom text message that will be added to the email sent.", alias="tEzsignfoldersignerassociationMessage")
    obj_ezsignsignergroup: Optional[EzsignsignergroupResponseCompound] = Field(default=None, alias="objEzsignsignergroup")
    obj_user: Optional[EzsignfoldersignerassociationResponseCompoundUser] = Field(default=None, alias="objUser")
    obj_ezsignsigner: Optional[EzsignsignerResponseCompound] = Field(default=None, alias="objEzsignsigner")
    __properties: ClassVar[List[str]] = ["pkiEzsignfoldersignerassociationID", "fkiEzsignfolderID", "bEzsignfoldersignerassociationDelayedsend", "bEzsignfoldersignerassociationReceivecopy", "tEzsignfoldersignerassociationMessage", "objEzsignsignergroup", "objUser", "objEzsignsigner"]

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
        """Create an instance of EzsignfoldersignerassociationResponseCompound from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignfoldersignerassociationResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfoldersignerassociationID": obj.get("pkiEzsignfoldersignerassociationID"),
            "fkiEzsignfolderID": obj.get("fkiEzsignfolderID"),
            "bEzsignfoldersignerassociationDelayedsend": obj.get("bEzsignfoldersignerassociationDelayedsend"),
            "bEzsignfoldersignerassociationReceivecopy": obj.get("bEzsignfoldersignerassociationReceivecopy"),
            "tEzsignfoldersignerassociationMessage": obj.get("tEzsignfoldersignerassociationMessage"),
            "objEzsignsignergroup": EzsignsignergroupResponseCompound.from_dict(obj["objEzsignsignergroup"]) if obj.get("objEzsignsignergroup") is not None else None,
            "objUser": EzsignfoldersignerassociationResponseCompoundUser.from_dict(obj["objUser"]) if obj.get("objUser") is not None else None,
            "objEzsignsigner": EzsignsignerResponseCompound.from_dict(obj["objEzsignsigner"]) if obj.get("objEzsignsigner") is not None else None
        })
        return _obj


