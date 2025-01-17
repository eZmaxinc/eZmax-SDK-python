# InscriptionnotauthenticatedGetCommunicationrecipientsV1Response

Response for GET /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload**](InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_communicationrecipients_v1_response import InscriptionnotauthenticatedGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetCommunicationrecipientsV1Response from a JSON string
inscriptionnotauthenticated_get_communicationrecipients_v1_response_instance = InscriptionnotauthenticatedGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_communicationrecipients_v1_response_dict = inscriptionnotauthenticated_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetCommunicationrecipientsV1Response from a dict
inscriptionnotauthenticated_get_communicationrecipients_v1_response_from_dict = InscriptionnotauthenticatedGetCommunicationrecipientsV1Response.from_dict(inscriptionnotauthenticated_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


