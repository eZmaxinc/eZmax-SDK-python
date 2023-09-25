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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint

class CommunicationattachmentResponseCompound(BaseModel):
    """
    A Communicationattachment Object  # noqa: E501
    """
    pki_communicationattachment_id: StrictInt = Field(..., alias="pkiCommunicationattachmentID", description="The unique ID of the Communicationattachment")
    fki_attachment_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAttachmentID", description="The unique ID of the Attachment.")
    fki_invoice_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiInvoiceID", description="The unique ID of the Invoice.")
    fki_salarypreparation_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiSalarypreparationID", description="The unique ID of the Salarypreparation.")
    s_communicationattachment_name: StrictStr = Field(..., alias="sCommunicationattachmentName", description="The name of the Communicationattachment")
    s_download_url: Optional[StrictStr] = Field(None, alias="sDownloadUrl", description="The Url to the requested document.  Url will expire after 3 hours.")
    __properties = ["pkiCommunicationattachmentID", "fkiAttachmentID", "fkiInvoiceID", "fkiSalarypreparationID", "sCommunicationattachmentName", "sDownloadUrl"]

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
    def from_json(cls, json_str: str) -> CommunicationattachmentResponseCompound:
        """Create an instance of CommunicationattachmentResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommunicationattachmentResponseCompound:
        """Create an instance of CommunicationattachmentResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommunicationattachmentResponseCompound.parse_obj(obj)

        _obj = CommunicationattachmentResponseCompound.parse_obj({
            "pki_communicationattachment_id": obj.get("pkiCommunicationattachmentID"),
            "fki_attachment_id": obj.get("fkiAttachmentID"),
            "fki_invoice_id": obj.get("fkiInvoiceID"),
            "fki_salarypreparation_id": obj.get("fkiSalarypreparationID"),
            "s_communicationattachment_name": obj.get("sCommunicationattachmentName"),
            "s_download_url": obj.get("sDownloadUrl")
        })
        return _obj


