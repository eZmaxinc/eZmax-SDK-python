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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.ezsigntemplateglobaldocument_response import EzsigntemplateglobaldocumentResponse
from eZmaxApi.models.ezsigntemplateglobalsigner_response_compound import EzsigntemplateglobalsignerResponseCompound
from eZmaxApi.models.field_e_ezsigntemplateglobal_module import FieldEEzsigntemplateglobalModule
from eZmaxApi.models.field_e_ezsigntemplateglobal_supplier import FieldEEzsigntemplateglobalSupplier
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateglobalResponseCompound(BaseModel):
    """
    A Ezsigntemplateglobal Object
    """ # noqa: E501
    pki_ezsigntemplateglobal_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplateglobal", alias="pkiEzsigntemplateglobalID")
    fki_ezsigntemplateglobaldocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplateglobaldocument", alias="fkiEzsigntemplateglobaldocumentID")
    fki_module_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Module", alias="fkiModuleID")
    s_module_name_x: Optional[StrictStr] = Field(default=None, description="The Name of the Module in the language of the requester", alias="sModuleNameX")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_language_name_x: StrictStr = Field(description="The Name of the Language in the language of the requester", alias="sLanguageNameX")
    e_ezsigntemplateglobal_module: FieldEEzsigntemplateglobalModule = Field(alias="eEzsigntemplateglobalModule")
    e_ezsigntemplateglobal_supplier: FieldEEzsigntemplateglobalSupplier = Field(alias="eEzsigntemplateglobalSupplier")
    s_ezsigntemplateglobal_code: Annotated[str, Field(strict=True)] = Field(description="The Code of the Ezsigntemplateglobal", alias="sEzsigntemplateglobalCode")
    s_ezsigntemplateglobal_description: StrictStr = Field(description="The description of the Ezsigntemplate", alias="sEzsigntemplateglobalDescription")
    obj_ezsigntemplateglobaldocument: Optional[EzsigntemplateglobaldocumentResponse] = Field(default=None, alias="objEzsigntemplateglobaldocument")
    a_obj_ezsigntemplateglobalsigner: List[EzsigntemplateglobalsignerResponseCompound] = Field(alias="a_objEzsigntemplateglobalsigner")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateglobalID", "fkiEzsigntemplateglobaldocumentID", "fkiModuleID", "sModuleNameX", "fkiLanguageID", "sLanguageNameX", "eEzsigntemplateglobalModule", "eEzsigntemplateglobalSupplier", "sEzsigntemplateglobalCode", "sEzsigntemplateglobalDescription", "objEzsigntemplateglobaldocument", "a_objEzsigntemplateglobalsigner"]

    @field_validator('s_ezsigntemplateglobal_code')
    def s_ezsigntemplateglobal_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,10}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,10}$/")
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
        """Create an instance of EzsigntemplateglobalResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezsigntemplateglobaldocument
        if self.obj_ezsigntemplateglobaldocument:
            _dict['objEzsigntemplateglobaldocument'] = self.obj_ezsigntemplateglobaldocument.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsigntemplateglobalsigner (list)
        _items = []
        if self.a_obj_ezsigntemplateglobalsigner:
            for _item in self.a_obj_ezsigntemplateglobalsigner:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objEzsigntemplateglobalsigner'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsigntemplateglobalResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateglobalID": obj.get("pkiEzsigntemplateglobalID"),
            "fkiEzsigntemplateglobaldocumentID": obj.get("fkiEzsigntemplateglobaldocumentID"),
            "fkiModuleID": obj.get("fkiModuleID"),
            "sModuleNameX": obj.get("sModuleNameX"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sLanguageNameX": obj.get("sLanguageNameX"),
            "eEzsigntemplateglobalModule": obj.get("eEzsigntemplateglobalModule"),
            "eEzsigntemplateglobalSupplier": obj.get("eEzsigntemplateglobalSupplier"),
            "sEzsigntemplateglobalCode": obj.get("sEzsigntemplateglobalCode"),
            "sEzsigntemplateglobalDescription": obj.get("sEzsigntemplateglobalDescription"),
            "objEzsigntemplateglobaldocument": EzsigntemplateglobaldocumentResponse.from_dict(obj["objEzsigntemplateglobaldocument"]) if obj.get("objEzsigntemplateglobaldocument") is not None else None,
            "a_objEzsigntemplateglobalsigner": [EzsigntemplateglobalsignerResponseCompound.from_dict(_item) for _item in obj["a_objEzsigntemplateglobalsigner"]] if obj.get("a_objEzsigntemplateglobalsigner") is not None else None
        })
        return _obj


