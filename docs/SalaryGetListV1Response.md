# SalaryGetListV1Response

Response for GET /1/object/salary/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalaryGetListV1ResponseMPayload**](SalaryGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_get_list_v1_response import SalaryGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryGetListV1Response from a JSON string
salary_get_list_v1_response_instance = SalaryGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(SalaryGetListV1Response.to_json())

# convert the object into a dict
salary_get_list_v1_response_dict = salary_get_list_v1_response_instance.to_dict()
# create an instance of SalaryGetListV1Response from a dict
salary_get_list_v1_response_from_dict = SalaryGetListV1Response.from_dict(salary_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


