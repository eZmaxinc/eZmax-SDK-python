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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from eZmaxApi.models.field_e_notificationpreference_status import FieldENotificationpreferenceStatus
from eZmaxApi.models.multilingual_notificationtest_name import MultilingualNotificationtestName
from typing import Optional, Set
from typing_extensions import Self

class CustomNotificationtestgetnotificationtestsResponse(BaseModel):
    """
    A Notificationtest Object in the context of getNotificationtests
    """ # noqa: E501
    pki_notificationtest_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Notificationtest", alias="pkiNotificationtestID")
    obj_notificationtest_name: MultilingualNotificationtestName = Field(alias="objNotificationtestName")
    fki_notificationsubsection_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Notificationsubsection", alias="fkiNotificationsubsectionID")
    s_notificationtest_function: StrictStr = Field(description="The function name of the Notificationtest", alias="sNotificationtestFunction")
    s_notificationtest_name_x: StrictStr = Field(description="The name of the Notificationtest in the language of the requester", alias="sNotificationtestNameX")
    e_notificationpreference_status: FieldENotificationpreferenceStatus = Field(alias="eNotificationpreferenceStatus")
    i_notificationtest: StrictInt = Field(description="The number of elements returned by the Notificationtest", alias="iNotificationtest")
    __properties: ClassVar[List[str]] = ["pkiNotificationtestID", "objNotificationtestName", "fkiNotificationsubsectionID", "sNotificationtestFunction", "sNotificationtestNameX", "eNotificationpreferenceStatus", "iNotificationtest"]

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
        """Create an instance of CustomNotificationtestgetnotificationtestsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of obj_notificationtest_name
        if self.obj_notificationtest_name:
            _dict['objNotificationtestName'] = self.obj_notificationtest_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomNotificationtestgetnotificationtestsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiNotificationtestID": obj.get("pkiNotificationtestID"),
            "objNotificationtestName": MultilingualNotificationtestName.from_dict(obj["objNotificationtestName"]) if obj.get("objNotificationtestName") is not None else None,
            "fkiNotificationsubsectionID": obj.get("fkiNotificationsubsectionID"),
            "sNotificationtestFunction": obj.get("sNotificationtestFunction"),
            "sNotificationtestNameX": obj.get("sNotificationtestNameX"),
            "eNotificationpreferenceStatus": obj.get("eNotificationpreferenceStatus"),
            "iNotificationtest": obj.get("iNotificationtest")
        })
        return _obj


