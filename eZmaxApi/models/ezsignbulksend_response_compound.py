# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.ezsignbulksend_response import EzsignbulksendResponse
from eZmaxApi.models.ezsignbulksenddocumentmapping_response_compound import EzsignbulksenddocumentmappingResponseCompound
from eZmaxApi.models.ezsignbulksendsignermapping_response import EzsignbulksendsignermappingResponse
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
from typing import Optional, Set
from typing_extensions import Self

class EzsignbulksendResponseCompound(EzsignbulksendResponse):
    """
    An Ezsignbulksend Object and children to create a complete structure
    """ # noqa: E501
    a_obj_ezsignbulksenddocumentmapping: List[EzsignbulksenddocumentmappingResponseCompound] = Field(alias="a_objEzsignbulksenddocumentmapping")
    a_obj_ezsignbulksendsignermapping: List[EzsignbulksendsignermappingResponse] = Field(alias="a_objEzsignbulksendsignermapping")
    __properties: ClassVar[List[str]] = ["pkiEzsignbulksendID", "fkiEzsignfoldertypeID", "fkiLanguageID", "sLanguageNameX", "eEzsignfoldertypePrivacylevel", "sEzsignfoldertypeNameX", "sEzsignbulksendDescription", "tEzsignbulksendNote", "bEzsignbulksendNeedvalidation", "bEzsignbulksendIsactive", "objAudit", "a_objEzsignbulksenddocumentmapping", "a_objEzsignbulksendsignermapping"]

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
        """Create an instance of EzsignbulksendResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignbulksenddocumentmapping (list)
        _items = []
        if self.a_obj_ezsignbulksenddocumentmapping:
            for _item_a_obj_ezsignbulksenddocumentmapping in self.a_obj_ezsignbulksenddocumentmapping:
                if _item_a_obj_ezsignbulksenddocumentmapping:
                    _items.append(_item_a_obj_ezsignbulksenddocumentmapping.to_dict())
            _dict['a_objEzsignbulksenddocumentmapping'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignbulksendsignermapping (list)
        _items = []
        if self.a_obj_ezsignbulksendsignermapping:
            for _item_a_obj_ezsignbulksendsignermapping in self.a_obj_ezsignbulksendsignermapping:
                if _item_a_obj_ezsignbulksendsignermapping:
                    _items.append(_item_a_obj_ezsignbulksendsignermapping.to_dict())
            _dict['a_objEzsignbulksendsignermapping'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignbulksendResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignbulksendID": obj.get("pkiEzsignbulksendID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sLanguageNameX": obj.get("sLanguageNameX"),
            "eEzsignfoldertypePrivacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "sEzsignbulksendDescription": obj.get("sEzsignbulksendDescription"),
            "tEzsignbulksendNote": obj.get("tEzsignbulksendNote"),
            "bEzsignbulksendNeedvalidation": obj.get("bEzsignbulksendNeedvalidation"),
            "bEzsignbulksendIsactive": obj.get("bEzsignbulksendIsactive"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "a_objEzsignbulksenddocumentmapping": [EzsignbulksenddocumentmappingResponseCompound.from_dict(_item) for _item in obj["a_objEzsignbulksenddocumentmapping"]] if obj.get("a_objEzsignbulksenddocumentmapping") is not None else None,
            "a_objEzsignbulksendsignermapping": [EzsignbulksendsignermappingResponse.from_dict(_item) for _item in obj["a_objEzsignbulksendsignermapping"]] if obj.get("a_objEzsignbulksendsignermapping") is not None else None
        })
        return _obj


