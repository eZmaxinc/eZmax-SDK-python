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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from eZmaxApi.models.common_response_obj_sql_query import CommonResponseObjSQLQuery
from typing import Optional, Set
from typing_extensions import Self

class CommonResponseObjDebug(BaseModel):
    """
    This is a generic debug object that is returned by all API requests
    """ # noqa: E501
    s_memory_usage: StrictStr = Field(description="The peak memory allocated during the API request execution. Formatted as a human readable string", alias="sMemoryUsage")
    s_run_time: StrictStr = Field(description="The total server execution time of the API request execution. Formatted as a human readable string", alias="sRunTime")
    i_sql_selects: StrictInt = Field(description="The number of SQL SELECT queries that were sent to the database server during the API request execution", alias="iSQLSelects")
    i_sql_queries: StrictInt = Field(description="The number of SQL INSERT/UPDATE/DELETE queries that were sent to the database server during the API request execution", alias="iSQLQueries")
    a_obj_sql_query: List[CommonResponseObjSQLQuery] = Field(description="An array of the SQL Queries that were executed during the API request execution", alias="a_objSQLQuery")
    __properties: ClassVar[List[str]] = ["sMemoryUsage", "sRunTime", "iSQLSelects", "iSQLQueries", "a_objSQLQuery"]

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
        """Create an instance of CommonResponseObjDebug from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_sql_query (list)
        _items = []
        if self.a_obj_sql_query:
            for _item in self.a_obj_sql_query:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objSQLQuery'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonResponseObjDebug from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sMemoryUsage": obj.get("sMemoryUsage"),
            "sRunTime": obj.get("sRunTime"),
            "iSQLSelects": obj.get("iSQLSelects"),
            "iSQLQueries": obj.get("iSQLQueries"),
            "a_objSQLQuery": [CommonResponseObjSQLQuery.from_dict(_item) for _item in obj["a_objSQLQuery"]] if obj.get("a_objSQLQuery") is not None else None
        })
        return _obj


