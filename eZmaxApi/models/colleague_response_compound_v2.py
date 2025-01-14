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
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_user_name_response import CustomUserNameResponse
from eZmaxApi.models.field_e_colleague_ezsign import FieldEColleagueEzsign
from eZmaxApi.models.field_e_colleague_realestateinprogess import FieldEColleagueRealestateinprogess
from typing import Optional, Set
from typing_extensions import Self

class ColleagueResponseCompoundV2(BaseModel):
    """
    A Colleague Object
    """ # noqa: E501
    pki_colleague_id: Annotated[int, Field(le=65535, strict=True, ge=0)] = Field(description="The unique ID of the Colleague", alias="pkiColleagueID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    fki_user_id_colleague: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserIDColleague")
    b_colleague_ezsignemail: StrictBool = Field(description="Whether the email can be used by the cloning user in Ezsign", alias="bColleagueEzsignemail")
    b_colleague_financial: StrictBool = Field(description="Whether the cloning user has access to the financial", alias="bColleagueFinancial")
    b_colleague_usecloneemail: StrictBool = Field(description="Whether the cloning user has access to the cloned user email to send communications", alias="bColleagueUsecloneemail")
    b_colleague_attachment: StrictBool = Field(description="Whether the cloning user has access to the attachment", alias="bColleagueAttachment")
    b_colleague_canafe: StrictBool = Field(description="Whether the cloning user has access to canafe", alias="bColleagueCanafe")
    b_colleague_permission: StrictBool = Field(description="Whether the cloning user copies the permission of the cloned user", alias="bColleaguePermission")
    b_colleague_realestatecompleted: StrictBool = Field(description="Whether if the cloning user has access to the completed folders in real estate", alias="bColleagueRealestatecompleted")
    dt_colleague_from: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The from of the Colleague", alias="dtColleagueFrom")
    dt_colleague_to: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The to of the Colleague", alias="dtColleagueTo")
    e_colleague_ezsign: FieldEColleagueEzsign = Field(alias="eColleagueEzsign")
    e_colleague_realestateinprogress: FieldEColleagueRealestateinprogess = Field(alias="eColleagueRealestateinprogress")
    obj_user_name: CustomUserNameResponse = Field(alias="objUserName")
    obj_audit: CommonAudit = Field(alias="objAudit")
    __properties: ClassVar[List[str]] = ["pkiColleagueID", "fkiUserID", "fkiUserIDColleague", "bColleagueEzsignemail", "bColleagueFinancial", "bColleagueUsecloneemail", "bColleagueAttachment", "bColleagueCanafe", "bColleaguePermission", "bColleagueRealestatecompleted", "dtColleagueFrom", "dtColleagueTo", "eColleagueEzsign", "eColleagueRealestateinprogress", "objUserName", "objAudit"]

    @field_validator('dt_colleague_from')
    def dt_colleague_from_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
        return value

    @field_validator('dt_colleague_to')
    def dt_colleague_to_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
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
        """Create an instance of ColleagueResponseCompoundV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_user_name
        if self.obj_user_name:
            _dict['objUserName'] = self.obj_user_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ColleagueResponseCompoundV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiColleagueID": obj.get("pkiColleagueID"),
            "fkiUserID": obj.get("fkiUserID"),
            "fkiUserIDColleague": obj.get("fkiUserIDColleague"),
            "bColleagueEzsignemail": obj.get("bColleagueEzsignemail"),
            "bColleagueFinancial": obj.get("bColleagueFinancial"),
            "bColleagueUsecloneemail": obj.get("bColleagueUsecloneemail"),
            "bColleagueAttachment": obj.get("bColleagueAttachment"),
            "bColleagueCanafe": obj.get("bColleagueCanafe"),
            "bColleaguePermission": obj.get("bColleaguePermission"),
            "bColleagueRealestatecompleted": obj.get("bColleagueRealestatecompleted"),
            "dtColleagueFrom": obj.get("dtColleagueFrom"),
            "dtColleagueTo": obj.get("dtColleagueTo"),
            "eColleagueEzsign": obj.get("eColleagueEzsign"),
            "eColleagueRealestateinprogress": obj.get("eColleagueRealestateinprogress"),
            "objUserName": CustomUserNameResponse.from_dict(obj["objUserName"]) if obj.get("objUserName") is not None else None,
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None
        })
        return _obj


