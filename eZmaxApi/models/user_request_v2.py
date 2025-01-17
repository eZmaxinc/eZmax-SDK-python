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
from eZmaxApi.models.email_request import EmailRequest
from eZmaxApi.models.field_e_user_ezsignaccess import FieldEUserEzsignaccess
from eZmaxApi.models.field_e_user_logintype import FieldEUserLogintype
from eZmaxApi.models.field_e_user_type import FieldEUserType
from eZmaxApi.models.phone_request_v2 import PhoneRequestV2
from typing import Optional, Set
from typing_extensions import Self

class UserRequestV2(BaseModel):
    """
    A User Object
    """ # noqa: E501
    pki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="pkiUserID")
    fki_agent_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Agent.", alias="fkiAgentID")
    fki_broker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Broker.", alias="fkiBrokerID")
    fki_assistant_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Assistant.", alias="fkiAssistantID")
    fki_employee_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Employee.", alias="fkiEmployeeID")
    fki_company_id_default: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The unique ID of the Company", alias="fkiCompanyIDDefault")
    fki_department_id_default: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Department", alias="fkiDepartmentIDDefault")
    fki_timezone_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Timezone", alias="fkiTimezoneID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    obj_email: EmailRequest = Field(description="An Email Object and children to create a complete structure", alias="objEmail")
    fki_billingentityinternal_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    obj_phone_home: Optional[PhoneRequestV2] = Field(default=None, description="A Phone Object and children to create a complete structure", alias="objPhoneHome")
    obj_phone_sms: Optional[PhoneRequestV2] = Field(default=None, description="A Phone Object and children to create a complete structure", alias="objPhoneSMS")
    fki_secretquestion_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Secretquestion.  Valid values:  |Value|Description| |-|-| |1|The name of the hospital in which you were born| |2|The name of your grade school| |3|The last name of your favorite teacher| |4|Your favorite sports team| |5|Your favorite TV show| |6|Your favorite movie| |7|The name of the street on which you grew up| |8|The name of your first employer| |9|Your first car| |10|Your favorite food| |11|The name of your first pet| |12|Favorite musician/band| |13|What instrument you play| |14|Your father's middle name| |15|Your mother's maiden name| |16|Name of your eldest child| |17|Your spouse's middle name| |18|Favorite restaurant| |19|Childhood nickname| |20|Favorite vacation destination| |21|Your boat's name| |22|Date of Birth (YYYY-MM-DD)| |22|Secret Code| |22|Your reference code|", alias="fkiSecretquestionID")
    s_user_secretresponse: Optional[StrictStr] = Field(default=None, description="The answer to the Secretquestion", alias="sUserSecretresponse")
    fki_module_id_form: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Module", alias="fkiModuleIDForm")
    e_user_type: FieldEUserType = Field(alias="eUserType")
    e_user_logintype: FieldEUserLogintype = Field(alias="eUserLogintype")
    s_user_firstname: StrictStr = Field(description="The first name of the user", alias="sUserFirstname")
    s_user_lastname: StrictStr = Field(description="The last name of the user", alias="sUserLastname")
    s_user_loginname: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginname")
    s_user_jobtitle: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The job title of the user", alias="sUserJobtitle")
    e_user_ezsignaccess: FieldEUserEzsignaccess = Field(alias="eUserEzsignaccess")
    b_user_isactive: StrictBool = Field(description="Whether the User is active or not", alias="bUserIsactive")
    b_user_validatebyadministration: Optional[StrictBool] = Field(default=None, description="Whether if the transactions in which the User is implicated must be validated by administrative personnel or not", alias="bUserValidatebyadministration")
    b_user_validatebydirector: Optional[StrictBool] = Field(default=None, description="Whether if the transactions in which the User is implicated must be validated by a director or not", alias="bUserValidatebydirector")
    b_user_attachmentautoverified: Optional[StrictBool] = Field(default=None, description="Whether if Attachments uploaded by the User must be validated or not", alias="bUserAttachmentautoverified")
    b_user_changepassword: Optional[StrictBool] = Field(default=None, description="Whether if the User is forced to change its password", alias="bUserChangepassword")
    __properties: ClassVar[List[str]] = ["pkiUserID", "fkiAgentID", "fkiBrokerID", "fkiAssistantID", "fkiEmployeeID", "fkiCompanyIDDefault", "fkiDepartmentIDDefault", "fkiTimezoneID", "fkiLanguageID", "objEmail", "fkiBillingentityinternalID", "objPhoneHome", "objPhoneSMS", "fkiSecretquestionID", "sUserSecretresponse", "fkiModuleIDForm", "eUserType", "eUserLogintype", "sUserFirstname", "sUserLastname", "sUserLoginname", "sUserJobtitle", "eUserEzsignaccess", "bUserIsactive", "bUserValidatebyadministration", "bUserValidatebydirector", "bUserAttachmentautoverified", "bUserChangepassword"]

    @field_validator('s_user_loginname')
    def s_user_loginname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w.%+\-!#$%&\'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w.%+\-!#$%&'*+\/=?^`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

    @field_validator('s_user_jobtitle')
    def s_user_jobtitle_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
        """Create an instance of UserRequestV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_email
        if self.obj_email:
            _dict['objEmail'] = self.obj_email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_home
        if self.obj_phone_home:
            _dict['objPhoneHome'] = self.obj_phone_home.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_phone_sms
        if self.obj_phone_sms:
            _dict['objPhoneSMS'] = self.obj_phone_sms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of UserRequestV2 from a dict"""


