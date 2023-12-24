# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PermissionRequest(BaseModel):
    """
    A Permission Object
    """ # noqa: E501
    pki_permission_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Permission", alias="pkiPermissionID")
    fki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserID")
    fki_apikey_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Apikey", alias="fkiApikeyID")
    fki_usergroup_id: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Usergroup", alias="fkiUsergroupID")
    fki_company_id: Optional[Annotated[int, Field(le=255, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Company", alias="fkiCompanyID")
    fki_modulesection_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Modulesection", alias="fkiModulesectionID")
    __properties: ClassVar[List[str]] = ["pkiPermissionID", "fkiUserID", "fkiApikeyID", "fkiUsergroupID", "fkiCompanyID", "fkiModulesectionID"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PermissionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PermissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiPermissionID": obj.get("pkiPermissionID"),
            "fkiUserID": obj.get("fkiUserID"),
            "fkiApikeyID": obj.get("fkiApikeyID"),
            "fkiUsergroupID": obj.get("fkiUsergroupID"),
            "fkiCompanyID": obj.get("fkiCompanyID"),
            "fkiModulesectionID": obj.get("fkiModulesectionID")
        })
        return _obj


