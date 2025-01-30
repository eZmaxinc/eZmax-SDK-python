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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.custom_contact_name_response import CustomContactNameResponse
from eZmaxApi.models.multilingual_apikey_description import MultilingualApikeyDescription
from typing import Optional, Set
from typing_extensions import Self

class ApikeyResponse(BaseModel):
    """
    An Apikey Object
    """ # noqa: E501
    pki_apikey_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Apikey", alias="pkiApikeyID")
    fki_user_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserID")
    obj_apikey_description: MultilingualApikeyDescription = Field(alias="objApikeyDescription")
    obj_contact_name: CustomContactNameResponse = Field(alias="objContactName")
    s_apikey_apikey: Optional[StrictStr] = Field(default=None, description="The Apikey for the API key.  This will be hidden if we are not creating or regenerating the Apikey.", alias="sApikeyApikey")
    s_apikey_secret: Optional[StrictStr] = Field(default=None, description="The Secret for the API key.  This will be hidden if we are not creating or regenerating the Apikey.", alias="sApikeySecret")
    b_apikey_isactive: StrictBool = Field(description="Whether the apikey is active or not", alias="bApikeyIsactive")
    b_apikey_issigned: Optional[StrictBool] = Field(default=None, description="Whether the apikey is signed or not", alias="bApikeyIssigned")
    obj_audit: CommonAudit = Field(alias="objAudit")
    __properties: ClassVar[List[str]] = ["pkiApikeyID", "fkiUserID", "objApikeyDescription", "objContactName", "sApikeyApikey", "sApikeySecret", "bApikeyIsactive", "bApikeyIssigned", "objAudit"]

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
        """Create an instance of ApikeyResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_apikey_description
        if self.obj_apikey_description:
            _dict['objApikeyDescription'] = self.obj_apikey_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_contact_name
        if self.obj_contact_name:
            _dict['objContactName'] = self.obj_contact_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApikeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiApikeyID": obj.get("pkiApikeyID"),
            "fkiUserID": obj.get("fkiUserID"),
            "objApikeyDescription": MultilingualApikeyDescription.from_dict(obj["objApikeyDescription"]) if obj.get("objApikeyDescription") is not None else None,
            "objContactName": CustomContactNameResponse.from_dict(obj["objContactName"]) if obj.get("objContactName") is not None else None,
            "sApikeyApikey": obj.get("sApikeyApikey"),
            "sApikeySecret": obj.get("sApikeySecret"),
            "bApikeyIsactive": obj.get("bApikeyIsactive"),
            "bApikeyIssigned": obj.get("bApikeyIssigned"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None
        })
        return _obj


