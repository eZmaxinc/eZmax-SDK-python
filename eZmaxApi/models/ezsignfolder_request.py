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
from eZmaxApi.models.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
from typing import Optional, Set
from typing_extensions import Self

class EzsignfolderRequest(BaseModel):
    """
    An Ezsignfolder Object
    """ # noqa: E501
    pki_ezsignfolder_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignfolder", alias="pkiEzsignfolderID")
    fki_ezsignfoldertype_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    fki_ezsigntsarequirement_id: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server's time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server's time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**|", alias="fkiEzsigntsarequirementID")
    s_ezsignfolder_description: StrictStr = Field(description="The description of the Ezsignfolder", alias="sEzsignfolderDescription")
    t_ezsignfolder_note: Optional[StrictStr] = Field(default=None, description="Note about the Ezsignfolder", alias="tEzsignfolderNote")
    e_ezsignfolder_sendreminderfrequency: FieldEEzsignfolderSendreminderfrequency = Field(alias="eEzsignfolderSendreminderfrequency")
    s_ezsignfolder_externalid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This field can be used to store an External ID from the client's system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format. ", alias="sEzsignfolderExternalid")
    __properties: ClassVar[List[str]] = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "fkiEzsigntsarequirementID", "sEzsignfolderDescription", "tEzsignfolderNote", "eEzsignfolderSendreminderfrequency", "sEzsignfolderExternalid"]

    @field_validator('s_ezsignfolder_externalid')
    def s_ezsignfolder_externalid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,128}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,128}$/")
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
        """Create an instance of EzsignfolderRequest from a JSON string"""
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
        """Create an instance of EzsignfolderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfolderID": obj.get("pkiEzsignfolderID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "tEzsignfolderNote": obj.get("tEzsignfolderNote"),
            "eEzsignfolderSendreminderfrequency": obj.get("eEzsignfolderSendreminderfrequency"),
            "sEzsignfolderExternalid": obj.get("sEzsignfolderExternalid")
        })
        return _obj


