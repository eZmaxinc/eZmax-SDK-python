# CommonResponseObjSQLQuery

Definition of objSQLQuery Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_query** | **str** | The SQL Query | 
**f_duration** | **float** | Execution time of the SQL Query in seconds | 

## Example

```python
from eZmaxApi.models.common_response_obj_sql_query import CommonResponseObjSQLQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseObjSQLQuery from a JSON string
common_response_obj_sql_query_instance = CommonResponseObjSQLQuery.from_json(json)
# print the JSON string representation of the object
print CommonResponseObjSQLQuery.to_json()

# convert the object into a dict
common_response_obj_sql_query_dict = common_response_obj_sql_query_instance.to_dict()
# create an instance of CommonResponseObjSQLQuery from a dict
common_response_obj_sql_query_form_dict = common_response_obj_sql_query.from_dict(common_response_obj_sql_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


