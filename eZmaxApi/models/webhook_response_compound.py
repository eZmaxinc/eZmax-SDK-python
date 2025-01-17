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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.field_e_webhook_ezsignevent import FieldEWebhookEzsignevent
from eZmaxApi.models.field_e_webhook_managementevent import FieldEWebhookManagementevent
from eZmaxApi.models.field_e_webhook_module import FieldEWebhookModule
from eZmaxApi.models.webhook_response import WebhookResponse
from eZmaxApi.models.webhookheader_response_compound import WebhookheaderResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class WebhookResponseCompound(WebhookResponse):
    """
    A Webhook Object
    """ # noqa: E501
    s_webhook_event: Optional[StrictStr] = Field(default=None, description="The concatenated string to describe the Webhook event", alias="sWebhookEvent")
    a_obj_webhookheader: Optional[List[WebhookheaderResponseCompound]] = Field(default=None, alias="a_objWebhookheader")
    __properties: ClassVar[List[str]] = ["pkiWebhookID", "fkiAuthenticationexternalID", "sWebhookDescription", "fkiEzsignfoldertypeID", "sEzsignfoldertypeNameX", "eWebhookModule", "eWebhookEzsignevent", "eWebhookManagementevent", "sWebhookUrl", "sWebhookEmailfailed", "sWebhookApikey", "sWebhookSecret", "bWebhookIsactive", "bWebhookIssigned", "bWebhookSkipsslvalidation", "sAuthenticationexternalDescription", "objAudit", "sWebhookEvent", "a_objWebhookheader"]

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
        """Create an instance of WebhookResponseCompound from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_webhookheader (list)
        _items = []
        if self.a_obj_webhookheader:
            for _item_a_obj_webhookheader in self.a_obj_webhookheader:
                if _item_a_obj_webhookheader:
                    _items.append(_item_a_obj_webhookheader.to_dict())
            _dict['a_objWebhookheader'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Self]:
        """Create an instance of WebhookResponseCompound from a dict"""


