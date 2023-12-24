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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.field_e_ezmaxinvoicing_paymenttype import FieldEEzmaxinvoicingPaymenttype
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzmaxinvoicingResponse(BaseModel):
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
    __properties: ClassVar[List[str]] = ["pkiEzmaxinvoicingID", "fkiEzmaxinvoicingcontractID", "fkiEzmaxpricingID", "fkiSystemconfigurationtypeID", "sSystemconfigurationtypeDescriptionX", "yyyymmEzmaxinvoicing", "iEzmaxinvoicingDays", "eEzmaxinvoicingPaymenttype", "dEzmaxinvoicingRebatepaymenttype", "iEzmaxinvoicingContractlength", "dEzmaxinvoicingRebatecontractlength", "bEzmaxinvoicingRebateEzsignallagents", "objAudit"]

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

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EzmaxinvoicingResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EzmaxinvoicingResponse from a dict"""
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
            "objAudit": CommonAudit.from_dict(obj.get("objAudit")) if obj.get("objAudit") is not None else None
        })
        return _obj


