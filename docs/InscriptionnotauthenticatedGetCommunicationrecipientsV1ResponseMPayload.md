# InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload import InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload from a JSON string
inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload_instance = InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload_dict = inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload from a dict
inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload_from_dict = InscriptionnotauthenticatedGetCommunicationrecipientsV1ResponseMPayload.from_dict(inscriptionnotauthenticated_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


