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
from eZmaxApi.models.ezsigndocument_request import EzsigndocumentRequest
from eZmaxApi.models.ezsigndocument_request_compound import EzsigndocumentRequestCompound
from typing import Optional, Set
from typing_extensions import Self

class EzsigndocumentCreateObjectV1Request(BaseModel):
    """
    Request for POST /1/object/ezsigndocument
    """ # noqa: E501
    obj_ezsigndocument: Optional[EzsigndocumentRequest] = Field(default=None, alias="objEzsigndocument")
    obj_ezsigndocument_compound: Optional[EzsigndocumentRequestCompound] = Field(default=None, alias="objEzsigndocumentCompound")
    __properties: ClassVar[List[str]] = ["objEzsigndocument", "objEzsigndocumentCompound"]

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
        """Create an instance of EzsigndocumentCreateObjectV1Request from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigndocument
        if self.obj_ezsigndocument:
            _dict['objEzsigndocument'] = self.obj_ezsigndocument.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigndocument_compound
        if self.obj_ezsigndocument_compound:
            _dict['objEzsigndocumentCompound'] = self.obj_ezsigndocument_compound.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigndocumentCreateObjectV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objEzsigndocument": EzsigndocumentRequest.from_dict(obj["objEzsigndocument"]) if obj.get("objEzsigndocument") is not None else None,
            "objEzsigndocumentCompound": EzsigndocumentRequestCompound.from_dict(obj["objEzsigndocumentCompound"]) if obj.get("objEzsigndocumentCompound") is not None else None
        })
        return _obj


