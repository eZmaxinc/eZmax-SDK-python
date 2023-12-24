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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomEzmaxpricingResponse(BaseModel):
    """
    A Custom Ezmaxpricing Object
    """ # noqa: E501
    pki_ezmaxpricing_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="The unique ID of the Ezmaxpricing", alias="pkiEzmaxpricingID")
    d_ezmaxpricing_rebateezsignallagents: Annotated[str, Field(strict=True)] = Field(description="The rebate offered when eZsign is taken for all agents", alias="dEzmaxpricingRebateezsignallagents")
    dt_ezmaxpricing_start: StrictStr = Field(description="The start date of the Ezmaxpricing", alias="dtEzmaxpricingStart")
    dt_ezmaxpricing_end: Optional[StrictStr] = Field(default=None, description="The end date of the Ezmaxpricing", alias="dtEzmaxpricingEnd")
    __properties: ClassVar[List[str]] = ["pkiEzmaxpricingID", "dEzmaxpricingRebateezsignallagents", "dtEzmaxpricingStart", "dtEzmaxpricingEnd"]

    @field_validator('d_ezmaxpricing_rebateezsignallagents')
    def d_ezmaxpricing_rebateezsignallagents_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-{0,1}[\d]{1,9}?\.[\d]{2}$", value):
            raise ValueError(r"must validate the regular expression /^-{0,1}[\d]{1,9}?\.[\d]{2}$/")
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
        """Create an instance of CustomEzmaxpricingResponse from a JSON string"""
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
        """Create an instance of CustomEzmaxpricingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzmaxpricingID": obj.get("pkiEzmaxpricingID"),
            "dEzmaxpricingRebateezsignallagents": obj.get("dEzmaxpricingRebateezsignallagents"),
            "dtEzmaxpricingStart": obj.get("dtEzmaxpricingStart"),
            "dtEzmaxpricingEnd": obj.get("dtEzmaxpricingEnd")
        })
        return _obj


