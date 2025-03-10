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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.contactinformations_request_compound import ContactinformationsRequestCompound
from typing import Optional, Set
from typing_extensions import Self

class ContactRequestCompound(BaseModel):
    """
    A Contact Object and children to create a complete structure
    """ # noqa: E501
    fki_contacttitle_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)|", alias="fkiContacttitleID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    s_contact_firstname: Annotated[str, Field(strict=True)] = Field(description="The First name of the contact", alias="sContactFirstname")
    s_contact_lastname: Annotated[str, Field(strict=True)] = Field(description="The Last name of the contact", alias="sContactLastname")
    s_contact_company: StrictStr = Field(description="The Company name of the contact", alias="sContactCompany")
    dt_contact_birthdate: Optional[StrictStr] = Field(default=None, description="The Birth Date of the contact", alias="dtContactBirthdate")
    obj_contactinformations: ContactinformationsRequestCompound = Field(alias="objContactinformations")
    __properties: ClassVar[List[str]] = ["fkiContacttitleID", "fkiLanguageID", "sContactFirstname", "sContactLastname", "sContactCompany", "dtContactBirthdate", "objContactinformations"]

    @field_validator('s_contact_firstname')
    def s_contact_firstname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,20}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,20}$/")
        return value

    @field_validator('s_contact_lastname')
    def s_contact_lastname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{1,25}$", value):
            raise ValueError(r"must validate the regular expression /^.{1,25}$/")
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
        """Create an instance of ContactRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_contactinformations
        if self.obj_contactinformations:
            _dict['objContactinformations'] = self.obj_contactinformations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiContacttitleID": obj.get("fkiContacttitleID"),
            "fkiLanguageID": obj.get("fkiLanguageID"),
            "sContactFirstname": obj.get("sContactFirstname"),
            "sContactLastname": obj.get("sContactLastname"),
            "sContactCompany": obj.get("sContactCompany"),
            "dtContactBirthdate": obj.get("dtContactBirthdate"),
            "objContactinformations": ContactinformationsRequestCompound.from_dict(obj["objContactinformations"]) if obj.get("objContactinformations") is not None else None
        })
        return _obj


