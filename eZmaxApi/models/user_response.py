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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, constr, validator
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.email_response_compound import EmailResponseCompound
from eZmaxApi.models.field_e_user_ezsignaccess import FieldEUserEzsignaccess
from eZmaxApi.models.field_e_user_logintype import FieldEUserLogintype
from eZmaxApi.models.field_e_user_origin import FieldEUserOrigin
from eZmaxApi.models.field_e_user_type import FieldEUserType
from eZmaxApi.models.phone_response_compound import PhoneResponseCompound

class UserResponse(BaseModel):
    """
    A User Object  # noqa: E501
    """
    pki_user_id: conint(strict=True, ge=0) = Field(..., alias="pkiUserID", description="The unique ID of the User")
    fki_agent_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAgentID", description="The unique ID of the Agent.")
    fki_broker_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiBrokerID", description="The unique ID of the Broker.")
    fki_assistant_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiAssistantID", description="The unique ID of the Assistant.")
    fki_employee_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiEmployeeID", description="The unique ID of the Employee.")
    fki_company_id_default: conint(strict=True, le=255, ge=1) = Field(..., alias="fkiCompanyIDDefault", description="The unique ID of the Company")
    s_company_name_x: StrictStr = Field(..., alias="sCompanyNameX", description="The Name of the Company in the language of the requester")
    fki_department_id_default: conint(strict=True, ge=0) = Field(..., alias="fkiDepartmentIDDefault", description="The unique ID of the Department")
    s_department_name_x: StrictStr = Field(..., alias="sDepartmentNameX", description="The Name of the Department in the language of the requester")
    fki_timezone_id: conint(strict=True, ge=0) = Field(..., alias="fkiTimezoneID", description="The unique ID of the Timezone")
    s_timezone_name: StrictStr = Field(..., alias="sTimezoneName", description="The description of the Timezone")
    fki_language_id: conint(strict=True, le=2, ge=1) = Field(..., alias="fkiLanguageID", description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|")
    s_language_name_x: StrictStr = Field(..., alias="sLanguageNameX", description="The Name of the Language in the language of the requester")
    obj_email: EmailResponseCompound = Field(..., alias="objEmail")
    fki_billingentityinternal_id: conint(strict=True, ge=0) = Field(..., alias="fkiBillingentityinternalID", description="The unique ID of the Billingentityinternal.")
    s_billingentityinternal_description_x: StrictStr = Field(..., alias="sBillingentityinternalDescriptionX", description="The description of the Billingentityinternal in the language of the requester")
    obj_phone_home: Optional[PhoneResponseCompound] = Field(None, alias="objPhoneHome")
    obj_phone_sms: Optional[PhoneResponseCompound] = Field(None, alias="objPhoneSMS")
    fki_secretquestion_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiSecretquestionID", description="The unique ID of the Secretquestion.  Valid values:  |Value|Description| |-|-| |1|The name of the hospital in which you were born| |2|The name of your grade school| |3|The last name of your favorite teacher| |4|Your favorite sports team| |5|Your favorite TV show| |6|Your favorite movie| |7|The name of the street on which you grew up| |8|The name of your first employer| |9|Your first car| |10|Your favorite food| |11|The name of your first pet| |12|Favorite musician/band| |13|What instrument you play| |14|Your father's middle name| |15|Your mother's maiden name| |16|Name of your eldest child| |17|Your spouse's middle name| |18|Favorite restaurant| |19|Childhood nickname| |20|Favorite vacation destination| |21|Your boat's name| |22|Date of Birth (YYYY-MM-DD)|")
    fki_module_id_form: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiModuleIDForm", description="The unique ID of the Module")
    s_module_name_x: Optional[StrictStr] = Field(None, alias="sModuleNameX", description="The Name of the Module in the language of the requester")
    e_user_origin: FieldEUserOrigin = Field(..., alias="eUserOrigin")
    e_user_type: FieldEUserType = Field(..., alias="eUserType")
    e_user_logintype: FieldEUserLogintype = Field(..., alias="eUserLogintype")
    s_user_firstname: StrictStr = Field(..., alias="sUserFirstname", description="The first name of the user")
    s_user_lastname: StrictStr = Field(..., alias="sUserLastname", description="The last name of the user")
    s_user_loginname: constr(strict=True) = Field(..., alias="sUserLoginname", description="The login name of the User.")
    e_user_ezsignaccess: FieldEUserEzsignaccess = Field(..., alias="eUserEzsignaccess")
    dt_user_lastlogondate: Optional[constr(strict=True)] = Field(None, alias="dtUserLastlogondate", description="The last logon date of the User")
    dt_user_passwordchanged: Optional[constr(strict=True)] = Field(None, alias="dtUserPasswordchanged", description="The date at which the User's password was last changed")
    dt_user_ezsignprepaidexpiration: Optional[constr(strict=True)] = Field(None, alias="dtUserEzsignprepaidexpiration", description="The eZsign prepaid expiration date")
    b_user_isactive: StrictBool = Field(..., alias="bUserIsactive", description="Whether the User is active or not")
    b_user_validatebyadministration: Optional[StrictBool] = Field(None, alias="bUserValidatebyadministration", description="Whether if the transactions in which the User is implicated must be validated by administrative personnel or not")
    b_user_validatebydirector: Optional[StrictBool] = Field(None, alias="bUserValidatebydirector", description="Whether if the transactions in which the User is implicated must be validated by a director or not")
    b_user_attachmentautoverified: Optional[StrictBool] = Field(None, alias="bUserAttachmentautoverified", description="Whether if Attachments uploaded by the User must be validated or not")
    b_user_changepassword: StrictBool = Field(..., alias="bUserChangepassword", description="Whether if the User is forced to change its password")
    obj_audit: CommonAudit = Field(..., alias="objAudit")
    __properties = ["pkiUserID", "fkiAgentID", "fkiBrokerID", "fkiAssistantID", "fkiEmployeeID", "fkiCompanyIDDefault", "sCompanyNameX", "fkiDepartmentIDDefault", "sDepartmentNameX", "fkiTimezoneID", "sTimezoneName", "fkiLanguageID", "sLanguageNameX", "objEmail", "fkiBillingentityinternalID", "sBillingentityinternalDescriptionX", "objPhoneHome", "objPhoneSMS", "fkiSecretquestionID", "fkiModuleIDForm", "sModuleNameX", "eUserOrigin", "eUserType", "eUserLogintype", "sUserFirstname", "sUserLastname", "sUserLoginname", "eUserEzsignaccess", "dtUserLastlogondate", "dtUserPasswordchanged", "dtUserEzsignprepaidexpiration", "bUserIsactive", "bUserValidatebyadministration", "bUserValidatebydirector", "bUserAttachmentautoverified", "bUserChangepassword", "objAudit"]

    @validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w\.-]+@[\w\.-]+\.\w{2,4})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w\.-]+@[\w\.-]+\.\w{2,4})|([a-zA-Z0-9]){1,32})$/")
        return value

    @validator('dt_user_lastlogondate')
    def dt_user_lastlogondate_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @validator('dt_user_passwordchanged')
    def dt_user_passwordchanged_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @validator('dt_user_ezsignprepaidexpiration')
    def dt_user_ezsignprepaidexpiration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
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
    def from_json(cls, json_str: str) -> UserResponse:
        """Create an instance of UserResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_email
        if self.obj_email:
            _dict['objEmail'] = self.obj_email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_home
        if self.obj_phone_home:
            _dict['objPhoneHome'] = self.obj_phone_home.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_sms
        if self.obj_phone_sms:
            _dict['objPhoneSMS'] = self.obj_phone_sms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserResponse:
        """Create an instance of UserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserResponse.parse_obj(obj)

        _obj = UserResponse.parse_obj({
            "pki_user_id": obj.get("pkiUserID"),
            "fki_agent_id": obj.get("fkiAgentID"),
            "fki_broker_id": obj.get("fkiBrokerID"),
            "fki_assistant_id": obj.get("fkiAssistantID"),
            "fki_employee_id": obj.get("fkiEmployeeID"),
            "fki_company_id_default": obj.get("fkiCompanyIDDefault"),
            "s_company_name_x": obj.get("sCompanyNameX"),
            "fki_department_id_default": obj.get("fkiDepartmentIDDefault"),
            "s_department_name_x": obj.get("sDepartmentNameX"),
            "fki_timezone_id": obj.get("fkiTimezoneID"),
            "s_timezone_name": obj.get("sTimezoneName"),
            "fki_language_id": obj.get("fkiLanguageID"),
            "s_language_name_x": obj.get("sLanguageNameX"),
            "obj_email": EmailResponseCompound.from_dict(obj.get("objEmail")) if obj.get("objEmail") is not None else None,
            "fki_billingentityinternal_id": obj.get("fkiBillingentityinternalID"),
            "s_billingentityinternal_description_x": obj.get("sBillingentityinternalDescriptionX"),
            "obj_phone_home": PhoneResponseCompound.from_dict(obj.get("objPhoneHome")) if obj.get("objPhoneHome") is not None else None,
            "obj_phone_sms": PhoneResponseCompound.from_dict(obj.get("objPhoneSMS")) if obj.get("objPhoneSMS") is not None else None,
            "fki_secretquestion_id": obj.get("fkiSecretquestionID"),
            "fki_module_id_form": obj.get("fkiModuleIDForm"),
            "s_module_name_x": obj.get("sModuleNameX"),
            "e_user_origin": obj.get("eUserOrigin"),
            "e_user_type": obj.get("eUserType"),
            "e_user_logintype": obj.get("eUserLogintype"),
            "s_user_firstname": obj.get("sUserFirstname"),
            "s_user_lastname": obj.get("sUserLastname"),
            "s_user_loginname": obj.get("sUserLoginname"),
            "e_user_ezsignaccess": obj.get("eUserEzsignaccess"),
            "dt_user_lastlogondate": obj.get("dtUserLastlogondate"),
            "dt_user_passwordchanged": obj.get("dtUserPasswordchanged"),
            "dt_user_ezsignprepaidexpiration": obj.get("dtUserEzsignprepaidexpiration"),
            "b_user_isactive": obj.get("bUserIsactive"),
            "b_user_validatebyadministration": obj.get("bUserValidatebyadministration"),
            "b_user_validatebydirector": obj.get("bUserValidatebydirector"),
            "b_user_attachmentautoverified": obj.get("bUserAttachmentautoverified"),
            "b_user_changepassword": obj.get("bUserChangepassword"),
            "obj_audit": CommonAudit.from_dict(obj.get("objAudit")) if obj.get("objAudit") is not None else None
        })
        return _obj


