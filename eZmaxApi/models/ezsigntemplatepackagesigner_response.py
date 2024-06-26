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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatepackagesignerResponse(BaseModel):
    """
    A Ezsigntemplatepackagesigner Object
    """ # noqa: E501
    pki_ezsigntemplatepackagesigner_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatepackagesigner", alias="pkiEzsigntemplatepackagesignerID")
    fki_ezsigntemplatepackage_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatepackage", alias="fkiEzsigntemplatepackageID")
    s_ezsigntemplatepackagesigner_description: StrictStr = Field(description="The description of the Ezsigntemplatepackagesigner", alias="sEzsigntemplatepackagesignerDescription")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatepackagesignerID", "fkiEzsigntemplatepackageID", "sEzsigntemplatepackagesignerDescription"]

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
        """Create an instance of EzsigntemplatepackagesignerResponse from a JSON string"""
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
        """Create an instance of EzsigntemplatepackagesignerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatepackagesignerID": obj.get("pkiEzsigntemplatepackagesignerID"),
            "fkiEzsigntemplatepackageID": obj.get("fkiEzsigntemplatepackageID"),
            "sEzsigntemplatepackagesignerDescription": obj.get("sEzsigntemplatepackagesignerDescription")
        })
        return _obj


