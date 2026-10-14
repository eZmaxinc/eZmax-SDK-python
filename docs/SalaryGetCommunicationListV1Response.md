# SalaryGetCommunicationListV1Response

Response for GET /1/object/salary/{pkiSalaryID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalaryGetCommunicationListV1ResponseMPayload**](SalaryGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_get_communication_list_v1_response import SalaryGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryGetCommunicationListV1Response from a JSON string
salary_get_communication_list_v1_response_instance = SalaryGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(SalaryGetCommunicationListV1Response.to_json())

# convert the object into a dict
salary_get_communication_list_v1_response_dict = salary_get_communication_list_v1_response_instance.to_dict()
# create an instance of SalaryGetCommunicationListV1Response from a dict
salary_get_communication_list_v1_response_from_dict = SalaryGetCommunicationListV1Response.from_dict(salary_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


