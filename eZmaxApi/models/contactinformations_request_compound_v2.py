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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.address_request_compound import AddressRequestCompound
from eZmaxApi.models.email_request_compound import EmailRequestCompound
from eZmaxApi.models.field_e_contactinformations_type import FieldEContactinformationsType
from eZmaxApi.models.phone_request_compound import PhoneRequestCompound
from eZmaxApi.models.website_request_compound import WebsiteRequestCompound
from typing import Optional, Set
from typing_extensions import Self

class ContactinformationsRequestCompoundV2(BaseModel):
    """
    A Contactinformations Object and children to create a complete structure
    """ # noqa: E501
    e_contactinformations_type: FieldEContactinformationsType = Field(alias="eContactinformationsType")
    i_address_default: StrictInt = Field(description="The index in the a_objAddress array (zero based index) representing the Address object that should become the default one.  You can leave the value to 0 if the array is empty.", alias="iAddressDefault")
    i_phone_default: StrictInt = Field(description="The index in the a_objPhone array (zero based index) representing the Phone object that should become the default one.  You can leave the value to 0 if the array is empty.", alias="iPhoneDefault")
    i_email_default: StrictInt = Field(description="The index in the a_objEmail array (zero based index) representing the Email object that should become the default one.  You can leave the value to 0 if the array is empty.", alias="iEmailDefault")
    i_website_default: StrictInt = Field(description="The index in the a_objWebsite array (zero based index) representing the Website object that should become the default one.  You can leave the value to 0 if the array is empty.", alias="iWebsiteDefault")
    a_obj_address: List[AddressRequestCompound] = Field(alias="a_objAddress")
    a_obj_phone: List[PhoneRequestCompound] = Field(alias="a_objPhone")
    a_obj_email: List[EmailRequestCompound] = Field(alias="a_objEmail")
    a_obj_website: List[WebsiteRequestCompound] = Field(alias="a_objWebsite")
    __properties: ClassVar[List[str]] = ["eContactinformationsType", "iAddressDefault", "iPhoneDefault", "iEmailDefault", "iWebsiteDefault", "a_objAddress", "a_objPhone", "a_objEmail", "a_objWebsite"]

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
        """Create an instance of ContactinformationsRequestCompoundV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_address (list)
        _items = []
        if self.a_obj_address:
            for _item_a_obj_address in self.a_obj_address:
                if _item_a_obj_address:
                    _items.append(_item_a_obj_address.to_dict())
            _dict['a_objAddress'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_phone (list)
        _items = []
        if self.a_obj_phone:
            for _item_a_obj_phone in self.a_obj_phone:
                if _item_a_obj_phone:
                    _items.append(_item_a_obj_phone.to_dict())
            _dict['a_objPhone'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_email (list)
        _items = []
        if self.a_obj_email:
            for _item_a_obj_email in self.a_obj_email:
                if _item_a_obj_email:
                    _items.append(_item_a_obj_email.to_dict())
            _dict['a_objEmail'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_website (list)
        _items = []
        if self.a_obj_website:
            for _item_a_obj_website in self.a_obj_website:
                if _item_a_obj_website:
                    _items.append(_item_a_obj_website.to_dict())
            _dict['a_objWebsite'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactinformationsRequestCompoundV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eContactinformationsType": obj.get("eContactinformationsType"),
            "iAddressDefault": obj.get("iAddressDefault"),
            "iPhoneDefault": obj.get("iPhoneDefault"),
            "iEmailDefault": obj.get("iEmailDefault"),
            "iWebsiteDefault": obj.get("iWebsiteDefault"),
            "a_objAddress": [AddressRequestCompound.from_dict(_item) for _item in obj["a_objAddress"]] if obj.get("a_objAddress") is not None else None,
            "a_objPhone": [PhoneRequestCompound.from_dict(_item) for _item in obj["a_objPhone"]] if obj.get("a_objPhone") is not None else None,
            "a_objEmail": [EmailRequestCompound.from_dict(_item) for _item in obj["a_objEmail"]] if obj.get("a_objEmail") is not None else None,
            "a_objWebsite": [WebsiteRequestCompound.from_dict(_item) for _item in obj["a_objWebsite"]] if obj.get("a_objWebsite") is not None else None
        })
        return _obj


