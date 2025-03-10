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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsigntemplatedocumentpagerecognition_operator import FieldEEzsigntemplatedocumentpagerecognitionOperator
from eZmaxApi.models.field_e_ezsigntemplatedocumentpagerecognition_section import FieldEEzsigntemplatedocumentpagerecognitionSection
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatedocumentpagerecognitionResponse(BaseModel):
    """
    A Ezsigntemplatedocumentpagerecognition Object
    """ # noqa: E501
    pki_ezsigntemplatedocumentpagerecognition_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocumentpagerecognition", alias="pkiEzsigntemplatedocumentpagerecognitionID")
    fki_ezsigntemplatedocumentpage_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocumentpage", alias="fkiEzsigntemplatedocumentpageID")
    e_ezsigntemplatedocumentpagerecognition_operator: FieldEEzsigntemplatedocumentpagerecognitionOperator = Field(alias="eEzsigntemplatedocumentpagerecognitionOperator")
    e_ezsigntemplatedocumentpagerecognition_section: FieldEEzsigntemplatedocumentpagerecognitionSection = Field(alias="eEzsigntemplatedocumentpagerecognitionSection")
    i_ezsigntemplatedocumentpagerecognition_similarpercentage: Optional[Annotated[int, Field(le=100, strict=True, ge=60)]] = Field(default=None, description="The similarpercentage of the Ezsigntemplatedocumentpagerecognition", alias="iEzsigntemplatedocumentpagerecognitionSimilarpercentage")
    i_ezsigntemplatedocumentpagerecognition_x: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The x of the Ezsigntemplatedocumentpagerecognition", alias="iEzsigntemplatedocumentpagerecognitionX")
    i_ezsigntemplatedocumentpagerecognition_y: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The y of the Ezsigntemplatedocumentpagerecognition", alias="iEzsigntemplatedocumentpagerecognitionY")
    i_ezsigntemplatedocumentpagerecognition_width: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The width of the Ezsigntemplatedocumentpagerecognition", alias="iEzsigntemplatedocumentpagerecognitionWidth")
    i_ezsigntemplatedocumentpagerecognition_height: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The height of the Ezsigntemplatedocumentpagerecognition", alias="iEzsigntemplatedocumentpagerecognitionHeight")
    t_ezsigntemplatedocumentpagerecognition_text: Annotated[str, Field(strict=True)] = Field(description="The text of the Ezsigntemplatedocumentpagerecognition", alias="tEzsigntemplatedocumentpagerecognitionText")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatedocumentpagerecognitionID", "fkiEzsigntemplatedocumentpageID", "eEzsigntemplatedocumentpagerecognitionOperator", "eEzsigntemplatedocumentpagerecognitionSection", "iEzsigntemplatedocumentpagerecognitionSimilarpercentage", "iEzsigntemplatedocumentpagerecognitionX", "iEzsigntemplatedocumentpagerecognitionY", "iEzsigntemplatedocumentpagerecognitionWidth", "iEzsigntemplatedocumentpagerecognitionHeight", "tEzsigntemplatedocumentpagerecognitionText"]

    @field_validator('t_ezsigntemplatedocumentpagerecognition_text')
    def t_ezsigntemplatedocumentpagerecognition_text_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[.\D\d]{0,65535}$", value):
            raise ValueError(r"must validate the regular expression /^[.\D\d]{0,65535}$/")
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
        """Create an instance of EzsigntemplatedocumentpagerecognitionResponse from a JSON string"""
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
        """Create an instance of EzsigntemplatedocumentpagerecognitionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatedocumentpagerecognitionID": obj.get("pkiEzsigntemplatedocumentpagerecognitionID"),
            "fkiEzsigntemplatedocumentpageID": obj.get("fkiEzsigntemplatedocumentpageID"),
            "eEzsigntemplatedocumentpagerecognitionOperator": obj.get("eEzsigntemplatedocumentpagerecognitionOperator"),
            "eEzsigntemplatedocumentpagerecognitionSection": obj.get("eEzsigntemplatedocumentpagerecognitionSection"),
            "iEzsigntemplatedocumentpagerecognitionSimilarpercentage": obj.get("iEzsigntemplatedocumentpagerecognitionSimilarpercentage"),
            "iEzsigntemplatedocumentpagerecognitionX": obj.get("iEzsigntemplatedocumentpagerecognitionX"),
            "iEzsigntemplatedocumentpagerecognitionY": obj.get("iEzsigntemplatedocumentpagerecognitionY"),
            "iEzsigntemplatedocumentpagerecognitionWidth": obj.get("iEzsigntemplatedocumentpagerecognitionWidth"),
            "iEzsigntemplatedocumentpagerecognitionHeight": obj.get("iEzsigntemplatedocumentpagerecognitionHeight"),
            "tEzsigntemplatedocumentpagerecognitionText": obj.get("tEzsigntemplatedocumentpagerecognitionText")
        })
        return _obj


