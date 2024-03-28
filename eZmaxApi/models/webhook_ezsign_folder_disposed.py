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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.attempt_response_compound import AttemptResponseCompound
from eZmaxApi.models.custom_webhook_response import CustomWebhookResponse
from eZmaxApi.models.ezsignfolder_response import EzsignfolderResponse
from typing import Optional, Set
from typing_extensions import Self

class WebhookEzsignFolderDisposed(BaseModel):
    """
    This is the base Webhook object
    """ # noqa: E501
    obj_webhook: CustomWebhookResponse = Field(alias="objWebhook")
    a_obj_attempt: List[AttemptResponseCompound] = Field(description="An array containing details of previous attempts that were made to deliver the message. The array is empty if it's the first attempt.", alias="a_objAttempt")
    obj_ezsignfolder: EzsignfolderResponse = Field(alias="objEzsignfolder")
    __properties: ClassVar[List[str]] = ["objWebhook", "a_objAttempt", "objEzsignfolder"]

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
        """Create an instance of WebhookEzsignFolderDisposed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_webhook
        if self.obj_webhook:
            _dict['objWebhook'] = self.obj_webhook.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_attempt (list)
        _items = []
        if self.a_obj_attempt:
            for _item in self.a_obj_attempt:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objAttempt'] = _items
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfolder
        if self.obj_ezsignfolder:
            _dict['objEzsignfolder'] = self.obj_ezsignfolder.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookEzsignFolderDisposed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objWebhook": CustomWebhookResponse.from_dict(obj["objWebhook"]) if obj.get("objWebhook") is not None else None,
            "a_objAttempt": [AttemptResponseCompound.from_dict(_item) for _item in obj["a_objAttempt"]] if obj.get("a_objAttempt") is not None else None,
            "objEzsignfolder": EzsignfolderResponse.from_dict(obj["objEzsignfolder"]) if obj.get("objEzsignfolder") is not None else None
        })
        return _obj


