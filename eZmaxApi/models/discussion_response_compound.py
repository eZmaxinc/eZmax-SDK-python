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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.custom_discussionconfiguration_response import CustomDiscussionconfigurationResponse
from eZmaxApi.models.discussionmembership_response_compound import DiscussionmembershipResponseCompound
from eZmaxApi.models.discussionmessage_response_compound import DiscussionmessageResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class DiscussionResponseCompound(BaseModel):
    """
    A Discussion Object
    """ # noqa: E501
    pki_discussion_id: Annotated[int, Field(le=16777215, strict=True, ge=0)] = Field(description="The unique ID of the Discussion", alias="pkiDiscussionID")
    s_discussion_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Discussion", alias="sDiscussionDescription")
    b_discussion_closed: StrictBool = Field(description="Whether if it's an closed", alias="bDiscussionClosed")
    dt_discussion_lastread: Optional[StrictStr] = Field(default=None, description="The date the Discussion was last read", alias="dtDiscussionLastread")
    i_discussionmessage_count: StrictInt = Field(description="The count of Attachment.", alias="iDiscussionmessageCount")
    i_discussionmessage_countunread: StrictInt = Field(description="The count of Attachment.", alias="iDiscussionmessageCountunread")
    obj_discussionconfiguration: Optional[CustomDiscussionconfigurationResponse] = Field(default=None, alias="objDiscussionconfiguration")
    a_obj_discussionmembership: List[DiscussionmembershipResponseCompound] = Field(alias="a_objDiscussionmembership")
    a_obj_discussionmessage: List[DiscussionmessageResponseCompound] = Field(alias="a_objDiscussionmessage")
    __properties: ClassVar[List[str]] = ["pkiDiscussionID", "sDiscussionDescription", "bDiscussionClosed", "dtDiscussionLastread", "iDiscussionmessageCount", "iDiscussionmessageCountunread", "objDiscussionconfiguration", "a_objDiscussionmembership", "a_objDiscussionmessage"]

    @field_validator('s_discussion_description')
    def s_discussion_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,75}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,75}$/")
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
        """Create an instance of DiscussionResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_discussionconfiguration
        if self.obj_discussionconfiguration:
            _dict['objDiscussionconfiguration'] = self.obj_discussionconfiguration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_discussionmembership (list)
        _items = []
        if self.a_obj_discussionmembership:
            for _item_a_obj_discussionmembership in self.a_obj_discussionmembership:
                if _item_a_obj_discussionmembership:
                    _items.append(_item_a_obj_discussionmembership.to_dict())
            _dict['a_objDiscussionmembership'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_discussionmessage (list)
        _items = []
        if self.a_obj_discussionmessage:
            for _item_a_obj_discussionmessage in self.a_obj_discussionmessage:
                if _item_a_obj_discussionmessage:
                    _items.append(_item_a_obj_discussionmessage.to_dict())
            _dict['a_objDiscussionmessage'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DiscussionResponseCompound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiDiscussionID": obj.get("pkiDiscussionID"),
            "sDiscussionDescription": obj.get("sDiscussionDescription"),
            "bDiscussionClosed": obj.get("bDiscussionClosed"),
            "dtDiscussionLastread": obj.get("dtDiscussionLastread"),
            "iDiscussionmessageCount": obj.get("iDiscussionmessageCount"),
            "iDiscussionmessageCountunread": obj.get("iDiscussionmessageCountunread"),
            "objDiscussionconfiguration": CustomDiscussionconfigurationResponse.from_dict(obj["objDiscussionconfiguration"]) if obj.get("objDiscussionconfiguration") is not None else None,
            "a_objDiscussionmembership": [DiscussionmembershipResponseCompound.from_dict(_item) for _item in obj["a_objDiscussionmembership"]] if obj.get("a_objDiscussionmembership") is not None else None,
            "a_objDiscussionmessage": [DiscussionmessageResponseCompound.from_dict(_item) for _item in obj["a_objDiscussionmessage"]] if obj.get("a_objDiscussionmessage") is not None else None
        })
        return _obj


