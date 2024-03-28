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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class NotificationtestGetElementsV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/notificationtest/{pkiNotificationtestID}/getElements
    """ # noqa: E501
    pki_notificationtest_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Notificationtest", alias="pkiNotificationtestID")
    s_notificationtest_function: StrictStr = Field(description="The function name of the Notificationtest", alias="sNotificationtestFunction")
    a_s_variableobject_property: List[StrictStr] = Field(alias="a_sVariableobjectProperty")
    a_obj_variableobject: List[Dict[str, Any]] = Field(alias="a_objVariableobject")
    __properties: ClassVar[List[str]] = ["pkiNotificationtestID", "sNotificationtestFunction", "a_sVariableobjectProperty", "a_objVariableobject"]

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
        """Create an instance of NotificationtestGetElementsV1ResponseMPayload from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationtestGetElementsV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiNotificationtestID": obj.get("pkiNotificationtestID"),
            "sNotificationtestFunction": obj.get("sNotificationtestFunction"),
            "a_sVariableobjectProperty": obj.get("a_sVariableobjectProperty"),
            "a_objVariableobject": obj.get("a_objVariableobject")
        })
        return _obj


