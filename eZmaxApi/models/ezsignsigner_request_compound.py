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
from eZmaxApi.models.ezsignsigner_request_compound_contact import EzsignsignerRequestCompoundContact
from typing import Optional, Set
from typing_extensions import Self

class EzsignsignerRequestCompound(BaseModel):
    """
    An Ezsignsigner Object and children to create a complete structure
    """ # noqa: E501
    fki_userlogintype_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \"In-Person\" and there won't be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \"In-Person\" and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**|", alias="fkiUserlogintypeID")
    fki_taxassignment_id: Annotated[int, Field(le=15, strict=True, ge=0)] = Field(description="The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable|", alias="fkiTaxassignmentID")
    fki_secretquestion_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Secretquestion.  Valid values:  |Value|Description| |-|-| |1|The name of the hospital in which you were born| |2|The name of your grade school| |3|The last name of your favorite teacher| |4|Your favorite sports team| |5|Your favorite TV show| |6|Your favorite movie| |7|The name of the street on which you grew up| |8|The name of your first employer| |9|Your first car| |10|Your favorite food| |11|The name of your first pet| |12|Favorite musician/band| |13|What instrument you play| |14|Your father's middle name| |15|Your mother's maiden name| |16|Name of your eldest child| |17|Your spouse's middle name| |18|Favorite restaurant| |19|Childhood nickname| |20|Favorite vacation destination| |21|Your boat's name| |22|Date of Birth (YYYY-MM-DD)| |22|Secret Code| |22|Your reference code|", alias="fkiSecretquestionID")
    e_ezsignsigner_logintype: Optional[StrictStr] = Field(default=None, description="The method the Ezsignsigner will authenticate to the signing platform.  1. **Password** means the Ezsignsigner will receive a secure link by email. 2. **PasswordPhone** means the Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**. 3. **PasswordQuestion** means the Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer. 4. **InPersonPhone** means the Ezsignsigner will only be able to sign \"In-Person\" and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**. 5. **InPerson** means the Ezsignsigner will only be able to sign \"In-Person\" and there won't be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type.", alias="eEzsignsignerLogintype")
    s_ezsignsigner_secretanswer: Optional[StrictStr] = Field(default=None, description="The predefined answer to the secret question the Ezsignsigner will need to provide to successfully authenticate.", alias="sEzsignsignerSecretanswer")
    obj_contact: EzsignsignerRequestCompoundContact = Field(alias="objContact")
    __properties: ClassVar[List[str]] = ["fkiUserlogintypeID", "fkiTaxassignmentID", "fkiSecretquestionID", "eEzsignsignerLogintype", "sEzsignsignerSecretanswer", "objContact"]

    @field_validator('e_ezsignsigner_logintype')
    def e_ezsignsigner_logintype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Password', 'PasswordPhone', 'PasswordQuestion', 'InPersonPhone', 'InPerson']):
            raise ValueError("must be one of enum values ('Password', 'PasswordPhone', 'PasswordQuestion', 'InPersonPhone', 'InPerson')")
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
        """Create an instance of EzsignsignerRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_contact
        if self.obj_contact:
            _dict['objContact'] = self.obj_contact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignsignerRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkiUserlogintypeID": obj.get("fkiUserlogintypeID"),
            "fkiTaxassignmentID": obj.get("fkiTaxassignmentID"),
            "fkiSecretquestionID": obj.get("fkiSecretquestionID"),
            "eEzsignsignerLogintype": obj.get("eEzsignsignerLogintype"),
            "sEzsignsignerSecretanswer": obj.get("sEzsignsignerSecretanswer"),
            "objContact": EzsignsignerRequestCompoundContact.from_dict(obj["objContact"]) if obj.get("objContact") is not None else None
        })
        return _obj


