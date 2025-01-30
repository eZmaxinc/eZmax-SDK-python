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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsigntemplatesigner_mapping import FieldEEzsigntemplatesignerMapping
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatesignerResponse(BaseModel):
    """
    A Ezsigntemplatesigner Object
    """ # noqa: E501
    pki_ezsigntemplatesigner_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatesigner", alias="pkiEzsigntemplatesignerID")
    fki_ezsigntemplate_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplate", alias="fkiEzsigntemplateID")
    fki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserID")
    fki_usergroup_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupID")
    fki_ezdoctemplatedocument_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezdoctemplatedocument", alias="fkiEzdoctemplatedocumentID")
    b_ezsigntemplatesigner_receivecopy: Optional[StrictBool] = Field(default=None, description="If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain't required to sign the document.", alias="bEzsigntemplatesignerReceivecopy")
    e_ezsigntemplatesigner_mapping: Optional[FieldEEzsigntemplatesignerMapping] = Field(default=None, alias="eEzsigntemplatesignerMapping")
    s_ezsigntemplatesigner_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezsigntemplatesigner", alias="sEzsigntemplatesignerDescription")
    s_user_name: Optional[StrictStr] = Field(default=None, description="The description of the User in the language of the requester", alias="sUserName")
    s_usergroup_name_x: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Name of the Usergroup in the language of the requester", alias="sUsergroupNameX")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatesignerID", "fkiEzsigntemplateID", "fkiUserID", "fkiUsergroupID", "fkiEzdoctemplatedocumentID", "bEzsigntemplatesignerReceivecopy", "eEzsigntemplatesignerMapping", "sEzsigntemplatesignerDescription", "sUserName", "sUsergroupNameX"]

    @field_validator('s_ezsigntemplatesigner_description')
    def s_ezsigntemplatesigner_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,50}$/")
        return value

    @field_validator('s_usergroup_name_x')
    def s_usergroup_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
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
        """Create an instance of EzsigntemplatesignerResponse from a JSON string"""
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
        """Create an instance of EzsigntemplatesignerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplatesignerID": obj.get("pkiEzsigntemplatesignerID"),
            "fkiEzsigntemplateID": obj.get("fkiEzsigntemplateID"),
            "fkiUserID": obj.get("fkiUserID"),
            "fkiUsergroupID": obj.get("fkiUsergroupID"),
            "fkiEzdoctemplatedocumentID": obj.get("fkiEzdoctemplatedocumentID"),
            "bEzsigntemplatesignerReceivecopy": obj.get("bEzsigntemplatesignerReceivecopy"),
            "eEzsigntemplatesignerMapping": obj.get("eEzsigntemplatesignerMapping"),
            "sEzsigntemplatesignerDescription": obj.get("sEzsigntemplatesignerDescription"),
            "sUserName": obj.get("sUserName"),
            "sUsergroupNameX": obj.get("sUsergroupNameX")
        })
        return _obj


