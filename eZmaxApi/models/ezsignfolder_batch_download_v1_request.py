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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsignfolderBatchDownloadV1Request(BaseModel):
    """
    Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/batchDownload
    """ # noqa: E501
    a_pki_ezsigndocument_id: Annotated[List[Annotated[int, Field(strict=True, ge=0)]], Field(min_length=1)] = Field(alias="a_pkiEzsigndocumentID")
    a_e_document_type: List[StrictStr] = Field(description="The type of document to retrieve.  1. **Signed** Is the final document once all signatures were applied. 2. **Proofdocument** Is the evidence report. 3. **Proof** Is the complete evidence archive including all of the above and more.", alias="a_eDocumentType")
    __properties: ClassVar[List[str]] = ["a_pkiEzsigndocumentID", "a_eDocumentType"]

    @field_validator('a_e_document_type')
    def a_e_document_type_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['Signed', 'Proof', 'Proofdocument']):
                raise ValueError("each list item must be one of ('Signed', 'Proof', 'Proofdocument')")
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
        """Create an instance of EzsignfolderBatchDownloadV1Request from a JSON string"""
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
        """Create an instance of EzsignfolderBatchDownloadV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "a_pkiEzsigndocumentID": obj.get("a_pkiEzsigndocumentID"),
            "a_eDocumentType": obj.get("a_eDocumentType")
        })
        return _obj


