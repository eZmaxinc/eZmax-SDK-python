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
from eZmaxApi.models.field_e_ezsigntemplate_recognition import FieldEEzsigntemplateRecognition
from eZmaxApi.models.field_e_ezsigntemplate_type import FieldEEzsigntemplateType
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateRequestCompoundV3(BaseModel):
    """
    A Ezsigntemplate Object and children
    """ # noqa: E501
    pki_ezsigntemplate_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplate", alias="pkiEzsigntemplateID")
    fki_ezsignfoldertype_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    fki_ezdoctemplatedocument_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezdoctemplatedocument", alias="fkiEzdoctemplatedocumentID")
    s_ezsigntemplate_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezsigntemplate", alias="sEzsigntemplateDescription")
    s_ezsigntemplate_externaldescription: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The external description of the Ezsigntemplate", alias="sEzsigntemplateExternaldescription")
    t_ezsigntemplate_comment: Optional[StrictStr] = Field(default=None, description="The comment of the Ezsigntemplate", alias="tEzsigntemplateComment")
    e_ezsigntemplate_recognition: Optional[FieldEEzsigntemplateRecognition] = Field(default=FieldEEzsigntemplateRecognition.NO, alias="eEzsigntemplateRecognition")
    s_ezsigntemplate_filenameregexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The filename regexp of the Ezsigntemplate.", alias="sEzsigntemplateFilenameregexp")
    b_ezsigntemplate_adminonly: StrictBool = Field(description="Whether the Ezsigntemplate can be accessed by admin users only (eUserType=Normal)", alias="bEzsigntemplateAdminonly")
    e_ezsigntemplate_type: FieldEEzsigntemplateType = Field(alias="eEzsigntemplateType")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateID", "fkiEzsignfoldertypeID", "fkiLanguageID", "fkiEzdoctemplatedocumentID", "sEzsigntemplateDescription", "sEzsigntemplateExternaldescription", "tEzsigntemplateComment", "eEzsigntemplateRecognition", "sEzsigntemplateFilenameregexp", "bEzsigntemplateAdminonly", "eEzsigntemplateType"]

    @field_validator('s_ezsigntemplate_description')
    def s_ezsigntemplate_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,80}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,80}$/")
        return value

    @field_validator('s_ezsigntemplate_externaldescription')
    def s_ezsigntemplate_externaldescription_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,75}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,75}$/")
        return value

    @field_validator('s_ezsigntemplate_filenameregexp')
    def s_ezsigntemplate_filenameregexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{1,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,50}$/")
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
        """Create an instance of EzsigntemplateRequestCompoundV3 from a JSON string"""
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
        """Create an instance of EzsigntemplateRequestCompoundV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateID": obj.get("pkiEzsigntemplateID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "fkiEzdoctemplatedocumentID": obj.get("fkiEzdoctemplatedocumentID"),
            "sEzsigntemplateDescription": obj.get("sEzsigntemplateDescription"),
            "sEzsigntemplateExternaldescription": obj.get("sEzsigntemplateExternaldescription"),
            "tEzsigntemplateComment": obj.get("tEzsigntemplateComment"),
            "eEzsigntemplateRecognition": obj.get("eEzsigntemplateRecognition") if obj.get("eEzsigntemplateRecognition") is not None else FieldEEzsigntemplateRecognition.NO,
            "sEzsigntemplateFilenameregexp": obj.get("sEzsigntemplateFilenameregexp"),
            "bEzsigntemplateAdminonly": obj.get("bEzsigntemplateAdminonly"),
            "eEzsigntemplateType": obj.get("eEzsigntemplateType")
        })
        return _obj


