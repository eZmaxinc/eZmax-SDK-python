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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatedocumentResponse(BaseModel):
    """
    A Ezsigntemplatedocument Object
    """ # noqa: E501
    pki_ezsigntemplatedocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocument", alias="pkiEzsigntemplatedocumentID")
    fki_ezsigntemplate_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplate", alias="fkiEzsigntemplateID")
    s_ezsigntemplatedocument_name: StrictStr = Field(description="The name of the Ezsigntemplatedocument.", alias="sEzsigntemplatedocumentName")
    i_ezsigntemplatedocument_pagetotal: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of pages in the Ezsigntemplatedocument.", alias="iEzsigntemplatedocumentPagetotal")
    i_ezsigntemplatedocument_signaturetotal: StrictInt = Field(description="The number of total signatures in the Ezsigntemplate.", alias="iEzsigntemplatedocumentSignaturetotal")
    i_ezsigntemplatedocument_formfieldtotal: StrictInt = Field(description="The number of total form fields in the Ezsigntemplate.", alias="iEzsigntemplatedocumentFormfieldtotal")
    b_ezsigntemplatedocument_hassignedsignatures: StrictBool = Field(description="If the Ezsigntemplatedocument contains signed signatures (From internal or external sources)", alias="bEzsigntemplatedocumentHassignedsignatures")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatedocumentID", "fkiEzsigntemplateID", "sEzsigntemplatedocumentName", "iEzsigntemplatedocumentPagetotal", "iEzsigntemplatedocumentSignaturetotal", "iEzsigntemplatedocumentFormfieldtotal", "bEzsigntemplatedocumentHassignedsignatures"]

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
        """Create an instance of EzsigntemplatedocumentResponse from a JSON string"""
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
        """Create an instance of EzsigntemplatedocumentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatedocumentID": obj.get("pkiEzsigntemplatedocumentID"),
            "fkiEzsigntemplateID": obj.get("fkiEzsigntemplateID"),
            "sEzsigntemplatedocumentName": obj.get("sEzsigntemplatedocumentName"),
            "iEzsigntemplatedocumentPagetotal": obj.get("iEzsigntemplatedocumentPagetotal"),
            "iEzsigntemplatedocumentSignaturetotal": obj.get("iEzsigntemplatedocumentSignaturetotal"),
            "iEzsigntemplatedocumentFormfieldtotal": obj.get("iEzsigntemplatedocumentFormfieldtotal"),
            "bEzsigntemplatedocumentHassignedsignatures": obj.get("bEzsigntemplatedocumentHassignedsignatures")
        })
        return _obj


