# CommonResponseObjDebug

This is a generic debug object that is returned by all API requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_memory_usage** | **str** | The peak memory allocated during the API request execution. Formatted as a human readable string | 
**s_run_time** | **str** | The total server execution time of the API request execution. Formatted as a human readable string | 
**i_sql_selects** | **int** | The number of SQL SELECT queries that were sent to the database server during the API request execution | 
**i_sql_queries** | **int** | The number of SQL INSERT/UPDATE/DELETE queries that were sent to the database server during the API request execution | 
**a_obj_sql_query** | [**List[CommonResponseObjSQLQuery]**](CommonResponseObjSQLQuery.md) | An array of the SQL Queries that were executed during the API request execution | 

## Example

```python
from eZmaxApi.models.common_response_obj_debug import CommonResponseObjDebug

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseObjDebug from a JSON string
common_response_obj_debug_instance = CommonResponseObjDebug.from_json(json)
# print the JSON string representation of the object
print(CommonResponseObjDebug.to_json())

# convert the object into a dict
common_response_obj_debug_dict = common_response_obj_debug_instance.to_dict()
# create an instance of CommonResponseObjDebug from a dict
common_response_obj_debug_from_dict = CommonResponseObjDebug.from_dict(common_response_obj_debug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


