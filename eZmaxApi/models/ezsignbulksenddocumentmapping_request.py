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
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzsignbulksenddocumentmappingRequest(BaseModel):
    """
    A Ezsignbulksenddocumentmapping Object
    """ # noqa: E501
    pki_ezsignbulksenddocumentmapping_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignbulksenddocumentmapping.", alias="pkiEzsignbulksenddocumentmappingID")
    fki_ezsignbulksend_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignbulksend", alias="fkiEzsignbulksendID")
    fki_ezsigntemplatepackage_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatepackage", alias="fkiEzsigntemplatepackageID")
    fki_ezsigntemplate_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplate", alias="fkiEzsigntemplateID")
    __properties: ClassVar[List[str]] = ["pkiEzsignbulksenddocumentmappingID", "fkiEzsignbulksendID", "fkiEzsigntemplatepackageID", "fkiEzsigntemplateID"]

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
        """Create an instance of EzsignbulksenddocumentmappingRequest from a JSON string"""
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
        """Create an instance of EzsignbulksenddocumentmappingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignbulksenddocumentmappingID": obj.get("pkiEzsignbulksenddocumentmappingID"),
            "fkiEzsignbulksendID": obj.get("fkiEzsignbulksendID"),
            "fkiEzsigntemplatepackageID": obj.get("fkiEzsigntemplatepackageID"),
            "fkiEzsigntemplateID": obj.get("fkiEzsigntemplateID")
        })
        return _obj


