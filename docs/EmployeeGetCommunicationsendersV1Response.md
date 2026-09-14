# EmployeeGetCommunicationsendersV1Response

Response for GET /1/object/employee/{pkiEmployeeID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EmployeeGetCommunicationsendersV1ResponseMPayload**](EmployeeGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.employee_get_communicationsenders_v1_response import EmployeeGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeGetCommunicationsendersV1Response from a JSON string
employee_get_communicationsenders_v1_response_instance = EmployeeGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(EmployeeGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
employee_get_communicationsenders_v1_response_dict = employee_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of EmployeeGetCommunicationsendersV1Response from a dict
employee_get_communicationsenders_v1_response_from_dict = EmployeeGetCommunicationsendersV1Response.from_dict(employee_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


