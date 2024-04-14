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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.address_request import AddressRequest
from eZmaxApi.models.contact_request_compound import ContactRequestCompound
from typing import Optional, Set
from typing_extensions import Self

class FranchisereferalincomeRequestCompound(BaseModel):
    """
    A Franchisereferalincome Object and children to create a complete structure
    """ # noqa: E501
    pki_franchisereferalincome_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Franchisereferalincome", alias="pkiFranchisereferalincomeID")
    fki_franchisebroker_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Franchisebroker", alias="fkiFranchisebrokerID")
    fki_franchisereferalincomeprogram_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Franchisereferalincomeprogram", alias="fkiFranchisereferalincomeprogramID")
    fki_period_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Period", alias="fkiPeriodID")
    d_franchisereferalincome_loan: StrictStr = Field(description="The loan amount", alias="dFranchisereferalincomeLoan")
    d_franchisereferalincome_franchiseamount: StrictStr = Field(description="The amount that will be given to the franchise", alias="dFranchisereferalincomeFranchiseamount")
    d_franchisereferalincome_franchisoramount: StrictStr = Field(description="The amount that will be kept by the franchisor", alias="dFranchisereferalincomeFranchisoramount")
    d_franchisereferalincome_agentamount: StrictStr = Field(description="The amount that will be given to the agent", alias="dFranchisereferalincomeAgentamount")
    dt_franchisereferalincome_disbursed: StrictStr = Field(description="The date the amounts were disbursed", alias="dtFranchisereferalincomeDisbursed")
    t_franchisereferalincome_comment: StrictStr = Field(description="Comment about the transaction", alias="tFranchisereferalincomeComment")
    fki_franchiseoffice_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Franchisereoffice", alias="fkiFranchiseofficeID")
    s_franchisereferalincome_remoteid: StrictStr = Field(alias="sFranchisereferalincomeRemoteid")
    obj_address: Optional[AddressRequest] = Field(default=None, alias="objAddress")
    a_obj_contact: List[ContactRequestCompound] = Field(alias="a_objContact")
    __properties: ClassVar[List[str]] = ["pkiFranchisereferalincomeID", "fkiFranchisebrokerID", "fkiFranchisereferalincomeprogramID", "fkiPeriodID", "dFranchisereferalincomeLoan", "dFranchisereferalincomeFranchiseamount", "dFranchisereferalincomeFranchisoramount", "dFranchisereferalincomeAgentamount", "dtFranchisereferalincomeDisbursed", "tFranchisereferalincomeComment", "fkiFranchiseofficeID", "sFranchisereferalincomeRemoteid", "objAddress", "a_objContact"]

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
        """Create an instance of FranchisereferalincomeRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_address
        if self.obj_address:
            _dict['objAddress'] = self.obj_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_contact (list)
        _items = []
        if self.a_obj_contact:
            for _item in self.a_obj_contact:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objContact'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FranchisereferalincomeRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiFranchisereferalincomeID": obj.get("pkiFranchisereferalincomeID"),
            "fkiFranchisebrokerID": obj.get("fkiFranchisebrokerID"),
            "fkiFranchisereferalincomeprogramID": obj.get("fkiFranchisereferalincomeprogramID"),
            "fkiPeriodID": obj.get("fkiPeriodID"),
            "dFranchisereferalincomeLoan": obj.get("dFranchisereferalincomeLoan"),
            "dFranchisereferalincomeFranchiseamount": obj.get("dFranchisereferalincomeFranchiseamount"),
            "dFranchisereferalincomeFranchisoramount": obj.get("dFranchisereferalincomeFranchisoramount"),
            "dFranchisereferalincomeAgentamount": obj.get("dFranchisereferalincomeAgentamount"),
            "dtFranchisereferalincomeDisbursed": obj.get("dtFranchisereferalincomeDisbursed"),
            "tFranchisereferalincomeComment": obj.get("tFranchisereferalincomeComment"),
            "fkiFranchiseofficeID": obj.get("fkiFranchiseofficeID"),
            "sFranchisereferalincomeRemoteid": obj.get("sFranchisereferalincomeRemoteid"),
            "objAddress": AddressRequest.from_dict(obj["objAddress"]) if obj.get("objAddress") is not None else None,
            "a_objContact": [ContactRequestCompound.from_dict(_item) for _item in obj["a_objContact"]] if obj.get("a_objContact") is not None else None
        })
        return _obj


