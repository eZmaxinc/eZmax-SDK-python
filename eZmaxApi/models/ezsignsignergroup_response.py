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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.multilingual_ezsignsignergroup_description import MultilingualEzsignsignergroupDescription
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignergroupResponse(BaseModel):
    """
    An Ezsignsignergroup Object
    """ # noqa: E501
    pki_ezsignsignergroup_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezsignsignergroup", alias="pkiEzsignsignergroupID")
    obj_ezsignsignergroup_description: MultilingualEzsignsignergroupDescription = Field(alias="objEzsignsignergroupDescription")
    s_ezsignsignergroup_description_x: Optional[StrictStr] = Field(default=None, description="The Description of the Ezsignsignergroup in the language of the requester", alias="sEzsignsignergroupDescriptionX")
    __properties: ClassVar[List[str]] = ["pkiEzsignsignergroupID", "objEzsignsignergroupDescription", "sEzsignsignergroupDescriptionX"]

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
        """Create an instance of EzsignsignergroupResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignsignergroup_description
        if self.obj_ezsignsignergroup_description:
            _dict['objEzsignsignergroupDescription'] = self.obj_ezsignsignergroup_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignergroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignsignergroupID": obj.get("pkiEzsignsignergroupID"),
            "objEzsignsignergroupDescription": MultilingualEzsignsignergroupDescription.from_dict(obj["objEzsignsignergroupDescription"]) if obj.get("objEzsignsignergroupDescription") is not None else None,
            "sEzsignsignergroupDescriptionX": obj.get("sEzsignsignergroupDescriptionX")
        })
        return _obj


