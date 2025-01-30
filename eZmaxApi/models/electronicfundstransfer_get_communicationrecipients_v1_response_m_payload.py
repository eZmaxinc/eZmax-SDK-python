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
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.custom_communicationrecipientsgroup_response import CustomCommunicationrecipientsgroupResponse
from typing import Optional, Set
from typing_extensions import Self

class ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload(BaseModel):
    """
    Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationrecipients
    """ # noqa: E501
    a_obj_communicationrecipientsgroup: List[CustomCommunicationrecipientsgroupResponse] = Field(alias="a_objCommunicationrecipientsgroup")
    __properties: ClassVar[List[str]] = ["a_objCommunicationrecipientsgroup"]

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
        """Create an instance of ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_communicationrecipientsgroup (list)
        _items = []
        if self.a_obj_communicationrecipientsgroup:
            for _item_a_obj_communicationrecipientsgroup in self.a_obj_communicationrecipientsgroup:
                if _item_a_obj_communicationrecipientsgroup:
                    _items.append(_item_a_obj_communicationrecipientsgroup.to_dict())
            _dict['a_objCommunicationrecipientsgroup'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "a_objCommunicationrecipientsgroup": [CustomCommunicationrecipientsgroupResponse.from_dict(_item) for _item in obj["a_objCommunicationrecipientsgroup"]] if obj.get("a_objCommunicationrecipientsgroup") is not None else None
        })
        return _obj


