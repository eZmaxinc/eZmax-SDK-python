# SalaryGetCommunicationrecipientsV1Response

Response for GET /1/object/salary/{pkiSalaryID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalaryGetCommunicationrecipientsV1ResponseMPayload**](SalaryGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_get_communicationrecipients_v1_response import SalaryGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryGetCommunicationrecipientsV1Response from a JSON string
salary_get_communicationrecipients_v1_response_instance = SalaryGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(SalaryGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
salary_get_communicationrecipients_v1_response_dict = salary_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of SalaryGetCommunicationrecipientsV1Response from a dict
salary_get_communicationrecipients_v1_response_from_dict = SalaryGetCommunicationrecipientsV1Response.from_dict(salary_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


