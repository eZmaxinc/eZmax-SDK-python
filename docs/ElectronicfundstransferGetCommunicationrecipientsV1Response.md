# ElectronicfundstransferGetCommunicationrecipientsV1Response

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload**](ElectronicfundstransferGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_communicationrecipients_v1_response import ElectronicfundstransferGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetCommunicationrecipientsV1Response from a JSON string
electronicfundstransfer_get_communicationrecipients_v1_response_instance = ElectronicfundstransferGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_get_communicationrecipients_v1_response_dict = electronicfundstransfer_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransferGetCommunicationrecipientsV1Response from a dict
electronicfundstransfer_get_communicationrecipients_v1_response_from_dict = ElectronicfundstransferGetCommunicationrecipientsV1Response.from_dict(electronicfundstransfer_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


