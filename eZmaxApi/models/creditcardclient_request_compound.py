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

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.creditcardclient_request import CreditcardclientRequest
from eZmaxApi.models.creditcarddetail_request import CreditcarddetailRequest
from typing import Optional, Set
from typing_extensions import Self

class CreditcardclientRequestCompound(CreditcardclientRequest):
    """
    A Creditcardclient Object and children
    """ # noqa: E501
    __properties: ClassVar[List[str]] = ["pkiCreditcardclientID", "fksCreditcardtokenID", "bCreditcardclientrelationIsdefault", "sCreditcardclientDescription", "bCreditcardclientAllowedcompanypayment", "bCreditcardclientAllowedezsign", "bCreditcardclientAllowedtranquillit", "objCreditcarddetail", "sCreditcardclientCVV"]

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
        """Create an instance of CreditcardclientRequestCompound from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreditcardclientRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiCreditcardclientID": obj.get("pkiCreditcardclientID"),
            "fksCreditcardtokenID": obj.get("fksCreditcardtokenID"),
            "bCreditcardclientrelationIsdefault": obj.get("bCreditcardclientrelationIsdefault"),
            "sCreditcardclientDescription": obj.get("sCreditcardclientDescription"),
            "bCreditcardclientAllowedcompanypayment": obj.get("bCreditcardclientAllowedcompanypayment"),
            "bCreditcardclientAllowedezsign": obj.get("bCreditcardclientAllowedezsign"),
            "bCreditcardclientAllowedtranquillit": obj.get("bCreditcardclientAllowedtranquillit"),
            "objCreditcarddetail": CreditcarddetailRequest.from_dict(obj["objCreditcarddetail"]) if obj.get("objCreditcarddetail") is not None else None,
            "sCreditcardclientCVV": obj.get("sCreditcardclientCVV")
        })
        return _obj


