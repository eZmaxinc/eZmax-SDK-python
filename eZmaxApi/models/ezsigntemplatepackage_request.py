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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplatepackageRequest(BaseModel):
    """
    A Ezsigntemplatepackage Object
    """ # noqa: E501
    pki_ezsigntemplatepackage_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsigntemplatepackage", alias="pkiEzsigntemplatepackageID")
    fki_ezsignfoldertype_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    fki_ezdoctemplatedocument_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezdoctemplatedocument", alias="fkiEzdoctemplatedocumentID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_ezsigntemplatepackage_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezsigntemplatepackage", alias="sEzsigntemplatepackageDescription")
    b_ezsigntemplatepackage_adminonly: StrictBool = Field(description="Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType=Normal)", alias="bEzsigntemplatepackageAdminonly")
    b_ezsigntemplatepackage_isactive: StrictBool = Field(description="Whether the Ezsigntemplatepackage is active or not", alias="bEzsigntemplatepackageIsactive")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplatepackageID", "fkiEzsignfoldertypeID", "fkiEzdoctemplatedocumentID", "fkiLanguageID", "sEzsigntemplatepackageDescription", "bEzsigntemplatepackageAdminonly", "bEzsigntemplatepackageIsactive"]

    @field_validator('s_ezsigntemplatepackage_description')
    def s_ezsigntemplatepackage_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,80}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,80}$/")
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
        """Create an instance of EzsigntemplatepackageRequest from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of EzsigntemplatepackageRequest from a dict"""


