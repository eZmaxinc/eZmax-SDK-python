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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzmaxinvoicingsummaryexternaldetailResponse(BaseModel):
    """
    A Ezmaxinvoicingsummaryexternaldetail Object
    """ # noqa: E501
    pki_ezmaxinvoicingsummaryexternaldetail_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezmaxinvoicingsummaryexternaldetail", alias="pkiEzmaxinvoicingsummaryexternaldetailID")
    fki_ezmaxinvoicingsummaryexternal_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezmaxinvoicingsummaryexternal", alias="fkiEzmaxinvoicingsummaryexternalID")
    fki_ezmaxproduct_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="The unique ID of the Ezmaxproduct", alias="fkiEzmaxproductID")
    s_ezmaxproduct_description_x: StrictStr = Field(description="The description of the Ezmaxproduct in the language of the requester", alias="sEzmaxproductDescriptionX")
    d_ezmaxinvoicingsummaryexternaldetail_countreal: Annotated[str, Field(strict=True)] = Field(description="The count item invoiced for the product", alias="dEzmaxinvoicingsummaryexternaldetailCountreal")
    d_ezmaxinvoicingsummaryexternaldetail_subtotal: Annotated[str, Field(strict=True)] = Field(description="The subtotal invoiced for the product", alias="dEzmaxinvoicingsummaryexternaldetailSubtotal")
    d_ezmaxinvoicingsummaryexternaldetail_rebate: Annotated[str, Field(strict=True)] = Field(description="The rebate for the product", alias="dEzmaxinvoicingsummaryexternaldetailRebate")
    d_ezmaxinvoicingsummaryexternaldetail_total: Annotated[str, Field(strict=True)] = Field(description="The total invoiced for the product", alias="dEzmaxinvoicingsummaryexternaldetailTotal")
    b_ezmaxinvoicingsummaryexternaldetail_adjustment: StrictBool = Field(description="Whether it's an adjustment", alias="bEzmaxinvoicingsummaryexternaldetailAdjustment")
    t_ezmaxproduct_help_x: StrictStr = Field(description="The help message of the Ezmaxproduct in the language of the requester", alias="tEzmaxproductHelpX")
    __properties: ClassVar[List[str]] = ["pkiEzmaxinvoicingsummaryexternaldetailID", "fkiEzmaxinvoicingsummaryexternalID", "fkiEzmaxproductID", "sEzmaxproductDescriptionX", "dEzmaxinvoicingsummaryexternaldetailCountreal", "dEzmaxinvoicingsummaryexternaldetailSubtotal", "dEzmaxinvoicingsummaryexternaldetailRebate", "dEzmaxinvoicingsummaryexternaldetailTotal", "bEzmaxinvoicingsummaryexternaldetailAdjustment", "tEzmaxproductHelpX"]

    @field_validator('d_ezmaxinvoicingsummaryexternaldetail_countreal')
    def d_ezmaxinvoicingsummaryexternaldetail_countreal_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,6}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,6}?\.[\d]{2}$/")
        return value

    @field_validator('d_ezmaxinvoicingsummaryexternaldetail_subtotal')
    def d_ezmaxinvoicingsummaryexternaldetail_subtotal_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
        return value

    @field_validator('d_ezmaxinvoicingsummaryexternaldetail_rebate')
    def d_ezmaxinvoicingsummaryexternaldetail_rebate_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
        return value

    @field_validator('d_ezmaxinvoicingsummaryexternaldetail_total')
    def d_ezmaxinvoicingsummaryexternaldetail_total_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
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
        """Create an instance of EzmaxinvoicingsummaryexternaldetailResponse from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of EzmaxinvoicingsummaryexternaldetailResponse from a dict"""


