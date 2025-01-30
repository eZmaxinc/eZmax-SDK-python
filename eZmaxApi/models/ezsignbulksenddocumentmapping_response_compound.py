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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.ezsigntemplate_response_compound import EzsigntemplateResponseCompound
from eZmaxApi.models.ezsigntemplatepackage_response_compound import EzsigntemplatepackageResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsignbulksenddocumentmappingResponseCompound(BaseModel):
    """
    A Ezsignbulksenddocumentmapping Object
    """ # noqa: E501
    pki_ezsignbulksenddocumentmapping_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignbulksenddocumentmapping.", alias="pkiEzsignbulksenddocumentmappingID")
    fki_ezsignbulksend_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignbulksend", alias="fkiEzsignbulksendID")
    fki_ezsigntemplatepackage_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatepackage", alias="fkiEzsigntemplatepackageID")
    fki_ezsigntemplate_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplate", alias="fkiEzsigntemplateID")
    i_ezsignbulksenddocumentmapping_order: Annotated[int, Field(strict=True, ge=0)] = Field(description="The order in which the Ezsigntemplate or Ezsigntemplatepackage will be presented to the signatory in the Ezsignfolder.", alias="iEzsignbulksenddocumentmappingOrder")
    obj_ezsigntemplate: Optional[EzsigntemplateResponseCompound] = Field(default=None, alias="objEzsigntemplate")
    obj_ezsigntemplatepackage: Optional[EzsigntemplatepackageResponseCompound] = Field(default=None, alias="objEzsigntemplatepackage")
    __properties: ClassVar[List[str]] = ["pkiEzsignbulksenddocumentmappingID", "fkiEzsignbulksendID", "fkiEzsigntemplatepackageID", "fkiEzsigntemplateID", "iEzsignbulksenddocumentmappingOrder", "objEzsigntemplate", "objEzsigntemplatepackage"]

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
        """Create an instance of EzsignbulksenddocumentmappingResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplate
        if self.obj_ezsigntemplate:
            _dict['objEzsigntemplate'] = self.obj_ezsigntemplate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplatepackage
        if self.obj_ezsigntemplatepackage:
            _dict['objEzsigntemplatepackage'] = self.obj_ezsigntemplatepackage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignbulksenddocumentmappingResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignbulksenddocumentmappingID": obj.get("pkiEzsignbulksenddocumentmappingID"),
            "fkiEzsignbulksendID": obj.get("fkiEzsignbulksendID"),
            "fkiEzsigntemplatepackageID": obj.get("fkiEzsigntemplatepackageID"),
            "fkiEzsigntemplateID": obj.get("fkiEzsigntemplateID"),
            "iEzsignbulksenddocumentmappingOrder": obj.get("iEzsignbulksenddocumentmappingOrder"),
            "objEzsigntemplate": EzsigntemplateResponseCompound.from_dict(obj["objEzsigntemplate"]) if obj.get("objEzsigntemplate") is not None else None,
            "objEzsigntemplatepackage": EzsigntemplatepackageResponseCompound.from_dict(obj["objEzsigntemplatepackage"]) if obj.get("objEzsigntemplatepackage") is not None else None
        })
        return _obj


