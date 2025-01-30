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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.multilingual_supply_description import MultilingualSupplyDescription
from typing import Optional, Set
from typing_extensions import Self

class SupplyRequest(BaseModel):
    """
    A Supply Object
    """ # noqa: E501
    pki_supply_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Supply", alias="pkiSupplyID")
    fki_glaccount_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Glaccount", alias="fkiGlaccountID")
    fki_glaccountcontainer_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Glaccountcontainer", alias="fkiGlaccountcontainerID")
    fki_variableexpense_id: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The unique ID of the Variableexpense", alias="fkiVariableexpenseID")
    s_supply_code: Annotated[str, Field(strict=True)] = Field(description="The code of the Supply", alias="sSupplyCode")
    obj_supply_description: MultilingualSupplyDescription = Field(alias="objSupplyDescription")
    d_supply_unitprice: Annotated[str, Field(min_length=4, strict=True, max_length=13)] = Field(description="The unit price of the Supply", alias="dSupplyUnitprice")
    b_supply_isactive: StrictBool = Field(description="Whether the supply is active or not", alias="bSupplyIsactive")
    b_supply_variableprice: StrictBool = Field(description="Whether if the price is variable", alias="bSupplyVariableprice")
    __properties: ClassVar[List[str]] = ["pkiSupplyID", "fkiGlaccountID", "fkiGlaccountcontainerID", "fkiVariableexpenseID", "sSupplyCode", "objSupplyDescription", "dSupplyUnitprice", "bSupplyIsactive", "bSupplyVariableprice"]

    @field_validator('s_supply_code')
    def s_supply_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,5}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,5}$/")
        return value

    @field_validator('d_supply_unitprice')
    def d_supply_unitprice_validate_regular_expression(cls, value):
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
        """Create an instance of SupplyRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_supply_description
        if self.obj_supply_description:
            _dict['objSupplyDescription'] = self.obj_supply_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupplyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSupplyID": obj.get("pkiSupplyID"),
            "fkiGlaccountID": obj.get("fkiGlaccountID"),
            "fkiGlaccountcontainerID": obj.get("fkiGlaccountcontainerID"),
            "fkiVariableexpenseID": obj.get("fkiVariableexpenseID"),
            "sSupplyCode": obj.get("sSupplyCode"),
            "objSupplyDescription": MultilingualSupplyDescription.from_dict(obj["objSupplyDescription"]) if obj.get("objSupplyDescription") is not None else None,
            "dSupplyUnitprice": obj.get("dSupplyUnitprice"),
            "bSupplyIsactive": obj.get("bSupplyIsactive"),
            "bSupplyVariableprice": obj.get("bSupplyVariableprice")
        })
        return _obj


