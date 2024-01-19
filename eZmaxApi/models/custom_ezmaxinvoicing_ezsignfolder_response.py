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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomEzmaxinvoicingEzsignfolderResponse(BaseModel):
    """
    An EzmaxinvoicingEzsignfolder object containing information about the Ezmaxinvoicing for an Ezsignfolder
    """ # noqa: E501
    fki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="fkiEzsignfolderID")
    fki_billingentityinternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Billingentityinternal.", alias="fkiBillingentityinternalID")
    s_ezsignfolder_description: StrictStr = Field(description="The description of the Ezsignfolder", alias="sEzsignfolderDescription")
    b_ezsigntsarequirement_billable: StrictBool = Field(description="Whether the TSA requirement is billable or not", alias="bEzsigntsarequirementBillable")
    b_ezsignfolder_mfaused: StrictBool = Field(description="Whether the MFA was used or not for the Ezsignfolder", alias="bEzsignfolderMfaused")
    b_ezsignfolder_paymentused: StrictBool = Field(description="Whether there was a signature is of type payment", alias="bEzsignfolderPaymentused")
    b_ezsignfolder_allowed: StrictBool = Field(description="Whether you have access to the Ezsignfolder or not", alias="bEzsignfolderAllowed")
    __properties: ClassVar[List[str]] = ["fkiEzsignfolderID", "fkiBillingentityinternalID", "sEzsignfolderDescription", "bEzsigntsarequirementBillable", "bEzsignfolderMfaused", "bEzsignfolderPaymentused", "bEzsignfolderAllowed"]

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
        """Create an instance of CustomEzmaxinvoicingEzsignfolderResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomEzmaxinvoicingEzsignfolderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiEzsignfolderID": obj.get("fkiEzsignfolderID"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "bEzsigntsarequirementBillable": obj.get("bEzsigntsarequirementBillable"),
            "bEzsignfolderMfaused": obj.get("bEzsignfolderMfaused"),
            "bEzsignfolderPaymentused": obj.get("bEzsignfolderPaymentused"),
            "bEzsignfolderAllowed": obj.get("bEzsignfolderAllowed")
        })
        return _obj


