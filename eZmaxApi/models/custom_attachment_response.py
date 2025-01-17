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
from eZmaxApi.models.attachment_response_compound import AttachmentResponseCompound
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.field_e_attachment_documenttype import FieldEAttachmentDocumenttype
from eZmaxApi.models.field_e_attachment_privacy import FieldEAttachmentPrivacy
from eZmaxApi.models.field_e_attachment_type import FieldEAttachmentType
from eZmaxApi.models.field_e_attachment_verified import FieldEAttachmentVerified
from typing import Optional, Set
from typing_extensions import Self

class CustomAttachmentResponse(BaseModel):
    """
    A Custom Attachment Object
    """ # noqa: E501
    pki_attachment_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Attachment.", alias="pkiAttachmentID")
    fki_computer_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Computer", alias="fkiComputerID")
    fki_adjustment_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Adjustment", alias="fkiAdjustmentID")
    fki_agent_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Agent.", alias="fkiAgentID")
    fki_bankaccount_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Bankaccount", alias="fkiBankaccountID")
    fki_broker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Broker.", alias="fkiBrokerID")
    fki_commissionadvance_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Commissionadvance", alias="fkiCommissionadvanceID")
    fki_communication_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Communication.", alias="fkiCommunicationID")
    fki_customer_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Customer.", alias="fkiCustomerID")
    fki_customertemplate_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Customertemplate", alias="fkiCustomertemplateID")
    fki_deposit_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Deposit", alias="fkiDepositID")
    fki_deposittransitcheque_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Deposittransitcheque", alias="fkiDeposittransitchequeID")
    fki_electronicfundstransfer_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Electronicfundstransfer", alias="fkiElectronicfundstransferID")
    fki_employee_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Employee.", alias="fkiEmployeeID")
    fki_externalbroker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Externalbroker.", alias="fkiExternalbrokerID")
    fki_ezcomadvanceserver_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezcomadvanceserver", alias="fkiEzcomadvanceserverID")
    fki_ezcomcompany_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezcomcompany", alias="fkiEzcomcompanyID")
    fki_ezsigndocument_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentID")
    fki_ghacqcontract_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ghacqcontract", alias="fkiGhacqcontractID")
    fki_inscription_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Inscription.", alias="fkiInscriptionID")
    fki_inscriptiontemp_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Inscriptiontemp", alias="fkiInscriptiontempID")
    fki_inscriptionnotauthenticated_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Inscriptionnotauthenticated.", alias="fkiInscriptionnotauthenticatedID")
    fki_invoice_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Invoice.", alias="fkiInvoiceID")
    fki_buyercontract_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Buyercontract", alias="fkiBuyercontractID")
    fki_franchisebroker_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisebroker", alias="fkiFranchisebrokerID")
    fki_franchiseagence_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchiseagence", alias="fkiFranchiseagenceID")
    fki_franchiseoffice_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisereoffice", alias="fkiFranchiseofficeID")
    fki_franchisefranchise_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisefranchise", alias="fkiFranchisefranchiseID")
    fki_franchisecomplaint_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisecomplaint", alias="fkiFranchisecomplaintID")
    fki_lead_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Lead", alias="fkiLeadID")
    fki_marketingprogram_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Marketingprogram", alias="fkiMarketingprogramID")
    fki_marketingfollow_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Marketingfollow", alias="fkiMarketingfollowID")
    fki_notary_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Notary.", alias="fkiNotaryID")
    fki_officetaxreport_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Officetaxreport", alias="fkiOfficetaxreportID")
    fki_otherincome_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Otherincome", alias="fkiOtherincomeID")
    fki_paymentpreparation_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Paymentpreparation", alias="fkiPaymentpreparationID")
    fki_purchase_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the Purchase", alias="fkiPurchaseID")
    fki_salary_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Salary", alias="fkiSalaryID")
    fki_supplier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Supplier.", alias="fkiSupplierID")
    fki_tranqcontract_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Tranqcontract", alias="fkiTranqcontractID")
    fki_template_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Template", alias="fkiTemplateID")
    fki_inscriptionchecklist_id: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Inscriptionchecklist", alias="fkiInscriptionchecklistID")
    fki_folder_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Folder", alias="fkiFolderID")
    fki_rejectedoffertopurchase_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Rejectedoffertopurchase", alias="fkiRejectedoffertopurchaseID")
    fki_disclosure_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Disclosure", alias="fkiDisclosureID")
    fki_reconciliation_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Reconciliation", alias="fkiReconciliationID")
    fki_ezsigndocument_id_reference: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentIDReference")
    e_attachment_documenttype: FieldEAttachmentDocumenttype = Field(alias="eAttachmentDocumenttype")
    s_attachment_name: Annotated[str, Field(strict=True)] = Field(description="The name of the Attachment", alias="sAttachmentName")
    e_attachment_privacy: FieldEAttachmentPrivacy = Field(alias="eAttachmentPrivacy")
    fki_user_id_specific: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserIDSpecific")
    e_attachment_type: FieldEAttachmentType = Field(alias="eAttachmentType")
    i_attachment_size: Annotated[int, Field(le=4294967295, strict=True, ge=0)] = Field(description="The size of the Attachment", alias="iAttachmentSize")
    i_attachment_ed_mmoduleflag: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The edmmoduleflag of the Attachment", alias="iAttachmentEDMmoduleflag")
    s_attachment_md5: Annotated[str, Field(strict=True)] = Field(description="The md5 of the Attachment", alias="sAttachmentMD5")
    b_attachment_deleted: StrictBool = Field(description="Whether if it's deleted", alias="bAttachmentDeleted")
    b_attachment_valid: StrictBool = Field(description="Whether if it's valid", alias="bAttachmentValid")
    e_attachment_verified: FieldEAttachmentVerified = Field(alias="eAttachmentVerified")
    t_attachment_rejectioncomment: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The rejectioncomment of the Attachment", alias="tAttachmentRejectioncomment")
    fki_user_id_owner: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserIDOwner")
    obj_audit: Optional[CommonAudit] = Field(default=None, alias="objAudit")
    obj_attachment_proof: Optional[AttachmentResponseCompound] = Field(default=None, alias="objAttachmentProof")
    obj_attachment_proofdocument: Optional[AttachmentResponseCompound] = Field(default=None, alias="objAttachmentProofdocument")
    a_obj_attachment_attachment: Optional[List[AttachmentResponseCompound]] = Field(default=None, alias="a_objAttachmentAttachment")
    a_obj_attachment_version: Optional[List[AttachmentResponseCompound]] = Field(default=None, alias="a_objAttachmentVersion")
    __properties: ClassVar[List[str]] = ["pkiAttachmentID", "fkiComputerID", "fkiAdjustmentID", "fkiAgentID", "fkiBankaccountID", "fkiBrokerID", "fkiCommissionadvanceID", "fkiCommunicationID", "fkiCustomerID", "fkiCustomertemplateID", "fkiDepositID", "fkiDeposittransitchequeID", "fkiElectronicfundstransferID", "fkiEmployeeID", "fkiExternalbrokerID", "fkiEzcomadvanceserverID", "fkiEzcomcompanyID", "fkiEzsigndocumentID", "fkiGhacqcontractID", "fkiInscriptionID", "fkiInscriptiontempID", "fkiInscriptionnotauthenticatedID", "fkiInvoiceID", "fkiBuyercontractID", "fkiFranchisebrokerID", "fkiFranchiseagenceID", "fkiFranchiseofficeID", "fkiFranchisefranchiseID", "fkiFranchisecomplaintID", "fkiLeadID", "fkiMarketingprogramID", "fkiMarketingfollowID", "fkiNotaryID", "fkiOfficetaxreportID", "fkiOtherincomeID", "fkiPaymentpreparationID", "fkiPurchaseID", "fkiSalaryID", "fkiSupplierID", "fkiTranqcontractID", "fkiTemplateID", "fkiInscriptionchecklistID", "fkiFolderID", "fkiRejectedoffertopurchaseID", "fkiDisclosureID", "fkiReconciliationID", "fkiEzsigndocumentIDReference", "eAttachmentDocumenttype", "sAttachmentName", "eAttachmentPrivacy", "fkiUserIDSpecific", "eAttachmentType", "iAttachmentSize", "iAttachmentEDMmoduleflag", "sAttachmentMD5", "bAttachmentDeleted", "bAttachmentValid", "eAttachmentVerified", "tAttachmentRejectioncomment", "fkiUserIDOwner", "objAudit", "objAttachmentProof", "objAttachmentProofdocument", "a_objAttachmentAttachment", "a_objAttachmentVersion"]

    @field_validator('s_attachment_name')
    def s_attachment_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,75}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,75}$/")
        return value

    @field_validator('s_attachment_md5')
    def s_attachment_md5_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,32}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,32}$/")
        return value

    @field_validator('t_attachment_rejectioncomment')
    def t_attachment_rejectioncomment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,65535}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,65535}$/")
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
        """Create an instance of CustomAttachmentResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_attachment_proof
        if self.obj_attachment_proof:
            _dict['objAttachmentProof'] = self.obj_attachment_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_attachment_proofdocument
        if self.obj_attachment_proofdocument:
            _dict['objAttachmentProofdocument'] = self.obj_attachment_proofdocument.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_attachment_attachment (list)
        _items = []
        if self.a_obj_attachment_attachment:
            for _item_a_obj_attachment_attachment in self.a_obj_attachment_attachment:
                if _item_a_obj_attachment_attachment:
                    _items.append(_item_a_obj_attachment_attachment.to_dict())
            _dict['a_objAttachmentAttachment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_attachment_version (list)
        _items = []
        if self.a_obj_attachment_version:
            for _item_a_obj_attachment_version in self.a_obj_attachment_version:
                if _item_a_obj_attachment_version:
                    _items.append(_item_a_obj_attachment_version.to_dict())
            _dict['a_objAttachmentVersion'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomAttachmentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiAttachmentID": obj.get("pkiAttachmentID"),
            "fkiComputerID": obj.get("fkiComputerID"),
            "fkiAdjustmentID": obj.get("fkiAdjustmentID"),
            "fkiAgentID": obj.get("fkiAgentID"),
            "fkiBankaccountID": obj.get("fkiBankaccountID"),
            "fkiBrokerID": obj.get("fkiBrokerID"),
            "fkiCommissionadvanceID": obj.get("fkiCommissionadvanceID"),
            "fkiCommunicationID": obj.get("fkiCommunicationID"),
            "fkiCustomerID": obj.get("fkiCustomerID"),
            "fkiCustomertemplateID": obj.get("fkiCustomertemplateID"),
            "fkiDepositID": obj.get("fkiDepositID"),
            "fkiDeposittransitchequeID": obj.get("fkiDeposittransitchequeID"),
            "fkiElectronicfundstransferID": obj.get("fkiElectronicfundstransferID"),
            "fkiEmployeeID": obj.get("fkiEmployeeID"),
            "fkiExternalbrokerID": obj.get("fkiExternalbrokerID"),
            "fkiEzcomadvanceserverID": obj.get("fkiEzcomadvanceserverID"),
            "fkiEzcomcompanyID": obj.get("fkiEzcomcompanyID"),
            "fkiEzsigndocumentID": obj.get("fkiEzsigndocumentID"),
            "fkiGhacqcontractID": obj.get("fkiGhacqcontractID"),
            "fkiInscriptionID": obj.get("fkiInscriptionID"),
            "fkiInscriptiontempID": obj.get("fkiInscriptiontempID"),
            "fkiInscriptionnotauthenticatedID": obj.get("fkiInscriptionnotauthenticatedID"),
            "fkiInvoiceID": obj.get("fkiInvoiceID"),
            "fkiBuyercontractID": obj.get("fkiBuyercontractID"),
            "fkiFranchisebrokerID": obj.get("fkiFranchisebrokerID"),
            "fkiFranchiseagenceID": obj.get("fkiFranchiseagenceID"),
            "fkiFranchiseofficeID": obj.get("fkiFranchiseofficeID"),
            "fkiFranchisefranchiseID": obj.get("fkiFranchisefranchiseID"),
            "fkiFranchisecomplaintID": obj.get("fkiFranchisecomplaintID"),
            "fkiLeadID": obj.get("fkiLeadID"),
            "fkiMarketingprogramID": obj.get("fkiMarketingprogramID"),
            "fkiMarketingfollowID": obj.get("fkiMarketingfollowID"),
            "fkiNotaryID": obj.get("fkiNotaryID"),
            "fkiOfficetaxreportID": obj.get("fkiOfficetaxreportID"),
            "fkiOtherincomeID": obj.get("fkiOtherincomeID"),
            "fkiPaymentpreparationID": obj.get("fkiPaymentpreparationID"),
            "fkiPurchaseID": obj.get("fkiPurchaseID"),
            "fkiSalaryID": obj.get("fkiSalaryID"),
            "fkiSupplierID": obj.get("fkiSupplierID"),
            "fkiTranqcontractID": obj.get("fkiTranqcontractID"),
            "fkiTemplateID": obj.get("fkiTemplateID"),
            "fkiInscriptionchecklistID": obj.get("fkiInscriptionchecklistID"),
            "fkiFolderID": obj.get("fkiFolderID"),
            "fkiRejectedoffertopurchaseID": obj.get("fkiRejectedoffertopurchaseID"),
            "fkiDisclosureID": obj.get("fkiDisclosureID"),
            "fkiReconciliationID": obj.get("fkiReconciliationID"),
            "fkiEzsigndocumentIDReference": obj.get("fkiEzsigndocumentIDReference"),
            "eAttachmentDocumenttype": obj.get("eAttachmentDocumenttype"),
            "sAttachmentName": obj.get("sAttachmentName"),
            "eAttachmentPrivacy": obj.get("eAttachmentPrivacy"),
            "fkiUserIDSpecific": obj.get("fkiUserIDSpecific"),
            "eAttachmentType": obj.get("eAttachmentType"),
            "iAttachmentSize": obj.get("iAttachmentSize"),
            "iAttachmentEDMmoduleflag": obj.get("iAttachmentEDMmoduleflag"),
            "sAttachmentMD5": obj.get("sAttachmentMD5"),
            "bAttachmentDeleted": obj.get("bAttachmentDeleted"),
            "bAttachmentValid": obj.get("bAttachmentValid"),
            "eAttachmentVerified": obj.get("eAttachmentVerified"),
            "tAttachmentRejectioncomment": obj.get("tAttachmentRejectioncomment"),
            "fkiUserIDOwner": obj.get("fkiUserIDOwner"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "objAttachmentProof": AttachmentResponseCompound.from_dict(obj["objAttachmentProof"]) if obj.get("objAttachmentProof") is not None else None,
            "objAttachmentProofdocument": AttachmentResponseCompound.from_dict(obj["objAttachmentProofdocument"]) if obj.get("objAttachmentProofdocument") is not None else None,
            "a_objAttachmentAttachment": [AttachmentResponseCompound.from_dict(_item) for _item in obj["a_objAttachmentAttachment"]] if obj.get("a_objAttachmentAttachment") is not None else None,
            "a_objAttachmentVersion": [AttachmentResponseCompound.from_dict(_item) for _item in obj["a_objAttachmentVersion"]] if obj.get("a_objAttachmentVersion") is not None else None
        })
        return _obj


