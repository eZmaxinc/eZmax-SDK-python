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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.communicationexternalrecipient_request_compound import CommunicationexternalrecipientRequestCompound
from eZmaxApi.models.communicationrecipient_request_compound import CommunicationrecipientRequestCompound
from eZmaxApi.models.communicationreference_request_compound import CommunicationreferenceRequestCompound
from eZmaxApi.models.custom_communicationattachment_request import CustomCommunicationattachmentRequest
from eZmaxApi.models.custom_communicationsender_request import CustomCommunicationsenderRequest
from eZmaxApi.models.field_e_communication_importance import FieldECommunicationImportance
from eZmaxApi.models.field_e_communication_type import FieldECommunicationType
from typing import Optional, Set
from typing_extensions import Self

class CommunicationRequestCompound(BaseModel):
    """
    Request for POST /1/object/communication
    """ # noqa: E501
    pki_communication_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Communication.", alias="pkiCommunicationID")
    e_communication_importance: Optional[FieldECommunicationImportance] = Field(default=None, alias="eCommunicationImportance")
    e_communication_type: FieldECommunicationType = Field(alias="eCommunicationType")
    obj_communicationsender: Optional[CustomCommunicationsenderRequest] = Field(default=None, alias="objCommunicationsender")
    s_communication_subject: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The subject of the Communication", alias="sCommunicationSubject")
    t_communication_body: StrictStr = Field(description="The Body of the Communication", alias="tCommunicationBody")
    b_communication_private: StrictBool = Field(description="Whether the Communication is private or not", alias="bCommunicationPrivate")
    e_communication_attachmenttype: Optional[StrictStr] = Field(default=None, description="How the attachment should be included in the email.   Only used if eCommunicationType is **Email**", alias="eCommunicationAttachmenttype")
    i_communication_attachmentlinkexpiration: Optional[Annotated[int, Field(le=30, strict=True, ge=1)]] = Field(default=None, description="The number of days before the attachment link expired.   Only used if eCommunicationType is **Email** and eCommunicationattachmentType is **Link**", alias="iCommunicationAttachmentlinkexpiration")
    b_communication_readreceipt: Optional[StrictBool] = Field(default=None, description="Whether we ask for a read receipt or not.", alias="bCommunicationReadreceipt")
    a_obj_communicationattachment: Annotated[List[CustomCommunicationattachmentRequest], Field(min_length=0)] = Field(alias="a_objCommunicationattachment")
    a_obj_communicationrecipient: Annotated[List[CommunicationrecipientRequestCompound], Field(min_length=0)] = Field(alias="a_objCommunicationrecipient")
    a_obj_communicationreference: Annotated[List[CommunicationreferenceRequestCompound], Field(min_length=0)] = Field(alias="a_objCommunicationreference")
    a_obj_communicationexternalrecipient: Annotated[List[CommunicationexternalrecipientRequestCompound], Field(min_length=0)] = Field(alias="a_objCommunicationexternalrecipient")
    __properties: ClassVar[List[str]] = ["pkiCommunicationID", "eCommunicationImportance", "eCommunicationType", "objCommunicationsender", "sCommunicationSubject", "tCommunicationBody", "bCommunicationPrivate", "eCommunicationAttachmenttype", "iCommunicationAttachmentlinkexpiration", "bCommunicationReadreceipt", "a_objCommunicationattachment", "a_objCommunicationrecipient", "a_objCommunicationreference", "a_objCommunicationexternalrecipient"]

    @field_validator('s_communication_subject')
    def s_communication_subject_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,200}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,200}$/")
        return value

    @field_validator('e_communication_attachmenttype')
    def e_communication_attachmenttype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Attachment', 'Url']):
            raise ValueError("must be one of enum values ('Attachment', 'Url')")
        return value

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
        """Create an instance of CommunicationRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_communicationsender
        if self.obj_communicationsender:
            _dict['objCommunicationsender'] = self.obj_communicationsender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationattachment (list)
        _items = []
        if self.a_obj_communicationattachment:
            for _item_a_obj_communicationattachment in self.a_obj_communicationattachment:
                if _item_a_obj_communicationattachment:
                    _items.append(_item_a_obj_communicationattachment.to_dict())
            _dict['a_objCommunicationattachment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationrecipient (list)
        _items = []
        if self.a_obj_communicationrecipient:
            for _item_a_obj_communicationrecipient in self.a_obj_communicationrecipient:
                if _item_a_obj_communicationrecipient:
                    _items.append(_item_a_obj_communicationrecipient.to_dict())
            _dict['a_objCommunicationrecipient'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationreference (list)
        _items = []
        if self.a_obj_communicationreference:
            for _item_a_obj_communicationreference in self.a_obj_communicationreference:
                if _item_a_obj_communicationreference:
                    _items.append(_item_a_obj_communicationreference.to_dict())
            _dict['a_objCommunicationreference'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationexternalrecipient (list)
        _items = []
        if self.a_obj_communicationexternalrecipient:
            for _item_a_obj_communicationexternalrecipient in self.a_obj_communicationexternalrecipient:
                if _item_a_obj_communicationexternalrecipient:
                    _items.append(_item_a_obj_communicationexternalrecipient.to_dict())
            _dict['a_objCommunicationexternalrecipient'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommunicationRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiCommunicationID": obj.get("pkiCommunicationID"),
            "eCommunicationImportance": obj.get("eCommunicationImportance"),
            "eCommunicationType": obj.get("eCommunicationType"),
            "objCommunicationsender": CustomCommunicationsenderRequest.from_dict(obj["objCommunicationsender"]) if obj.get("objCommunicationsender") is not None else None,
            "sCommunicationSubject": obj.get("sCommunicationSubject"),
            "tCommunicationBody": obj.get("tCommunicationBody"),
            "bCommunicationPrivate": obj.get("bCommunicationPrivate"),
            "eCommunicationAttachmenttype": obj.get("eCommunicationAttachmenttype"),
            "iCommunicationAttachmentlinkexpiration": obj.get("iCommunicationAttachmentlinkexpiration"),
            "bCommunicationReadreceipt": obj.get("bCommunicationReadreceipt"),
            "a_objCommunicationattachment": [CustomCommunicationattachmentRequest.from_dict(_item) for _item in obj["a_objCommunicationattachment"]] if obj.get("a_objCommunicationattachment") is not None else None,
            "a_objCommunicationrecipient": [CommunicationrecipientRequestCompound.from_dict(_item) for _item in obj["a_objCommunicationrecipient"]] if obj.get("a_objCommunicationrecipient") is not None else None,
            "a_objCommunicationreference": [CommunicationreferenceRequestCompound.from_dict(_item) for _item in obj["a_objCommunicationreference"]] if obj.get("a_objCommunicationreference") is not None else None,
            "a_objCommunicationexternalrecipient": [CommunicationexternalrecipientRequestCompound.from_dict(_item) for _item in obj["a_objCommunicationexternalrecipient"]] if obj.get("a_objCommunicationexternalrecipient") is not None else None
        })
        return _obj


