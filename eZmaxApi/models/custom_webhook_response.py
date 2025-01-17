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

from pydantic import ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.field_e_webhook_ezsignevent import FieldEWebhookEzsignevent
from eZmaxApi.models.field_e_webhook_managementevent import FieldEWebhookManagementevent
from eZmaxApi.models.field_e_webhook_module import FieldEWebhookModule
from eZmaxApi.models.webhook_response_compound import WebhookResponseCompound
from eZmaxApi.models.webhookheader_response_compound import WebhookheaderResponseCompound
from typing import Optional, Set
from typing_extensions import Self

class CustomWebhookResponse(WebhookResponseCompound):
    """
    A custom Webhook object
    """ # noqa: E501
    pks_customer_code: Annotated[str, Field(min_length=2, strict=True, max_length=6)] = Field(description="The customer code assigned to your account", alias="pksCustomerCode")
    b_webhook_test: StrictBool = Field(description="Wheter the webhook received is a manual test or a real event", alias="bWebhookTest")
    e_webhook_emittype: Optional[StrictStr] = Field(default=None, description="Wheter the webhook received is a manual test or a real event", alias="eWebhookEmittype")
    __properties: ClassVar[List[str]] = ["pkiWebhookID", "fkiAuthenticationexternalID", "sWebhookDescription", "fkiEzsignfoldertypeID", "sEzsignfoldertypeNameX", "eWebhookModule", "eWebhookEzsignevent", "eWebhookManagementevent", "sWebhookUrl", "sWebhookEmailfailed", "sWebhookApikey", "sWebhookSecret", "bWebhookIsactive", "bWebhookIssigned", "bWebhookSkipsslvalidation", "sAuthenticationexternalDescription", "objAudit", "sWebhookEvent", "a_objWebhookheader", "pksCustomerCode", "bWebhookTest", "eWebhookEmittype"]

    @field_validator('e_webhook_emittype')
    def e_webhook_emittype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Automatic', 'Manual', 'Test']):
            raise ValueError("must be one of enum values ('Automatic', 'Manual', 'Test')")
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
        """Create an instance of CustomWebhookResponse from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomWebhookResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiWebhookID": obj.get("pkiWebhookID"),
            "fkiAuthenticationexternalID": obj.get("fkiAuthenticationexternalID"),
            "sWebhookDescription": obj.get("sWebhookDescription"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "eWebhookModule": obj.get("eWebhookModule"),
            "eWebhookEzsignevent": obj.get("eWebhookEzsignevent"),
            "eWebhookManagementevent": obj.get("eWebhookManagementevent"),
            "sWebhookUrl": obj.get("sWebhookUrl"),
            "sWebhookEmailfailed": obj.get("sWebhookEmailfailed"),
            "sWebhookApikey": obj.get("sWebhookApikey"),
            "sWebhookSecret": obj.get("sWebhookSecret"),
            "bWebhookIsactive": obj.get("bWebhookIsactive"),
            "bWebhookIssigned": obj.get("bWebhookIssigned"),
            "bWebhookSkipsslvalidation": obj.get("bWebhookSkipsslvalidation"),
            "sAuthenticationexternalDescription": obj.get("sAuthenticationexternalDescription"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "sWebhookEvent": obj.get("sWebhookEvent"),
            "a_objWebhookheader": [WebhookheaderResponseCompound.from_dict(_item) for _item in obj["a_objWebhookheader"]] if obj.get("a_objWebhookheader") is not None else None,
            "pksCustomerCode": obj.get("pksCustomerCode"),
            "bWebhookTest": obj.get("bWebhookTest"),
            "eWebhookEmittype": obj.get("eWebhookEmittype")
        })
        return _obj


