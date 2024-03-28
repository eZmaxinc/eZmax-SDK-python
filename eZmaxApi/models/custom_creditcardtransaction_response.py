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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from eZmaxApi.models.field_e_creditcardtype_codename import FieldECreditcardtypeCodename
from typing import Optional, Set
from typing_extensions import Self

class CustomCreditcardtransactionResponse(BaseModel):
    """
    A custom Creditcardtransaction Object
    """ # noqa: E501
    e_creditcardtype_codename: FieldECreditcardtypeCodename = Field(alias="eCreditcardtypeCodename")
    d_creditcardtransaction_amount: Annotated[str, Field(strict=True)] = Field(description="The amount of the Creditcardtransaction", alias="dCreditcardtransactionAmount")
    s_creditcardtransaction_partiallydecryptednumber: Annotated[str, Field(strict=True)] = Field(description="The partially decrypted credit card number used in the Creditcardtransaction", alias="sCreditcardtransactionPartiallydecryptednumber")
    s_creditcardtransaction_referencenumber: Annotated[str, Field(strict=True)] = Field(description="The reference number on the creditcard service for the Creditcardtransaction", alias="sCreditcardtransactionReferencenumber")
    __properties: ClassVar[List[str]] = ["eCreditcardtypeCodename", "dCreditcardtransactionAmount", "sCreditcardtransactionPartiallydecryptednumber", "sCreditcardtransactionReferencenumber"]

    @field_validator('d_creditcardtransaction_amount')
    def d_creditcardtransaction_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
        return value

    @field_validator('s_creditcardtransaction_partiallydecryptednumber')
    def s_creditcardtransaction_partiallydecryptednumber_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^([X]{4}[ ]){3}(\d){4}$", value):
            raise ValueError(r"must validate the regular expression /^([X]{4}[ ]){3}(\d){4}$/")
        return value

    @field_validator('s_creditcardtransaction_referencenumber')
    def s_creditcardtransaction_referencenumber_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\d]{18}$", value):
            raise ValueError(r"must validate the regular expression /^[\d]{18}$/")
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
        """Create an instance of CustomCreditcardtransactionResponse from a JSON string"""
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
        """Create an instance of CustomCreditcardtransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eCreditcardtypeCodename": obj.get("eCreditcardtypeCodename"),
            "dCreditcardtransactionAmount": obj.get("dCreditcardtransactionAmount"),
            "sCreditcardtransactionPartiallydecryptednumber": obj.get("sCreditcardtransactionPartiallydecryptednumber"),
            "sCreditcardtransactionReferencenumber": obj.get("sCreditcardtransactionReferencenumber")
        })
        return _obj


