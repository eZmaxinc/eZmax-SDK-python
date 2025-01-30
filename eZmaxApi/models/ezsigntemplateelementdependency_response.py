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
from eZmaxApi.models.field_e_ezsigntemplateelementdependency_operator import FieldEEzsigntemplateelementdependencyOperator
from eZmaxApi.models.field_e_ezsigntemplateelementdependency_validation import FieldEEzsigntemplateelementdependencyValidation
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateelementdependencyResponse(BaseModel):
    """
    An Ezsigntemplateelementdependency Object
    """ # noqa: E501
    pki_ezsigntemplateelementdependency_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplateelementdependency", alias="pkiEzsigntemplateelementdependencyID")
    fki_ezsigntemplateformfield_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplateformfield", alias="fkiEzsigntemplateformfieldID")
    fki_ezsigntemplatesignature_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatesignature", alias="fkiEzsigntemplatesignatureID")
    fki_ezsigntemplateformfield_id_validation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplateformfield", alias="fkiEzsigntemplateformfieldIDValidation")
    fki_ezsigntemplateformfieldgroup_id_validation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplateformfieldgroup", alias="fkiEzsigntemplateformfieldgroupIDValidation")
    e_ezsigntemplateelementdependency_validation: FieldEEzsigntemplateelementdependencyValidation = Field(alias="eEzsigntemplateelementdependencyValidation")
    b_ezsigntemplateelementdependency_selected: Optional[StrictBool] = Field(default=None, description="Whether if it's selected or not when using eEzsigntemplateelementdependencyValidation = Selected", alias="bEzsigntemplateelementdependencySelected")
    e_ezsigntemplateelementdependency_operator: Optional[FieldEEzsigntemplateelementdependencyOperator] = Field(default=None, alias="eEzsigntemplateelementdependencyOperator")
    s_ezsigntemplateelementdependency_value: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The value of the Ezsignelementdependency", alias="sEzsigntemplateelementdependencyValue")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateelementdependencyID", "fkiEzsigntemplateformfieldID", "fkiEzsigntemplatesignatureID", "fkiEzsigntemplateformfieldIDValidation", "fkiEzsigntemplateformfieldgroupIDValidation", "eEzsigntemplateelementdependencyValidation", "bEzsigntemplateelementdependencySelected", "eEzsigntemplateelementdependencyOperator", "sEzsigntemplateelementdependencyValue"]

    @field_validator('s_ezsigntemplateelementdependency_value')
    def s_ezsigntemplateelementdependency_value_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
        """Create an instance of EzsigntemplateelementdependencyResponse from a JSON string"""
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
        """Create an instance of EzsigntemplateelementdependencyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateelementdependencyID": obj.get("pkiEzsigntemplateelementdependencyID"),
            "fkiEzsigntemplateformfieldID": obj.get("fkiEzsigntemplateformfieldID"),
            "fkiEzsigntemplatesignatureID": obj.get("fkiEzsigntemplatesignatureID"),
            "fkiEzsigntemplateformfieldIDValidation": obj.get("fkiEzsigntemplateformfieldIDValidation"),
            "fkiEzsigntemplateformfieldgroupIDValidation": obj.get("fkiEzsigntemplateformfieldgroupIDValidation"),
            "eEzsigntemplateelementdependencyValidation": obj.get("eEzsigntemplateelementdependencyValidation"),
            "bEzsigntemplateelementdependencySelected": obj.get("bEzsigntemplateelementdependencySelected"),
            "eEzsigntemplateelementdependencyOperator": obj.get("eEzsigntemplateelementdependencyOperator"),
            "sEzsigntemplateelementdependencyValue": obj.get("sEzsigntemplateelementdependencyValue")
        })
        return _obj


