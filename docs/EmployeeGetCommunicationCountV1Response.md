# EmployeeGetCommunicationCountV1Response

Response for GET /1/object/employee/{pkiEmployeeID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EmployeeGetCommunicationCountV1ResponseMPayload**](EmployeeGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.employee_get_communication_count_v1_response import EmployeeGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeGetCommunicationCountV1Response from a JSON string
employee_get_communication_count_v1_response_instance = EmployeeGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(EmployeeGetCommunicationCountV1Response.to_json())

# convert the object into a dict
employee_get_communication_count_v1_response_dict = employee_get_communication_count_v1_response_instance.to_dict()
# create an instance of EmployeeGetCommunicationCountV1Response from a dict
employee_get_communication_count_v1_response_from_dict = EmployeeGetCommunicationCountV1Response.from_dict(employee_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


