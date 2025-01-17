# InscriptionGetCommunicationrecipientsV1Response

Response for GET /1/object/inscription/{pkiInscriptionID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**InscriptionGetCommunicationrecipientsV1ResponseMPayload**](InscriptionGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_communicationrecipients_v1_response import InscriptionGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetCommunicationrecipientsV1Response from a JSON string
inscription_get_communicationrecipients_v1_response_instance = InscriptionGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
inscription_get_communicationrecipients_v1_response_dict = inscription_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of InscriptionGetCommunicationrecipientsV1Response from a dict
inscription_get_communicationrecipients_v1_response_from_dict = InscriptionGetCommunicationrecipientsV1Response.from_dict(inscription_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


