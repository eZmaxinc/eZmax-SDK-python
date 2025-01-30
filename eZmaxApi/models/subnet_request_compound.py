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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.multilingual_subnet_description import MultilingualSubnetDescription
from typing import Optional, Set
from typing_extensions import Self

class SubnetRequestCompound(BaseModel):
    """
    A Subnet Object and children
    """ # noqa: E501
    pki_subnet_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Subnet", alias="pkiSubnetID")
    fki_user_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the User", alias="fkiUserID")
    fki_apikey_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Apikey", alias="fkiApikeyID")
    obj_subnet_description: MultilingualSubnetDescription = Field(alias="objSubnetDescription")
    i_subnet_network: Annotated[int, Field(le=4294967295, strict=True, ge=0)] = Field(description="The network of the Subnet in integer form. For example 8.8.8.0 would be 134744064", alias="iSubnetNetwork")
    i_subnet_mask: Annotated[int, Field(le=4294967295, strict=True, ge=0)] = Field(description="The mask of the Subnet  in integer form. For example 255.255.255.0 would be 4294967040", alias="iSubnetMask")
    __properties: ClassVar[List[str]] = ["pkiSubnetID", "fkiUserID", "fkiApikeyID", "objSubnetDescription", "iSubnetNetwork", "iSubnetMask"]

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
        """Create an instance of SubnetRequestCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_subnet_description
        if self.obj_subnet_description:
            _dict['objSubnetDescription'] = self.obj_subnet_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubnetRequestCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSubnetID": obj.get("pkiSubnetID"),
            "fkiUserID": obj.get("fkiUserID"),
            "fkiApikeyID": obj.get("fkiApikeyID"),
            "objSubnetDescription": MultilingualSubnetDescription.from_dict(obj["objSubnetDescription"]) if obj.get("objSubnetDescription") is not None else None,
            "iSubnetNetwork": obj.get("iSubnetNetwork"),
            "iSubnetMask": obj.get("iSubnetMask")
        })
        return _obj


