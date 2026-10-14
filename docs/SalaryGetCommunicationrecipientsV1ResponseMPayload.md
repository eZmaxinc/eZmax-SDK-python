# SalaryGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/salary/{pkiSalaryID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.salary_get_communicationrecipients_v1_response_m_payload import SalaryGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryGetCommunicationrecipientsV1ResponseMPayload from a JSON string
salary_get_communicationrecipients_v1_response_m_payload_instance = SalaryGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SalaryGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
salary_get_communicationrecipients_v1_response_m_payload_dict = salary_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of SalaryGetCommunicationrecipientsV1ResponseMPayload from a dict
salary_get_communicationrecipients_v1_response_m_payload_from_dict = SalaryGetCommunicationrecipientsV1ResponseMPayload.from_dict(salary_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


