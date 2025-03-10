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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateglobaldocumentResponse(BaseModel):
    """
    A Ezsigntemplateglobaldocument Object
    """ # noqa: E501
    pki_ezsigntemplateglobaldocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplateglobaldocument", alias="pkiEzsigntemplateglobaldocumentID")
    s_ezsigntemplateglobaldocument_name: StrictStr = Field(description="The name of the Ezsigntemplateglobaldocument.", alias="sEzsigntemplateglobaldocumentName")
    i_ezsigntemplateglobaldocument_pagetotal: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of pages in the Ezsigntemplateglobaldocument.", alias="iEzsigntemplateglobaldocumentPagetotal")
    i_ezsigntemplateglobaldocument_signaturetotal: StrictInt = Field(description="The number of total signatures in the Ezsigntemplateglobal.", alias="iEzsigntemplateglobaldocumentSignaturetotal")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateglobaldocumentID", "sEzsigntemplateglobaldocumentName", "iEzsigntemplateglobaldocumentPagetotal", "iEzsigntemplateglobaldocumentSignaturetotal"]

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
        """Create an instance of EzsigntemplateglobaldocumentResponse from a JSON string"""
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
        """Create an instance of EzsigntemplateglobaldocumentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateglobaldocumentID": obj.get("pkiEzsigntemplateglobaldocumentID"),
            "sEzsigntemplateglobaldocumentName": obj.get("sEzsigntemplateglobaldocumentName"),
            "iEzsigntemplateglobaldocumentPagetotal": obj.get("iEzsigntemplateglobaldocumentPagetotal"),
            "iEzsigntemplateglobaldocumentSignaturetotal": obj.get("iEzsigntemplateglobaldocumentSignaturetotal")
        })
        return _obj


