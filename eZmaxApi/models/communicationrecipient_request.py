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
from pydantic import BaseModel, Field, conint
from eZmaxApi.models.field_e_communicationrecipient_type import FieldECommunicationrecipientType

class CommunicationrecipientRequest(BaseModel):
    """
    A Communicationrecipient Object  # noqa: E501
    """
    pki_communicationrecipient_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiCommunicationrecipientID", description="The unique ID of the Communicationrecipient.")
    fki_agent_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAgentID", description="The unique ID of the Agent.")
    fki_agentincorporation_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAgentincorporationID", description="The unique ID of the Agentincorporation.")
    fki_broker_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiBrokerID", description="The unique ID of the Broker.")
    fki_customer_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiCustomerID", description="The unique ID of the Customer.")
    fki_employee_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEmployeeID", description="The unique ID of the Employee.")
    fki_assistant_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAssistantID", description="The unique ID of the Assistant.")
    fki_externalbroker_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiExternalbrokerID", description="The unique ID of the Externalbroker.")
    fki_ezsignsigner_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEzsignsignerID", description="The unique ID of the Ezsignsigner")
    fki_notary_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiNotaryID", description="The unique ID of the Notary.")
    fki_supplier_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiSupplierID", description="The unique ID of the Supplier.")
    fki_user_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiUserID", description="The unique ID of the User")
    e_communicationrecipient_type: Optional[FieldECommunicationrecipientType] = Field(None, alias="eCommunicationrecipientType")
    __properties = ["pkiCommunicationrecipientID", "fkiAgentID", "fkiAgentincorporationID", "fkiBrokerID", "fkiCustomerID", "fkiEmployeeID", "fkiAssistantID", "fkiExternalbrokerID", "fkiEzsignsignerID", "fkiNotaryID", "fkiSupplierID", "fkiUserID", "eCommunicationrecipientType"]

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
    def from_json(cls, json_str: str) -> CommunicationrecipientRequest:
        """Create an instance of CommunicationrecipientRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommunicationrecipientRequest:
        """Create an instance of CommunicationrecipientRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommunicationrecipientRequest.parse_obj(obj)

        _obj = CommunicationrecipientRequest.parse_obj({
            "pki_communicationrecipient_id": obj.get("pkiCommunicationrecipientID"),
            "fki_agent_id": obj.get("fkiAgentID"),
            "fki_agentincorporation_id": obj.get("fkiAgentincorporationID"),
            "fki_broker_id": obj.get("fkiBrokerID"),
            "fki_customer_id": obj.get("fkiCustomerID"),
            "fki_employee_id": obj.get("fkiEmployeeID"),
            "fki_assistant_id": obj.get("fkiAssistantID"),
            "fki_externalbroker_id": obj.get("fkiExternalbrokerID"),
            "fki_ezsignsigner_id": obj.get("fkiEzsignsignerID"),
            "fki_notary_id": obj.get("fkiNotaryID"),
            "fki_supplier_id": obj.get("fkiSupplierID"),
            "fki_user_id": obj.get("fkiUserID"),
            "e_communicationrecipient_type": obj.get("eCommunicationrecipientType")
        })
        return _obj


