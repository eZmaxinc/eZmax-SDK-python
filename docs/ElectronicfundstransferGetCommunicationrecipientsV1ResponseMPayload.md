# ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_communicationrecipients_v1_response_m_payload import ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload from a JSON string
electronicfundstransfer_get_communicationrecipients_v1_response_m_payload_instance = ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
electronicfundstransfer_get_communicationrecipients_v1_response_m_payload_dict = electronicfundstransfer_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload from a dict
electronicfundstransfer_get_communicationrecipients_v1_response_m_payload_from_dict = ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload.from_dict(electronicfundstransfer_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


