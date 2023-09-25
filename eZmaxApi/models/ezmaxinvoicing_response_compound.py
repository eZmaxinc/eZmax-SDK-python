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
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_ezmaxinvoicing_ezsigndocument_response import CustomEzmaxinvoicingEzsigndocumentResponse
from eZmaxApi.models.custom_ezmaxinvoicing_ezsignfolder_response import CustomEzmaxinvoicingEzsignfolderResponse
from eZmaxApi.models.custom_ezmaxpricing_response import CustomEzmaxpricingResponse
from eZmaxApi.models.ezmaxinvoicingagent_response_compound import EzmaxinvoicingagentResponseCompound
from eZmaxApi.models.ezmaxinvoicingcontract_response_compound import EzmaxinvoicingcontractResponseCompound
from eZmaxApi.models.ezmaxinvoicingsummaryexternal_response_compound import EzmaxinvoicingsummaryexternalResponseCompound
from eZmaxApi.models.ezmaxinvoicingsummaryglobal_response_compound import EzmaxinvoicingsummaryglobalResponseCompound
from eZmaxApi.models.ezmaxinvoicingsummaryinternal_response_compound import EzmaxinvoicingsummaryinternalResponseCompound
from eZmaxApi.models.ezmaxinvoicinguser_response_compound import EzmaxinvoicinguserResponseCompound
from eZmaxApi.models.field_e_ezmaxinvoicing_paymenttype import FieldEEzmaxinvoicingPaymenttype

class EzmaxinvoicingResponseCompound(BaseModel):
    """
    A Ezmaxinvoicing Object  # noqa: E501
    """
    pki_ezmaxinvoicing_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="pkiEzmaxinvoicingID", description="The unique ID of the Ezmaxinvoicing")
    fki_ezmaxinvoicingcontract_id: conint(strict=True, ge=1) = Field(..., alias="fkiEzmaxinvoicingcontractID", description="The unique ID of the Ezmaxinvoicingcontract")
    fki_ezmaxpricing_id: conint(strict=True, ge=1) = Field(..., alias="fkiEzmaxpricingID", description="The unique ID of the Ezmaxpricing")
    fki_systemconfigurationtype_id: conint(strict=True, ge=1) = Field(..., alias="fkiSystemconfigurationtypeID", description="The unique ID of the Systemconfigurationtype")
    s_systemconfigurationtype_description_x: StrictStr = Field(..., alias="sSystemconfigurationtypeDescriptionX", description="The description of the Systemconfigurationtype in the language of the requester")
    yyyymm_ezmaxinvoicing: constr(strict=True, max_length=7) = Field(..., alias="yyyymmEzmaxinvoicing", description="The YYYYMM period of the Ezmaxinvoicing")
    i_ezmaxinvoicing_days: conint(strict=True, ge=1) = Field(..., alias="iEzmaxinvoicingDays", description="The number of days invoiced")
    e_ezmaxinvoicing_paymenttype: FieldEEzmaxinvoicingPaymenttype = Field(..., alias="eEzmaxinvoicingPaymenttype")
    d_ezmaxinvoicing_rebatepaymenttype: constr(strict=True) = Field(..., alias="dEzmaxinvoicingRebatepaymenttype", description="The percentage of rebate depending of the payment type")
    i_ezmaxinvoicing_contractlength: conint(strict=True, ge=1) = Field(..., alias="iEzmaxinvoicingContractlength", description="The length of the contract in years")
    d_ezmaxinvoicing_rebatecontractlength: constr(strict=True) = Field(..., alias="dEzmaxinvoicingRebatecontractlength", description="The percentage of rebate depending of the contract length")
    b_ezmaxinvoicing_rebate_ezsignallagents: StrictBool = Field(..., alias="bEzmaxinvoicingRebateEzsignallagents", description="Whether the rebate for eZsign is for all agents")
    obj_audit: Optional[CommonAudit] = Field(None, alias="objAudit")
    obj_ezmaxinvoicingcontract: EzmaxinvoicingcontractResponseCompound = Field(..., alias="objEzmaxinvoicingcontract")
    obj_ezmaxpricing: CustomEzmaxpricingResponse = Field(..., alias="objEzmaxpricing")
    a_obj_ezmaxinvoicingsummaryglobal: conlist(EzmaxinvoicingsummaryglobalResponseCompound) = Field(..., alias="a_objEzmaxinvoicingsummaryglobal")
    a_obj_ezmaxinvoicingsummaryexternal: conlist(EzmaxinvoicingsummaryexternalResponseCompound) = Field(..., alias="a_objEzmaxinvoicingsummaryexternal")
    a_obj_ezmaxinvoicingsummaryinternal: conlist(EzmaxinvoicingsummaryinternalResponseCompound) = Field(..., alias="a_objEzmaxinvoicingsummaryinternal")
    a_obj_ezmaxinvoicingagent: conlist(EzmaxinvoicingagentResponseCompound) = Field(..., alias="a_objEzmaxinvoicingagent")
    a_obj_ezmaxinvoicinguser: conlist(EzmaxinvoicinguserResponseCompound) = Field(..., alias="a_objEzmaxinvoicinguser")
    a_obj_ezmaxinvoicingezsignfolder: conlist(CustomEzmaxinvoicingEzsignfolderResponse) = Field(..., alias="a_objEzmaxinvoicingezsignfolder")
    a_obj_ezmaxinvoicingezsigndocument: conlist(CustomEzmaxinvoicingEzsigndocumentResponse) = Field(..., alias="a_objEzmaxinvoicingezsigndocument")
    __properties = ["pkiEzmaxinvoicingID", "fkiEzmaxinvoicingcontractID", "fkiEzmaxpricingID", "fkiSystemconfigurationtypeID", "sSystemconfigurationtypeDescriptionX", "yyyymmEzmaxinvoicing", "iEzmaxinvoicingDays", "eEzmaxinvoicingPaymenttype", "dEzmaxinvoicingRebatepaymenttype", "iEzmaxinvoicingContractlength", "dEzmaxinvoicingRebatecontractlength", "bEzmaxinvoicingRebateEzsignallagents", "objAudit", "objEzmaxinvoicingcontract", "objEzmaxpricing", "a_objEzmaxinvoicingsummaryglobal", "a_objEzmaxinvoicingsummaryexternal", "a_objEzmaxinvoicingsummaryinternal", "a_objEzmaxinvoicingagent", "a_objEzmaxinvoicinguser", "a_objEzmaxinvoicingezsignfolder", "a_objEzmaxinvoicingezsigndocument"]

    @validator('d_ezmaxinvoicing_rebatepaymenttype')
    def d_ezmaxinvoicing_rebatepaymenttype_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,3}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,3}?\.[\d]{2}$/")
        return value

    @validator('d_ezmaxinvoicing_rebatecontractlength')
    def d_ezmaxinvoicing_rebatecontractlength_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,3}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,3}?\.[\d]{2}$/")
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
    def from_json(cls, json_str: str) -> EzmaxinvoicingResponseCompound:
        """Create an instance of EzmaxinvoicingResponseCompound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezmaxinvoicingcontract
        if self.obj_ezmaxinvoicingcontract:
            _dict['objEzmaxinvoicingcontract'] = self.obj_ezmaxinvoicingcontract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezmaxpricing
        if self.obj_ezmaxpricing:
            _dict['objEzmaxpricing'] = self.obj_ezmaxpricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingsummaryglobal (list)
        _items = []
        if self.a_obj_ezmaxinvoicingsummaryglobal:
            for _item in self.a_obj_ezmaxinvoicingsummaryglobal:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingsummaryglobal'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingsummaryexternal (list)
        _items = []
        if self.a_obj_ezmaxinvoicingsummaryexternal:
            for _item in self.a_obj_ezmaxinvoicingsummaryexternal:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingsummaryexternal'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingsummaryinternal (list)
        _items = []
        if self.a_obj_ezmaxinvoicingsummaryinternal:
            for _item in self.a_obj_ezmaxinvoicingsummaryinternal:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingsummaryinternal'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingagent (list)
        _items = []
        if self.a_obj_ezmaxinvoicingagent:
            for _item in self.a_obj_ezmaxinvoicingagent:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingagent'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicinguser (list)
        _items = []
        if self.a_obj_ezmaxinvoicinguser:
            for _item in self.a_obj_ezmaxinvoicinguser:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicinguser'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingezsignfolder (list)
        _items = []
        if self.a_obj_ezmaxinvoicingezsignfolder:
            for _item in self.a_obj_ezmaxinvoicingezsignfolder:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingezsignfolder'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezmaxinvoicingezsigndocument (list)
        _items = []
        if self.a_obj_ezmaxinvoicingezsigndocument:
            for _item in self.a_obj_ezmaxinvoicingezsigndocument:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzmaxinvoicingezsigndocument'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzmaxinvoicingResponseCompound:
        """Create an instance of EzmaxinvoicingResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzmaxinvoicingResponseCompound.parse_obj(obj)

        _obj = EzmaxinvoicingResponseCompound.parse_obj({
            "pki_ezmaxinvoicing_id": obj.get("pkiEzmaxinvoicingID"),
            "fki_ezmaxinvoicingcontract_id": obj.get("fkiEzmaxinvoicingcontractID"),
            "fki_ezmaxpricing_id": obj.get("fkiEzmaxpricingID"),
            "fki_systemconfigurationtype_id": obj.get("fkiSystemconfigurationtypeID"),
            "s_systemconfigurationtype_description_x": obj.get("sSystemconfigurationtypeDescriptionX"),
            "yyyymm_ezmaxinvoicing": obj.get("yyyymmEzmaxinvoicing"),
            "i_ezmaxinvoicing_days": obj.get("iEzmaxinvoicingDays"),
            "e_ezmaxinvoicing_paymenttype": obj.get("eEzmaxinvoicingPaymenttype"),
            "d_ezmaxinvoicing_rebatepaymenttype": obj.get("dEzmaxinvoicingRebatepaymenttype"),
            "i_ezmaxinvoicing_contractlength": obj.get("iEzmaxinvoicingContractlength"),
            "d_ezmaxinvoicing_rebatecontractlength": obj.get("dEzmaxinvoicingRebatecontractlength"),
            "b_ezmaxinvoicing_rebate_ezsignallagents": obj.get("bEzmaxinvoicingRebateEzsignallagents"),
            "obj_audit": CommonAudit.from_dict(obj.get("objAudit")) if obj.get("objAudit") is not None else None,
            "obj_ezmaxinvoicingcontract": EzmaxinvoicingcontractResponseCompound.from_dict(obj.get("objEzmaxinvoicingcontract")) if obj.get("objEzmaxinvoicingcontract") is not None else None,
            "obj_ezmaxpricing": CustomEzmaxpricingResponse.from_dict(obj.get("objEzmaxpricing")) if obj.get("objEzmaxpricing") is not None else None,
            "a_obj_ezmaxinvoicingsummaryglobal": [EzmaxinvoicingsummaryglobalResponseCompound.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingsummaryglobal")] if obj.get("a_objEzmaxinvoicingsummaryglobal") is not None else None,
            "a_obj_ezmaxinvoicingsummaryexternal": [EzmaxinvoicingsummaryexternalResponseCompound.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingsummaryexternal")] if obj.get("a_objEzmaxinvoicingsummaryexternal") is not None else None,
            "a_obj_ezmaxinvoicingsummaryinternal": [EzmaxinvoicingsummaryinternalResponseCompound.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingsummaryinternal")] if obj.get("a_objEzmaxinvoicingsummaryinternal") is not None else None,
            "a_obj_ezmaxinvoicingagent": [EzmaxinvoicingagentResponseCompound.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingagent")] if obj.get("a_objEzmaxinvoicingagent") is not None else None,
            "a_obj_ezmaxinvoicinguser": [EzmaxinvoicinguserResponseCompound.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicinguser")] if obj.get("a_objEzmaxinvoicinguser") is not None else None,
            "a_obj_ezmaxinvoicingezsignfolder": [CustomEzmaxinvoicingEzsignfolderResponse.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingezsignfolder")] if obj.get("a_objEzmaxinvoicingezsignfolder") is not None else None,
            "a_obj_ezmaxinvoicingezsigndocument": [CustomEzmaxinvoicingEzsigndocumentResponse.from_dict(_item) for _item in obj.get("a_objEzmaxinvoicingezsigndocument")] if obj.get("a_objEzmaxinvoicingezsigndocument") is not None else None
        })
        return _obj


