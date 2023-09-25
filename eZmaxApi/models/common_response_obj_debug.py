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


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from eZmaxApi.models.common_response_obj_sql_query import CommonResponseObjSQLQuery

class CommonResponseObjDebug(BaseModel):
    """
    This is a generic debug object that is returned by all API requests  # noqa: E501
    """
    s_memory_usage: StrictStr = Field(..., alias="sMemoryUsage", description="The peak memory allocated during the API request execution. Formatted as a human readable string")
    s_run_time: StrictStr = Field(..., alias="sRunTime", description="The total server execution time of the API request execution. Formatted as a human readable string")
    i_sql_selects: StrictInt = Field(..., alias="iSQLSelects", description="The number of SQL SELECT queries that were sent to the database server during the API request execution")
    i_sql_queries: StrictInt = Field(..., alias="iSQLQueries", description="The number of SQL INSERT/UPDATE/DELETE queries that were sent to the database server during the API request execution")
    a_obj_sql_query: conlist(CommonResponseObjSQLQuery) = Field(..., alias="a_objSQLQuery", description="An array of the SQL Queries that were executed during the API request execution")
    __properties = ["sMemoryUsage", "sRunTime", "iSQLSelects", "iSQLQueries", "a_objSQLQuery"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CommonResponseObjDebug:
        """Create an instance of CommonResponseObjDebug from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_sql_query (list)
        _items = []
        if self.a_obj_sql_query:
            for _item in self.a_obj_sql_query:
                if _item:
                    _items.append(_item.to_dict())
            _dict['a_objSQLQuery'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommonResponseObjDebug:
        """Create an instance of CommonResponseObjDebug from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommonResponseObjDebug.parse_obj(obj)

        _obj = CommonResponseObjDebug.parse_obj({
            "s_memory_usage": obj.get("sMemoryUsage"),
            "s_run_time": obj.get("sRunTime"),
            "i_sql_selects": obj.get("iSQLSelects"),
            "i_sql_queries": obj.get("iSQLQueries"),
            "a_obj_sql_query": [CommonResponseObjSQLQuery.from_dict(_item) for _item in obj.get("a_objSQLQuery")] if obj.get("a_objSQLQuery") is not None else None
        })
        return _obj


