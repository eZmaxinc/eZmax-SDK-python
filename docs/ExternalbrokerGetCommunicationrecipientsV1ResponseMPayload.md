# ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/externalbroker/{pkiExternalbrokerID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_get_communicationrecipients_v1_response_m_payload import ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload from a JSON string
externalbroker_get_communicationrecipients_v1_response_m_payload_instance = ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
externalbroker_get_communicationrecipients_v1_response_m_payload_dict = externalbroker_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload from a dict
externalbroker_get_communicationrecipients_v1_response_m_payload_from_dict = ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload.from_dict(externalbroker_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


