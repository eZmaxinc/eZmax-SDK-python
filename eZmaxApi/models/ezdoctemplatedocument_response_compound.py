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
from eZmaxApi.models.field_e_ezdoctemplatedocument_privacylevel import FieldEEzdoctemplatedocumentPrivacylevel
from eZmaxApi.models.multilingual_ezdoctemplatedocument_name import MultilingualEzdoctemplatedocumentName
from typing import Optional, Set
from typing_extensions import Self

class EzdoctemplatedocumentResponseCompound(BaseModel):
    """
    A Ezdoctemplatedocument Object
    """ # noqa: E501
    pki_ezdoctemplatedocument_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezdoctemplatedocument", alias="pkiEzdoctemplatedocumentID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    fki_ezsignfoldertype_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    fki_ezdoctemplatetype_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Ezdoctemplatetype", alias="fkiEzdoctemplatetypeID")
    fki_ezdoctemplatefieldtypecategory_id: Annotated[int, Field(le=255, strict=True, ge=0)] = Field(description="The unique ID of the Ezdoctemplatefieldtypecategory", alias="fkiEzdoctemplatefieldtypecategoryID")
    e_ezdoctemplatedocument_privacylevel: Optional[FieldEEzdoctemplatedocumentPrivacylevel] = Field(default=None, alias="eEzdoctemplatedocumentPrivacylevel")
    b_ezdoctemplatedocument_isactive: StrictBool = Field(description="Whether the ezdoctemplatedocument is active or not", alias="bEzdoctemplatedocumentIsactive")
    obj_ezdoctemplatedocument_name: MultilingualEzdoctemplatedocumentName = Field(alias="objEzdoctemplatedocumentName")
    s_ezdoctemplatedocument_name_x: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The name of the Ezdoctemplatedocument in the language of the requester", alias="sEzdoctemplatedocumentNameX")
    s_ezsignfoldertype_name_x: Optional[StrictStr] = Field(default=None, description="The name of the Ezsignfoldertype in the language of the requester", alias="sEzsignfoldertypeNameX")
    s_ezdoctemplatefieldtypecategory_description_x: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezdoctemplatefieldtypecategory in the language of the requester", alias="sEzdoctemplatefieldtypecategoryDescriptionX")
    s_ezdoctemplatetype_description_x: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezdoctemplatetype in the language of the requester", alias="sEzdoctemplatetypeDescriptionX")
    __properties: ClassVar[List[str]] = ["pkiEzdoctemplatedocumentID", "fkiLanguageID", "fkiEzsignfoldertypeID", "fkiEzdoctemplatetypeID", "fkiEzdoctemplatefieldtypecategoryID", "eEzdoctemplatedocumentPrivacylevel", "bEzdoctemplatedocumentIsactive", "objEzdoctemplatedocumentName", "sEzdoctemplatedocumentNameX", "sEzsignfoldertypeNameX", "sEzdoctemplatefieldtypecategoryDescriptionX", "sEzdoctemplatetypeDescriptionX"]

    @field_validator('s_ezdoctemplatedocument_name_x')
    def s_ezdoctemplatedocument_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_ezdoctemplatefieldtypecategory_description_x')
    def s_ezdoctemplatefieldtypecategory_description_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,55}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,55}$/")
        return value

    @field_validator('s_ezdoctemplatetype_description_x')
    def s_ezdoctemplatetype_description_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of EzdoctemplatedocumentResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_ezdoctemplatedocument_name
        if self.obj_ezdoctemplatedocument_name:
            _dict['objEzdoctemplatedocumentName'] = self.obj_ezdoctemplatedocument_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzdoctemplatedocumentResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzdoctemplatedocumentID": obj.get("pkiEzdoctemplatedocumentID"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "fkiEzdoctemplatetypeID": obj.get("fkiEzdoctemplatetypeID"),
            "fkiEzdoctemplatefieldtypecategoryID": obj.get("fkiEzdoctemplatefieldtypecategoryID"),
            "eEzdoctemplatedocumentPrivacylevel": obj.get("eEzdoctemplatedocumentPrivacylevel"),
            "bEzdoctemplatedocumentIsactive": obj.get("bEzdoctemplatedocumentIsactive"),
            "objEzdoctemplatedocumentName": MultilingualEzdoctemplatedocumentName.from_dict(obj["objEzdoctemplatedocumentName"]) if obj.get("objEzdoctemplatedocumentName") is not None else None,
            "sEzdoctemplatedocumentNameX": obj.get("sEzdoctemplatedocumentNameX"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "sEzdoctemplatefieldtypecategoryDescriptionX": obj.get("sEzdoctemplatefieldtypecategoryDescriptionX"),
            "sEzdoctemplatetypeDescriptionX": obj.get("sEzdoctemplatetypeDescriptionX")
        })
        return _obj


