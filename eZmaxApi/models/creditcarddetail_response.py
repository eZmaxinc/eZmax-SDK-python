# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
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
from typing import Optional, Set
from typing_extensions import Self

class CreditcarddetailResponse(BaseModel):
    """
    A Creditcarddetail Object
    """ # noqa: E501
    pki_creditcarddetail_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Creditcarddetail", alias="pkiCreditcarddetailID")
    fki_creditcardtype_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Creditcardtype", alias="fkiCreditcardtypeID")
    i_creditcarddetail_lastdigits: Annotated[int, Field(le=9999, strict=True, ge=0)] = Field(description="The last digits of the Creditcarddetail", alias="iCreditcarddetailLastdigits")
    i_creditcarddetail_expirationmonth: Annotated[int, Field(le=12, strict=True, ge=0)] = Field(description="The expirationmonth of the Creditcarddetail", alias="iCreditcarddetailExpirationmonth")
    i_creditcarddetail_expirationyear: Annotated[int, Field(le=2200, strict=True, ge=0)] = Field(description="The expirationyear of the Creditcarddetail", alias="iCreditcarddetailExpirationyear")
    s_creditcarddetail_civic: Annotated[str, Field(strict=True)] = Field(description="The civic of the Creditcarddetail", alias="sCreditcarddetailCivic")
    s_creditcarddetail_street: Annotated[str, Field(strict=True)] = Field(description="The street of the Creditcarddetail", alias="sCreditcarddetailStreet")
    s_creditcarddetail_zip: Annotated[str, Field(strict=True)] = Field(description="The zip of the Creditcarddetail", alias="sCreditcarddetailZip")
    __properties: ClassVar[List[str]] = ["pkiCreditcarddetailID", "fkiCreditcardtypeID", "iCreditcarddetailLastdigits", "iCreditcarddetailExpirationmonth", "iCreditcarddetailExpirationyear", "sCreditcarddetailCivic", "sCreditcarddetailStreet", "sCreditcarddetailZip"]

    @field_validator('s_creditcarddetail_civic')
    def s_creditcarddetail_civic_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\d]{1,8}$", value):
            raise ValueError(r"must validate the regular expression /^[\d]{1,8}$/")
        return value

    @field_validator('s_creditcarddetail_street')
    def s_creditcarddetail_street_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,19}$/")
        return value

    @field_validator('s_creditcarddetail_zip')
    def s_creditcarddetail_zip_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,9}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,9}$/")
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
        """Create an instance of CreditcarddetailResponse from a JSON string"""
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
        """Create an instance of CreditcarddetailResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiCreditcarddetailID": obj.get("pkiCreditcarddetailID"),
            "fkiCreditcardtypeID": obj.get("fkiCreditcardtypeID"),
            "iCreditcarddetailLastdigits": obj.get("iCreditcarddetailLastdigits"),
            "iCreditcarddetailExpirationmonth": obj.get("iCreditcarddetailExpirationmonth"),
            "iCreditcarddetailExpirationyear": obj.get("iCreditcarddetailExpirationyear"),
            "sCreditcarddetailCivic": obj.get("sCreditcarddetailCivic"),
            "sCreditcarddetailStreet": obj.get("sCreditcarddetailStreet"),
            "sCreditcarddetailZip": obj.get("sCreditcarddetailZip")
        })
        return _obj


