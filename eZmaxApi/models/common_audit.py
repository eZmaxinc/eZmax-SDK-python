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
from eZmaxApi.models.common_auditdetail import CommonAuditdetail
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CommonAudit(BaseModel):
    """
    Gives informations about the user that created the object and the last user to have modified it.  If the object was never modified after creation, objAuditdetailModified won't be returned. 
    """ # noqa: E501
    obj_auditdetail_created: CommonAuditdetail = Field(alias="objAuditdetailCreated")
    obj_auditdetail_modified: Optional[CommonAuditdetail] = Field(default=None, alias="objAuditdetailModified")
    __properties: ClassVar[List[str]] = ["objAuditdetailCreated", "objAuditdetailModified"]

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
        """Create an instance of CommonAudit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_auditdetail_created
        if self.obj_auditdetail_created:
            _dict['objAuditdetailCreated'] = self.obj_auditdetail_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_auditdetail_modified
        if self.obj_auditdetail_modified:
            _dict['objAuditdetailModified'] = self.obj_auditdetail_modified.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CommonAudit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objAuditdetailCreated": CommonAuditdetail.from_dict(obj.get("objAuditdetailCreated")) if obj.get("objAuditdetailCreated") is not None else None,
            "objAuditdetailModified": CommonAuditdetail.from_dict(obj.get("objAuditdetailModified")) if obj.get("objAuditdetailModified") is not None else None
        })
        return _obj


