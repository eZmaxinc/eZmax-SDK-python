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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.creditcarddetail_request import CreditcarddetailRequest
from typing import Optional, Set
from typing_extensions import Self

class CreditcardclientRequest(BaseModel):
    """
    A Creditcardclient Object
    """ # noqa: E501
    pki_creditcardclient_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Creditcardclient", alias="pkiCreditcardclientID")
    fks_creditcardtoken_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The creditcard token identifier", alias="fksCreditcardtokenID")
    b_creditcardclientrelation_isdefault: StrictBool = Field(description="Whether if it's the creditcardclient is the default one", alias="bCreditcardclientrelationIsdefault")
    s_creditcardclient_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Creditcardclient", alias="sCreditcardclientDescription")
    b_creditcardclient_allowedcompanypayment: StrictBool = Field(description="Whether if it's an allowedagencypayment", alias="bCreditcardclientAllowedcompanypayment")
    b_creditcardclient_allowedezsign: StrictBool = Field(description="Whether if it's an allowedroyallepageprotection", alias="bCreditcardclientAllowedezsign")
    b_creditcardclient_allowedtranquillit: StrictBool = Field(description="Whether if it's an allowedtranquillit", alias="bCreditcardclientAllowedtranquillit")
    obj_creditcarddetail: CreditcarddetailRequest = Field(alias="objCreditcarddetail")
    s_creditcardclient_cvv: Annotated[str, Field(strict=True)] = Field(description="The creditcard card CVV", alias="sCreditcardclientCVV")
    __properties: ClassVar[List[str]] = ["pkiCreditcardclientID", "fksCreditcardtokenID", "bCreditcardclientrelationIsdefault", "sCreditcardclientDescription", "bCreditcardclientAllowedcompanypayment", "bCreditcardclientAllowedezsign", "bCreditcardclientAllowedtranquillit", "objCreditcarddetail", "sCreditcardclientCVV"]

    @field_validator('fks_creditcardtoken_id')
    def fks_creditcardtoken_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\{?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}?$", value):
            raise ValueError(r"must validate the regular expression /^\{?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}?$/")
        return value

    @field_validator('s_creditcardclient_description')
    def s_creditcardclient_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_creditcardclient_cvv')
    def s_creditcardclient_cvv_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{3,4}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{3,4}$/")
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
        """Create an instance of CreditcardclientRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_creditcarddetail
        if self.obj_creditcarddetail:
            _dict['objCreditcarddetail'] = self.obj_creditcarddetail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of CreditcardclientRequest from a dict"""


