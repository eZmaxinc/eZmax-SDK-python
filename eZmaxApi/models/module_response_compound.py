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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.modulesection_response_compound import ModulesectionResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class ModuleResponseCompound(BaseModel):
    """
    A Module Object
    """ # noqa: E501
    pki_module_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Module", alias="pkiModuleID")
    fki_modulegroup_id: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The unique ID of the Modulegroup", alias="fkiModulegroupID")
    e_module_internalname: StrictStr = Field(description="The Internal name of the Module.  This is theoretically an enum field but there are so many possibles values we decided not to list them all.", alias="eModuleInternalname")
    s_module_name_x: StrictStr = Field(description="The Name of the Module in the language of the requester", alias="sModuleNameX")
    b_module_registered: StrictBool = Field(description="Whether the Module is registered or not", alias="bModuleRegistered")
    b_module_registeredapi: StrictBool = Field(description="Whether the Module is registered or not for api use", alias="bModuleRegisteredapi")
    a_obj_modulesection: Optional[List[ModulesectionResponseCompound]] = Field(default=None, alias="a_objModulesection")
    __properties: ClassVar[List[str]] = ["pkiModuleID", "fkiModulegroupID", "eModuleInternalname", "sModuleNameX", "bModuleRegistered", "bModuleRegisteredapi", "a_objModulesection"]

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
        """Create an instance of ModuleResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_modulesection (list)
        _items = []
        if self.a_obj_modulesection:
            for _item_a_obj_modulesection in self.a_obj_modulesection:
                if _item_a_obj_modulesection:
                    _items.append(_item_a_obj_modulesection.to_dict())
            _dict['a_objModulesection'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModuleResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiModuleID": obj.get("pkiModuleID"),
            "fkiModulegroupID": obj.get("fkiModulegroupID"),
            "eModuleInternalname": obj.get("eModuleInternalname"),
            "sModuleNameX": obj.get("sModuleNameX"),
            "bModuleRegistered": obj.get("bModuleRegistered"),
            "bModuleRegisteredapi": obj.get("bModuleRegisteredapi"),
            "a_objModulesection": [ModulesectionResponseCompound.from_dict(_item) for _item in obj["a_objModulesection"]] if obj.get("a_objModulesection") is not None else None
        })
        return _obj


