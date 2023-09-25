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



from pydantic import BaseModel, Field, StrictInt, StrictStr, conint
from eZmaxApi.models.computed_e_communication_direction import ComputedECommunicationDirection
from eZmaxApi.models.field_e_communication_importance import FieldECommunicationImportance
from eZmaxApi.models.field_e_communication_type import FieldECommunicationType

class CustomCommunicationListElementResponse(BaseModel):
    """
    A Communication List Element  # noqa: E501
    """
    pki_communication_id: conint(strict=True, ge=0) = Field(..., alias="pkiCommunicationID", description="The unique ID of the Communication.")
    dt_created_date: StrictStr = Field(..., alias="dtCreatedDate", description="The date and time at which the object was created")
    e_communication_direction: ComputedECommunicationDirection = Field(..., alias="eCommunicationDirection")
    e_communication_importance: FieldECommunicationImportance = Field(..., alias="eCommunicationImportance")
    e_communication_type: FieldECommunicationType = Field(..., alias="eCommunicationType")
    i_communicationrecipient_count: StrictInt = Field(..., alias="iCommunicationrecipientCount", description="The count of Communicationrecipient")
    s_communication_subject: StrictStr = Field(..., alias="sCommunicationSubject", description="The subject of the Communication")
    s_communication_sender: StrictStr = Field(..., alias="sCommunicationSender", description="The sender name of the Communication")
    s_communication_recipient: StrictStr = Field(..., alias="sCommunicationRecipient", description="The recipients' name of the Communication")
    __properties = ["pkiCommunicationID", "dtCreatedDate", "eCommunicationDirection", "eCommunicationImportance", "eCommunicationType", "iCommunicationrecipientCount", "sCommunicationSubject", "sCommunicationSender", "sCommunicationRecipient"]

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
    def from_json(cls, json_str: str) -> CustomCommunicationListElementResponse:
        """Create an instance of CustomCommunicationListElementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomCommunicationListElementResponse:
        """Create an instance of CustomCommunicationListElementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomCommunicationListElementResponse.parse_obj(obj)

        _obj = CustomCommunicationListElementResponse.parse_obj({
            "pki_communication_id": obj.get("pkiCommunicationID"),
            "dt_created_date": obj.get("dtCreatedDate"),
            "e_communication_direction": obj.get("eCommunicationDirection"),
            "e_communication_importance": obj.get("eCommunicationImportance"),
            "e_communication_type": obj.get("eCommunicationType"),
            "i_communicationrecipient_count": obj.get("iCommunicationrecipientCount"),
            "s_communication_subject": obj.get("sCommunicationSubject"),
            "s_communication_sender": obj.get("sCommunicationSender"),
            "s_communication_recipient": obj.get("sCommunicationRecipient")
        })
        return _obj


