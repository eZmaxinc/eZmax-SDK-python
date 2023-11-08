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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr, validator
from eZmaxApi.models.communicationexternalrecipient_request_compound import CommunicationexternalrecipientRequestCompound
from eZmaxApi.models.communicationrecipient_request_compound import CommunicationrecipientRequestCompound
from eZmaxApi.models.communicationreference_request_compound import CommunicationreferenceRequestCompound
from eZmaxApi.models.custom_communicationattachment_request import CustomCommunicationattachmentRequest
from eZmaxApi.models.custom_communicationsender_request import CustomCommunicationsenderRequest
from eZmaxApi.models.field_e_communication_importance import FieldECommunicationImportance
from eZmaxApi.models.field_e_communication_type import FieldECommunicationType

class CommunicationRequestCompound(BaseModel):
    """
    Request for POST /1/object/communication  # noqa: E501
    """
    pki_communication_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiCommunicationID", description="The unique ID of the Communication.")
    e_communication_importance: Optional[FieldECommunicationImportance] = Field(None, alias="eCommunicationImportance")
    e_communication_type: FieldECommunicationType = Field(..., alias="eCommunicationType")
    obj_communicationsender: Optional[CustomCommunicationsenderRequest] = Field(None, alias="objCommunicationsender")
    s_communication_subject: Optional[constr(strict=True)] = Field(None, alias="sCommunicationSubject", description="The subject of the Communication")
    t_communication_body: StrictStr = Field(..., alias="tCommunicationBody", description="The Body of the Communication")
    b_communication_private: StrictBool = Field(..., alias="bCommunicationPrivate", description="Whether the Communication is private or not")
    e_communication_attachmenttype: Optional[StrictStr] = Field(None, alias="eCommunicationAttachmenttype", description="How the attachment should be included in the email.   Only used if eCommunicationType is **Email**")
    i_communication_attachmentlinkexpiration: Optional[conint(strict=True, le=30, ge=1)] = Field(None, alias="iCommunicationAttachmentlinkexpiration", description="The number of days before the attachment link expired.   Only used if eCommunicationType is **Email** and eCommunicationattachmentType is **Link**")
    b_communication_readreceipt: Optional[StrictBool] = Field(None, alias="bCommunicationReadreceipt", description="Whether we ask for a read receipt or not.")
    a_obj_communicationattachment: conlist(CustomCommunicationattachmentRequest, min_items=0) = Field(..., alias="a_objCommunicationattachment")
    a_obj_communicationrecipient: conlist(CommunicationrecipientRequestCompound, min_items=0) = Field(..., alias="a_objCommunicationrecipient")
    a_obj_communicationreference: conlist(CommunicationreferenceRequestCompound, min_items=0) = Field(..., alias="a_objCommunicationreference")
    a_obj_communicationexternalrecipient: conlist(CommunicationexternalrecipientRequestCompound, min_items=0) = Field(..., alias="a_objCommunicationexternalrecipient")
    __properties = ["pkiCommunicationID", "eCommunicationImportance", "eCommunicationType", "objCommunicationsender", "sCommunicationSubject", "tCommunicationBody", "bCommunicationPrivate", "eCommunicationAttachmenttype", "iCommunicationAttachmentlinkexpiration", "bCommunicationReadreceipt", "a_objCommunicationattachment", "a_objCommunicationrecipient", "a_objCommunicationreference", "a_objCommunicationexternalrecipient"]

    @validator('s_communication_subject')
    def s_communication_subject_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,150}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,150}$/")
        return value

    @validator('e_communication_attachmenttype')
    def e_communication_attachmenttype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Attachment', 'Url'):
            raise ValueError("must be one of enum values ('Attachment', 'Url')")
        return value

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
    def from_json(cls, json_str: str) -> CommunicationRequestCompound:
        """Create an instance of CommunicationRequestCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_communicationsender
        if self.obj_communicationsender:
            _dict['objCommunicationsender'] = self.obj_communicationsender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationattachment (list)
        _items = []
        if self.a_obj_communicationattachment:
            for _item in self.a_obj_communicationattachment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objCommunicationattachment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationrecipient (list)
        _items = []
        if self.a_obj_communicationrecipient:
            for _item in self.a_obj_communicationrecipient:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objCommunicationrecipient'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationreference (list)
        _items = []
        if self.a_obj_communicationreference:
            for _item in self.a_obj_communicationreference:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objCommunicationreference'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationexternalrecipient (list)
        _items = []
        if self.a_obj_communicationexternalrecipient:
            for _item in self.a_obj_communicationexternalrecipient:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objCommunicationexternalrecipient'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommunicationRequestCompound:
        """Create an instance of CommunicationRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommunicationRequestCompound.parse_obj(obj)

        _obj = CommunicationRequestCompound.parse_obj({
            "pki_communication_id": obj.get("pkiCommunicationID"),
            "e_communication_importance": obj.get("eCommunicationImportance"),
            "e_communication_type": obj.get("eCommunicationType"),
            "obj_communicationsender": CustomCommunicationsenderRequest.from_dict(obj.get("objCommunicationsender")) if obj.get("objCommunicationsender") is not None else None,
            "s_communication_subject": obj.get("sCommunicationSubject"),
            "t_communication_body": obj.get("tCommunicationBody"),
            "b_communication_private": obj.get("bCommunicationPrivate"),
            "e_communication_attachmenttype": obj.get("eCommunicationAttachmenttype"),
            "i_communication_attachmentlinkexpiration": obj.get("iCommunicationAttachmentlinkexpiration"),
            "b_communication_readreceipt": obj.get("bCommunicationReadreceipt"),
            "a_obj_communicationattachment": [CustomCommunicationattachmentRequest.from_dict(_item) for _item in obj.get("a_objCommunicationattachment")] if obj.get("a_objCommunicationattachment") is not None else None,
            "a_obj_communicationrecipient": [CommunicationrecipientRequestCompound.from_dict(_item) for _item in obj.get("a_objCommunicationrecipient")] if obj.get("a_objCommunicationrecipient") is not None else None,
            "a_obj_communicationreference": [CommunicationreferenceRequestCompound.from_dict(_item) for _item in obj.get("a_objCommunicationreference")] if obj.get("a_objCommunicationreference") is not None else None,
            "a_obj_communicationexternalrecipient": [CommunicationexternalrecipientRequestCompound.from_dict(_item) for _item in obj.get("a_objCommunicationexternalrecipient")] if obj.get("a_objCommunicationexternalrecipient") is not None else None
        })
        return _obj


