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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
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
from typing import Optional, Set
from typing_extensions import Self

class EzmaxinvoicingResponseCompound(BaseModel):
    """
    A Ezmaxinvoicing Object
    """ # noqa: E501
    pki_ezmaxinvoicing_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezmaxinvoicing", alias="pkiEzmaxinvoicingID")
    fki_ezmaxinvoicingcontract_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="The unique ID of the Ezmaxinvoicingcontract", alias="fkiEzmaxinvoicingcontractID")
    fki_ezmaxpricing_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="The unique ID of the Ezmaxpricing", alias="fkiEzmaxpricingID")
    fki_systemconfigurationtype_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="The unique ID of the Systemconfigurationtype", alias="fkiSystemconfigurationtypeID")
    s_systemconfigurationtype_description_x: StrictStr = Field(description="The description of the Systemconfigurationtype in the language of the requester", alias="sSystemconfigurationtypeDescriptionX")
    yyyymm_ezmaxinvoicing: Annotated[str, Field(strict=True, max_length=7)] = Field(description="The YYYYMM period of the Ezmaxinvoicing", alias="yyyymmEzmaxinvoicing")
    i_ezmaxinvoicing_days: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of days invoiced", alias="iEzmaxinvoicingDays")
    e_ezmaxinvoicing_paymenttype: FieldEEzmaxinvoicingPaymenttype = Field(alias="eEzmaxinvoicingPaymenttype")
    d_ezmaxinvoicing_rebatepaymenttype: Annotated[str, Field(strict=True)] = Field(description="The percentage of rebate depending of the payment type", alias="dEzmaxinvoicingRebatepaymenttype")
    i_ezmaxinvoicing_contractlength: Annotated[int, Field(strict=True, ge=1)] = Field(description="The length of the contract in years", alias="iEzmaxinvoicingContractlength")
    d_ezmaxinvoicing_rebatecontractlength: Annotated[str, Field(strict=True)] = Field(description="The percentage of rebate depending of the contract length", alias="dEzmaxinvoicingRebatecontractlength")
    b_ezmaxinvoicing_rebate_ezsignallagents: StrictBool = Field(description="Whether the rebate for eZsign is for all agents", alias="bEzmaxinvoicingRebateEzsignallagents")
    obj_audit: Optional[CommonAudit] = Field(default=None, alias="objAudit")
    obj_ezmaxinvoicingcontract: EzmaxinvoicingcontractResponseCompound = Field(alias="objEzmaxinvoicingcontract")
    obj_ezmaxpricing: CustomEzmaxpricingResponse = Field(alias="objEzmaxpricing")
    a_obj_ezmaxinvoicingsummaryglobal: List[EzmaxinvoicingsummaryglobalResponseCompound] = Field(alias="a_objEzmaxinvoicingsummaryglobal")
    a_obj_ezmaxinvoicingsummaryexternal: List[EzmaxinvoicingsummaryexternalResponseCompound] = Field(alias="a_objEzmaxinvoicingsummaryexternal")
    a_obj_ezmaxinvoicingsummaryinternal: List[EzmaxinvoicingsummaryinternalResponseCompound] = Field(alias="a_objEzmaxinvoicingsummaryinternal")
    a_obj_ezmaxinvoicingagent: List[EzmaxinvoicingagentResponseCompound] = Field(alias="a_objEzmaxinvoicingagent")
    a_obj_ezmaxinvoicinguser: List[EzmaxinvoicinguserResponseCompound] = Field(alias="a_objEzmaxinvoicinguser")
    a_obj_ezmaxinvoicingezsignfolder: List[CustomEzmaxinvoicingEzsignfolderResponse] = Field(alias="a_objEzmaxinvoicingezsignfolder")
    a_obj_ezmaxinvoicingezsigndocument: List[CustomEzmaxinvoicingEzsigndocumentResponse] = Field(alias="a_objEzmaxinvoicingezsigndocument")
    __properties: ClassVar[List[str]] = ["pkiEzmaxinvoicingID", "fkiEzmaxinvoicingcontractID", "fkiEzmaxpricingID", "fkiSystemconfigurationtypeID", "sSystemconfigurationtypeDescriptionX", "yyyymmEzmaxinvoicing", "iEzmaxinvoicingDays", "eEzmaxinvoicingPaymenttype", "dEzmaxinvoicingRebatepaymenttype", "iEzmaxinvoicingContractlength", "dEzmaxinvoicingRebatecontractlength", "bEzmaxinvoicingRebateEzsignallagents", "objAudit", "objEzmaxinvoicingcontract", "objEzmaxpricing", "a_objEzmaxinvoicingsummaryglobal", "a_objEzmaxinvoicingsummaryexternal", "a_objEzmaxinvoicingsummaryinternal", "a_objEzmaxinvoicingagent", "a_objEzmaxinvoicinguser", "a_objEzmaxinvoicingezsignfolder", "a_objEzmaxinvoicingezsigndocument"]

    @field_validator('d_ezmaxinvoicing_rebatepaymenttype')
    def d_ezmaxinvoicing_rebatepaymenttype_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,3}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,3}?\.[\d]{2}$/")
        return value

    @field_validator('d_ezmaxinvoicing_rebatecontractlength')
    def d_ezmaxinvoicing_rebatecontractlength_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,3}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,3}?\.[\d]{2}$/")
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
        """Create an instance of EzmaxinvoicingResponseCompound from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzmaxinvoicingResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzmaxinvoicingID": obj.get("pkiEzmaxinvoicingID"),
            "fkiEzmaxinvoicingcontractID": obj.get("fkiEzmaxinvoicingcontractID"),
            "fkiEzmaxpricingID": obj.get("fkiEzmaxpricingID"),
            "fkiSystemconfigurationtypeID": obj.get("fkiSystemconfigurationtypeID"),
            "sSystemconfigurationtypeDescriptionX": obj.get("sSystemconfigurationtypeDescriptionX"),
            "yyyymmEzmaxinvoicing": obj.get("yyyymmEzmaxinvoicing"),
            "iEzmaxinvoicingDays": obj.get("iEzmaxinvoicingDays"),
            "eEzmaxinvoicingPaymenttype": obj.get("eEzmaxinvoicingPaymenttype"),
            "dEzmaxinvoicingRebatepaymenttype": obj.get("dEzmaxinvoicingRebatepaymenttype"),
            "iEzmaxinvoicingContractlength": obj.get("iEzmaxinvoicingContractlength"),
            "dEzmaxinvoicingRebatecontractlength": obj.get("dEzmaxinvoicingRebatecontractlength"),
            "bEzmaxinvoicingRebateEzsignallagents": obj.get("bEzmaxinvoicingRebateEzsignallagents"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "objEzmaxinvoicingcontract": EzmaxinvoicingcontractResponseCompound.from_dict(obj["objEzmaxinvoicingcontract"]) if obj.get("objEzmaxinvoicingcontract") is not None else None,
            "objEzmaxpricing": CustomEzmaxpricingResponse.from_dict(obj["objEzmaxpricing"]) if obj.get("objEzmaxpricing") is not None else None,
            "a_objEzmaxinvoicingsummaryglobal": [EzmaxinvoicingsummaryglobalResponseCompound.from_dict(_item) for _item in obj["a_objEzmaxinvoicingsummaryglobal"]] if obj.get("a_objEzmaxinvoicingsummaryglobal") is not None else None,
            "a_objEzmaxinvoicingsummaryexternal": [EzmaxinvoicingsummaryexternalResponseCompound.from_dict(_item) for _item in obj["a_objEzmaxinvoicingsummaryexternal"]] if obj.get("a_objEzmaxinvoicingsummaryexternal") is not None else None,
            "a_objEzmaxinvoicingsummaryinternal": [EzmaxinvoicingsummaryinternalResponseCompound.from_dict(_item) for _item in obj["a_objEzmaxinvoicingsummaryinternal"]] if obj.get("a_objEzmaxinvoicingsummaryinternal") is not None else None,
            "a_objEzmaxinvoicingagent": [EzmaxinvoicingagentResponseCompound.from_dict(_item) for _item in obj["a_objEzmaxinvoicingagent"]] if obj.get("a_objEzmaxinvoicingagent") is not None else None,
            "a_objEzmaxinvoicinguser": [EzmaxinvoicinguserResponseCompound.from_dict(_item) for _item in obj["a_objEzmaxinvoicinguser"]] if obj.get("a_objEzmaxinvoicinguser") is not None else None,
            "a_objEzmaxinvoicingezsignfolder": [CustomEzmaxinvoicingEzsignfolderResponse.from_dict(_item) for _item in obj["a_objEzmaxinvoicingezsignfolder"]] if obj.get("a_objEzmaxinvoicingezsignfolder") is not None else None,
            "a_objEzmaxinvoicingezsigndocument": [CustomEzmaxinvoicingEzsigndocumentResponse.from_dict(_item) for _item in obj["a_objEzmaxinvoicingezsigndocument"]] if obj.get("a_objEzmaxinvoicingezsigndocument") is not None else None
        })
        return _obj


