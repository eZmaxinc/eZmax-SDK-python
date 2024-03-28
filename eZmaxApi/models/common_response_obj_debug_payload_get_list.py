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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from eZmaxApi.models.common_response_filter import CommonResponseFilter
from typing import Optional, Set
from typing_extensions import Self

class CommonResponseObjDebugPayloadGetList(BaseModel):
    """
    This is a debug object containing debugging information on the actual function
    """ # noqa: E501
    i_version_min: StrictInt = Field(description="The minimum version of the function that can be called", alias="iVersionMin")
    i_version_max: StrictInt = Field(description="The maximum version of the function that can be called", alias="iVersionMax")
    a_required_permission: List[StrictInt] = Field(description="An array of permissions required to access this function.  If the value \"0\" is present in the array, anyone can call this function.  You must have one of the permission to access the function. You don't need to have all of them.", alias="a_RequiredPermission")
    b_version_deprecated: StrictBool = Field(description="Wheter the current route is deprecated or not", alias="bVersionDeprecated")
    a_filter: CommonResponseFilter = Field(alias="a_Filter")
    a_order_by: Dict[str, StrictStr] = Field(description="List of available values for *eOrderBy*", alias="a_OrderBy")
    i_row_max: Annotated[int, Field(le=10000, strict=True, ge=1)] = Field(description="The maximum numbers of results to be returned.  When the content-type is **application/json** there is an implicit default of 10 000.  When it's **application/vnd.openxmlformats-officedocument.spreadsheetml.sheet** the is no implicit default so if you do not specify iRowMax, all records will be returned.", alias="iRowMax")
    i_row_offset: Annotated[int, Field(strict=True, ge=0)] = Field(description="The starting element from where to start retrieving the results. For example if you started at iRowOffset=0 and asked for iRowMax=100, to get the next 100 results, you could specify iRowOffset=100&iRowMax=100,", alias="iRowOffset")
    __properties: ClassVar[List[str]] = ["iVersionMin", "iVersionMax", "a_RequiredPermission", "bVersionDeprecated", "a_Filter", "a_OrderBy", "iRowMax", "iRowOffset"]

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
        """Create an instance of CommonResponseObjDebugPayloadGetList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of a_filter
        if self.a_filter:
            _dict['a_Filter'] = self.a_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonResponseObjDebugPayloadGetList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iVersionMin": obj.get("iVersionMin"),
            "iVersionMax": obj.get("iVersionMax"),
            "a_RequiredPermission": obj.get("a_RequiredPermission"),
            "bVersionDeprecated": obj.get("bVersionDeprecated"),
            "a_Filter": CommonResponseFilter.from_dict(obj["a_Filter"]) if obj.get("a_Filter") is not None else None,
            "a_OrderBy": obj.get("a_OrderBy"),
            "iRowMax": obj.get("iRowMax"),
            "iRowOffset": obj.get("iRowOffset") if obj.get("iRowOffset") is not None else 0
        })
        return _obj


