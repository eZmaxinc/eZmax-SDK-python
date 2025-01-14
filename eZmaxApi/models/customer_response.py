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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_customer_marketingcorrespondence import FieldECustomerMarketingcorrespondence
from eZmaxApi.models.field_e_customer_type import FieldECustomerType
from typing import Optional, Set
from typing_extensions import Self

class CustomerResponse(BaseModel):
    """
    A Customer Object
    """ # noqa: E501
    pki_customer_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Customer.", alias="pkiCustomerID")
    fki_company_id: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The unique ID of the Company", alias="fkiCompanyID")
    fki_customergroup_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Customergroup", alias="fkiCustomergroupID")
    s_customer_name: Annotated[str, Field(strict=True)] = Field(description="The name of the Customer", alias="sCustomerName")
    fki_contactinformations_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Contactinformations", alias="fkiContactinformationsID")
    fki_contactcontainer_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Contactcontainer", alias="fkiContactcontainerID")
    fki_image_id: StrictInt = Field(description="The unique ID of the Image", alias="fkiImageID")
    fki_glaccountcontainer_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Glaccountcontainer", alias="fkiGlaccountcontainerID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    fki_department_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Department", alias="fkiDepartmentID")
    fki_paymentmethod_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Paymentmethod", alias="fkiPaymentmethodID")
    fki_electronicfundstransferbankaccount_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Electronicfundstransferbankaccount", alias="fkiElectronicfundstransferbankaccountID")
    fki_electronicfundstransferbankaccount_id_directdebit: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Electronicfundstransferbankaccount", alias="fkiElectronicfundstransferbankaccountIDDirectdebit")
    fki_sendingmethod_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Sendingmethod", alias="fkiSendingmethodID")
    fki_taxassignment_id: Annotated[int, Field(le=15, strict=True, ge=0)] = Field(description="The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable|", alias="fkiTaxassignmentID")
    fki_attendancestatus_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Attendancestatus", alias="fkiAttendancestatusID")
    fki_agent_id_variableexpensechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Agent.", alias="fkiAgentIDVariableexpensechargeto")
    fki_broker_id_variableexpensechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Broker.", alias="fkiBrokerIDVariableexpensechargeto")
    fki_customer_id_variableexpensechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Customer.", alias="fkiCustomerIDVariableexpensechargeto")
    fki_glaccountcontainer_id_variableexpensechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Glaccountcontainer", alias="fkiGlaccountcontainerIDVariableexpensechargeto")
    fki_agent_id_supplychargechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Agent.", alias="fkiAgentIDSupplychargechargeto")
    fki_broker_id_supplychargechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Broker.", alias="fkiBrokerIDSupplychargechargeto")
    fki_customer_id_supplychargechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Customer.", alias="fkiCustomerIDSupplychargechargeto")
    fki_glaccountcontainer_id_supplychargechargeto: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Glaccountcontainer", alias="fkiGlaccountcontainerIDSupplychargechargeto")
    fki_invoicealternatelogo_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Invoicealternatelogo", alias="fkiInvoicealternatelogoID")
    fki_synchronizationlinkserver_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Synchronizationlinkserver", alias="fkiSynchronizationlinkserverID")
    efki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="efkiUserID")
    efks_customer_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The code of the Customer", alias="efksCustomerCode")
    s_customer_code: Annotated[str, Field(strict=True)] = Field(description="The code of the Customer", alias="sCustomerCode")
    d_customer_fulltimeequivalent: Annotated[str, Field(strict=True)] = Field(description="The fulltimeequivalent of the Customer", alias="dCustomerFulltimeequivalent")
    i_customer_photocopiercode: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The photocopiercode of the Customer", alias="iCustomerPhotocopiercode")
    i_customer_longdistancecode: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The longdistancecode of the Customer", alias="iCustomerLongdistancecode")
    i_customer_timewindowstart: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The timewindowstart of the Customer", alias="iCustomerTimewindowstart")
    i_customer_timewindowend: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The timewindowend of the Customer", alias="iCustomerTimewindowend")
    d_customer_minimumchargeableinterests: Annotated[str, Field(strict=True)] = Field(description="The minimumchargeableinterests of the Customer", alias="dCustomerMinimumchargeableinterests")
    dt_customer_birthdate: Annotated[str, Field(strict=True)] = Field(description="The birthdate of the Customer", alias="dtCustomerBirthdate")
    dt_customer_transfer: Annotated[str, Field(strict=True)] = Field(description="The transfer of the Customer", alias="dtCustomerTransfer")
    dt_customer_transferappointment: Annotated[str, Field(strict=True)] = Field(description="The transferappointment of the Customer", alias="dtCustomerTransferappointment")
    dt_customer_transfersurvey: Annotated[str, Field(strict=True)] = Field(description="The transfersurvey of the Customer", alias="dtCustomerTransfersurvey")
    b_customer_isactive: StrictBool = Field(description="Whether the customer is active or not", alias="bCustomerIsactive")
    b_customer_variableexpensefinanced: StrictBool = Field(description="Whether if it's an variableexpensefinanced", alias="bCustomerVariableexpensefinanced")
    b_customer_variableexpensefinancedtaxes: StrictBool = Field(description="Whether if it's an variableexpensefinancedtaxes", alias="bCustomerVariableexpensefinancedtaxes")
    b_customer_supplychargefinanced: StrictBool = Field(description="Whether if it's an supplychargefinanced", alias="bCustomerSupplychargefinanced")
    b_customer_supplychargefinancedtaxes: StrictBool = Field(description="Whether if it's an supplychargefinancedtaxes", alias="bCustomerSupplychargefinancedtaxes")
    b_customer_attendance: StrictBool = Field(description="Whether if it's an attendance", alias="bCustomerAttendance")
    e_customer_type: FieldECustomerType = Field(alias="eCustomerType")
    e_customer_marketingcorrespondence: FieldECustomerMarketingcorrespondence = Field(alias="eCustomerMarketingcorrespondence")
    b_customer_blackcopycarbon: StrictBool = Field(description="Whether if it's an blackcopycarbon", alias="bCustomerBlackcopycarbon")
    b_customer_unsubscribeinfo: StrictBool = Field(description="Whether if it's an unsubscribeinfo", alias="bCustomerUnsubscribeinfo")
    t_customer_comment: Annotated[str, Field(strict=True)] = Field(description="The comment of the Customer", alias="tCustomerComment")
    importid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="IMPORTID")
    __properties: ClassVar[List[str]] = ["pkiCustomerID", "fkiCompanyID", "fkiCustomergroupID", "sCustomerName", "fkiContactinformationsID", "fkiContactcontainerID", "fkiImageID", "fkiGlaccountcontainerID", "fkiLanguageID", "fkiDepartmentID", "fkiPaymentmethodID", "fkiElectronicfundstransferbankaccountID", "fkiElectronicfundstransferbankaccountIDDirectdebit", "fkiSendingmethodID", "fkiTaxassignmentID", "fkiAttendancestatusID", "fkiAgentIDVariableexpensechargeto", "fkiBrokerIDVariableexpensechargeto", "fkiCustomerIDVariableexpensechargeto", "fkiGlaccountcontainerIDVariableexpensechargeto", "fkiAgentIDSupplychargechargeto", "fkiBrokerIDSupplychargechargeto", "fkiCustomerIDSupplychargechargeto", "fkiGlaccountcontainerIDSupplychargechargeto", "fkiInvoicealternatelogoID", "fkiSynchronizationlinkserverID", "efkiUserID", "efksCustomerCode", "sCustomerCode", "dCustomerFulltimeequivalent", "iCustomerPhotocopiercode", "iCustomerLongdistancecode", "iCustomerTimewindowstart", "iCustomerTimewindowend", "dCustomerMinimumchargeableinterests", "dtCustomerBirthdate", "dtCustomerTransfer", "dtCustomerTransferappointment", "dtCustomerTransfersurvey", "bCustomerIsactive", "bCustomerVariableexpensefinanced", "bCustomerVariableexpensefinancedtaxes", "bCustomerSupplychargefinanced", "bCustomerSupplychargefinancedtaxes", "bCustomerAttendance", "eCustomerType", "eCustomerMarketingcorrespondence", "bCustomerBlackcopycarbon", "bCustomerUnsubscribeinfo", "tCustomerComment", "IMPORTID"]

    @field_validator('s_customer_name')
    def s_customer_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('efks_customer_code')
    def efks_customer_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,6}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,6}$/")
        return value

    @field_validator('s_customer_code')
    def s_customer_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,6}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,6}$/")
        return value

    @field_validator('d_customer_fulltimeequivalent')
    def d_customer_fulltimeequivalent_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,3}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,3}?\.[\d]{2}$/")
        return value

    @field_validator('d_customer_minimumchargeableinterests')
    def d_customer_minimumchargeableinterests_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
        return value

    @field_validator('dt_customer_birthdate')
    def dt_customer_birthdate_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
        return value

    @field_validator('dt_customer_transfer')
    def dt_customer_transfer_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('dt_customer_transferappointment')
    def dt_customer_transferappointment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('dt_customer_transfersurvey')
    def dt_customer_transfersurvey_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('t_customer_comment')
    def t_customer_comment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,16777215}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,16777215}$/")
        return value

    @field_validator('importid')
    def importid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,15}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,15}$/")
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
        """Create an instance of CustomerResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiCustomerID": obj.get("pkiCustomerID"),
            "fkiCompanyID": obj.get("fkiCompanyID"),
            "fkiCustomergroupID": obj.get("fkiCustomergroupID"),
            "sCustomerName": obj.get("sCustomerName"),
            "fkiContactinformationsID": obj.get("fkiContactinformationsID"),
            "fkiContactcontainerID": obj.get("fkiContactcontainerID"),
            "fkiImageID": obj.get("fkiImageID"),
            "fkiGlaccountcontainerID": obj.get("fkiGlaccountcontainerID"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "fkiDepartmentID": obj.get("fkiDepartmentID"),
            "fkiPaymentmethodID": obj.get("fkiPaymentmethodID"),
            "fkiElectronicfundstransferbankaccountID": obj.get("fkiElectronicfundstransferbankaccountID"),
            "fkiElectronicfundstransferbankaccountIDDirectdebit": obj.get("fkiElectronicfundstransferbankaccountIDDirectdebit"),
            "fkiSendingmethodID": obj.get("fkiSendingmethodID"),
            "fkiTaxassignmentID": obj.get("fkiTaxassignmentID"),
            "fkiAttendancestatusID": obj.get("fkiAttendancestatusID"),
            "fkiAgentIDVariableexpensechargeto": obj.get("fkiAgentIDVariableexpensechargeto"),
            "fkiBrokerIDVariableexpensechargeto": obj.get("fkiBrokerIDVariableexpensechargeto"),
            "fkiCustomerIDVariableexpensechargeto": obj.get("fkiCustomerIDVariableexpensechargeto"),
            "fkiGlaccountcontainerIDVariableexpensechargeto": obj.get("fkiGlaccountcontainerIDVariableexpensechargeto"),
            "fkiAgentIDSupplychargechargeto": obj.get("fkiAgentIDSupplychargechargeto"),
            "fkiBrokerIDSupplychargechargeto": obj.get("fkiBrokerIDSupplychargechargeto"),
            "fkiCustomerIDSupplychargechargeto": obj.get("fkiCustomerIDSupplychargechargeto"),
            "fkiGlaccountcontainerIDSupplychargechargeto": obj.get("fkiGlaccountcontainerIDSupplychargechargeto"),
            "fkiInvoicealternatelogoID": obj.get("fkiInvoicealternatelogoID"),
            "fkiSynchronizationlinkserverID": obj.get("fkiSynchronizationlinkserverID"),
            "efkiUserID": obj.get("efkiUserID"),
            "efksCustomerCode": obj.get("efksCustomerCode"),
            "sCustomerCode": obj.get("sCustomerCode"),
            "dCustomerFulltimeequivalent": obj.get("dCustomerFulltimeequivalent"),
            "iCustomerPhotocopiercode": obj.get("iCustomerPhotocopiercode"),
            "iCustomerLongdistancecode": obj.get("iCustomerLongdistancecode"),
            "iCustomerTimewindowstart": obj.get("iCustomerTimewindowstart"),
            "iCustomerTimewindowend": obj.get("iCustomerTimewindowend"),
            "dCustomerMinimumchargeableinterests": obj.get("dCustomerMinimumchargeableinterests"),
            "dtCustomerBirthdate": obj.get("dtCustomerBirthdate"),
            "dtCustomerTransfer": obj.get("dtCustomerTransfer"),
            "dtCustomerTransferappointment": obj.get("dtCustomerTransferappointment"),
            "dtCustomerTransfersurvey": obj.get("dtCustomerTransfersurvey"),
            "bCustomerIsactive": obj.get("bCustomerIsactive"),
            "bCustomerVariableexpensefinanced": obj.get("bCustomerVariableexpensefinanced"),
            "bCustomerVariableexpensefinancedtaxes": obj.get("bCustomerVariableexpensefinancedtaxes"),
            "bCustomerSupplychargefinanced": obj.get("bCustomerSupplychargefinanced"),
            "bCustomerSupplychargefinancedtaxes": obj.get("bCustomerSupplychargefinancedtaxes"),
            "bCustomerAttendance": obj.get("bCustomerAttendance"),
            "eCustomerType": obj.get("eCustomerType"),
            "eCustomerMarketingcorrespondence": obj.get("eCustomerMarketingcorrespondence"),
            "bCustomerBlackcopycarbon": obj.get("bCustomerBlackcopycarbon"),
            "bCustomerUnsubscribeinfo": obj.get("bCustomerUnsubscribeinfo"),
            "tCustomerComment": obj.get("tCustomerComment"),
            "IMPORTID": obj.get("IMPORTID")
        })
        return _obj


