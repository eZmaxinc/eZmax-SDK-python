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
from eZmaxApi.models.field_e_variableexpense_taxable import FieldEVariableexpenseTaxable
from eZmaxApi.models.multilingual_variableexpense_description import MultilingualVariableexpenseDescription
from typing import Optional, Set
from typing_extensions import Self

class VariableexpenseRequest(BaseModel):
    """
    A Variableexpense Object
    """ # noqa: E501
    pki_variableexpense_id: Optional[Annotated[int, Field(le=255, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Variableexpense", alias="pkiVariableexpenseID")
    s_variableexpense_code: Annotated[str, Field(strict=True)] = Field(description="The code of the Variableexpense", alias="sVariableexpenseCode")
    obj_variableexpense_description: MultilingualVariableexpenseDescription = Field(alias="objVariableexpenseDescription")
    e_variableexpense_taxable: FieldEVariableexpenseTaxable = Field(alias="eVariableexpenseTaxable")
    b_variableexpense_isactive: StrictBool = Field(description="Whether the variableexpense is active or not", alias="bVariableexpenseIsactive")
    __properties: ClassVar[List[str]] = ["pkiVariableexpenseID", "sVariableexpenseCode", "objVariableexpenseDescription", "eVariableexpenseTaxable", "bVariableexpenseIsactive"]

    @field_validator('s_variableexpense_code')
    def s_variableexpense_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,5}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,5}$/")
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
        """Create an instance of VariableexpenseRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_variableexpense_description
        if self.obj_variableexpense_description:
            _dict['objVariableexpenseDescription'] = self.obj_variableexpense_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VariableexpenseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiVariableexpenseID": obj.get("pkiVariableexpenseID"),
            "sVariableexpenseCode": obj.get("sVariableexpenseCode"),
            "objVariableexpenseDescription": MultilingualVariableexpenseDescription.from_dict(obj["objVariableexpenseDescription"]) if obj.get("objVariableexpenseDescription") is not None else None,
            "eVariableexpenseTaxable": obj.get("eVariableexpenseTaxable"),
            "bVariableexpenseIsactive": obj.get("bVariableexpenseIsactive")
        })
        return _obj


