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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.contactinformations_response_compound import ContactinformationsResponseCompound
from eZmaxApi.models.field_e_contact_type import FieldEContactType
from typing import Optional, Set
from typing_extensions import Self

class ContactResponse(BaseModel):
    """
    A Contact Object
    """ # noqa: E501
    pki_contact_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Contact", alias="pkiContactID")
    fki_language_id: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|", alias="fkiLanguageID")
    fki_contacttitle_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)|", alias="fkiContacttitleID")
    fki_contactinformations_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Contactinformations", alias="fkiContactinformationsID")
    dt_contact_birthdate: Optional[StrictStr] = Field(default=None, description="The Birth Date of the contact", alias="dtContactBirthdate")
    e_contact_type: FieldEContactType = Field(alias="eContactType")
    s_contact_firstname: StrictStr = Field(description="The First name of the contact", alias="sContactFirstname")
    s_contact_lastname: StrictStr = Field(description="The Last name of the contact", alias="sContactLastname")
    s_contact_company: Optional[StrictStr] = Field(default=None, description="The Company name of the contact", alias="sContactCompany")
    s_contact_occupation: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The occupation of the Contact", alias="sContactOccupation")
    t_contact_note: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The note of the Contact", alias="tContactNote")
    b_contact_isactive: StrictBool = Field(description="Whether the contact is active or not", alias="bContactIsactive")
    obj_contactinformations: ContactinformationsResponseCompound = Field(alias="objContactinformations")
    __properties: ClassVar[List[str]] = ["pkiContactID", "fkiLanguageID", "fkiContacttitleID", "fkiContactinformationsID", "dtContactBirthdate", "eContactType", "sContactFirstname", "sContactLastname", "sContactCompany", "sContactOccupation", "tContactNote", "bContactIsactive", "objContactinformations"]

    @field_validator('s_contact_occupation')
    def s_contact_occupation_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('t_contact_note')
    def t_contact_note_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,32000}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,32000}$/")
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
        """Create an instance of ContactResponse from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of ContactResponse from a dict"""


