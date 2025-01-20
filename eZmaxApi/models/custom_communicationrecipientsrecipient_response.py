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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.custom_contact_name_response import CustomContactNameResponse
from eZmaxApi.models.email_response import EmailResponse
from eZmaxApi.models.phone_response_compound import PhoneResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class CustomCommunicationrecipientsrecipientResponse(BaseModel):
    """
    Generic AutocompleteElement Response
    """ # noqa: E501
    fki_agent_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Agent.", alias="fkiAgentID")
    fki_broker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Broker.", alias="fkiBrokerID")
    fki_contact_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Contact", alias="fkiContactID")
    fki_customer_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Customer.", alias="fkiCustomerID")
    fki_employee_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Employee.", alias="fkiEmployeeID")
    fki_ezsignsigner_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignsigner", alias="fkiEzsignsignerID")
    fki_franchiseoffice_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisereoffice", alias="fkiFranchiseofficeID")
    fki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserID")
    fki_agentincorporation_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Agentincorporation.", alias="fkiAgentincorporationID")
    fki_assistant_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Assistant.", alias="fkiAssistantID")
    fki_externalbroker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Externalbroker.", alias="fkiExternalbrokerID")
    fki_ezcomagent_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezcomagent.", alias="fkiEzcomagentID")
    fki_notary_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Notary.", alias="fkiNotaryID")
    fki_rewardmember_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Rewardmember.", alias="fkiRewardmemberID")
    fki_supplier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Supplier.", alias="fkiSupplierID")
    e_communicationrecipientsrecipient_objecttype: StrictStr = Field(alias="eCommunicationrecipientsrecipientObjecttype")
    obj_contact_name: CustomContactNameResponse = Field(alias="objContactName")
    obj_email: Optional[EmailResponse] = Field(default=None, description="An Email Object and children to create a complete structure", alias="objEmail")
    obj_phone_fax: Optional[PhoneResponseCompound] = Field(default=None, alias="objPhoneFax")
    obj_phone_sms: Optional[PhoneResponseCompound] = Field(default=None, alias="objPhoneSMS")
    __properties: ClassVar[List[str]] = ["fkiAgentID", "fkiBrokerID", "fkiContactID", "fkiCustomerID", "fkiEmployeeID", "fkiEzsignsignerID", "fkiFranchiseofficeID", "fkiUserID", "fkiAgentincorporationID", "fkiAssistantID", "fkiExternalbrokerID", "fkiEzcomagentID", "fkiNotaryID", "fkiRewardmemberID", "fkiSupplierID", "eCommunicationrecipientsrecipientObjecttype", "objContactName", "objEmail", "objPhoneFax", "objPhoneSMS"]

    @field_validator('e_communicationrecipientsrecipient_objecttype')
    def e_communicationrecipientsrecipient_objecttype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Agent', 'Agentincorporation', 'Assistant', 'Broker', 'Contact', 'Customer', 'Employee', 'Externalbroker', 'Ezcomagent', 'Ezcomcompany', 'Ezsignsigner', 'Franchiseoffice', 'Notary', 'Rewardmember', 'Supplier', 'User']):
            raise ValueError("must be one of enum values ('Agent', 'Agentincorporation', 'Assistant', 'Broker', 'Contact', 'Customer', 'Employee', 'Externalbroker', 'Ezcomagent', 'Ezcomcompany', 'Ezsignsigner', 'Franchiseoffice', 'Notary', 'Rewardmember', 'Supplier', 'User')")
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
        """Create an instance of CustomCommunicationrecipientsrecipientResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_contact_name
        if self.obj_contact_name:
            _dict['objContactName'] = self.obj_contact_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_email
        if self.obj_email:
            _dict['objEmail'] = self.obj_email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_fax
        if self.obj_phone_fax:
            _dict['objPhoneFax'] = self.obj_phone_fax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_sms
        if self.obj_phone_sms:
            _dict['objPhoneSMS'] = self.obj_phone_sms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomCommunicationrecipientsrecipientResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiAgentID": obj.get("fkiAgentID"),
            "fkiBrokerID": obj.get("fkiBrokerID"),
            "fkiContactID": obj.get("fkiContactID"),
            "fkiCustomerID": obj.get("fkiCustomerID"),
            "fkiEmployeeID": obj.get("fkiEmployeeID"),
            "fkiEzsignsignerID": obj.get("fkiEzsignsignerID"),
            "fkiFranchiseofficeID": obj.get("fkiFranchiseofficeID"),
            "fkiUserID": obj.get("fkiUserID"),
            "fkiAgentincorporationID": obj.get("fkiAgentincorporationID"),
            "fkiAssistantID": obj.get("fkiAssistantID"),
            "fkiExternalbrokerID": obj.get("fkiExternalbrokerID"),
            "fkiEzcomagentID": obj.get("fkiEzcomagentID"),
            "fkiNotaryID": obj.get("fkiNotaryID"),
            "fkiRewardmemberID": obj.get("fkiRewardmemberID"),
            "fkiSupplierID": obj.get("fkiSupplierID"),
            "eCommunicationrecipientsrecipientObjecttype": obj.get("eCommunicationrecipientsrecipientObjecttype"),
            "objContactName": CustomContactNameResponse.from_dict(obj["objContactName"]) if obj.get("objContactName") is not None else None,
            "objEmail": EmailResponse.from_dict(obj["objEmail"]) if obj.get("objEmail") is not None else None,
            "objPhoneFax": PhoneResponseCompound.from_dict(obj["objPhoneFax"]) if obj.get("objPhoneFax") is not None else None,
            "objPhoneSMS": PhoneResponseCompound.from_dict(obj["objPhoneSMS"]) if obj.get("objPhoneSMS") is not None else None
        })
        return _obj


