# InscriptionnotauthenticatedGetObjectV2ResponseMPayload

Payload for GET /2/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_inscriptionnotauthenticated** | [**InscriptionnotauthenticatedResponseCompound**](InscriptionnotauthenticatedResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_object_v2_response_m_payload import InscriptionnotauthenticatedGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetObjectV2ResponseMPayload from a JSON string
inscriptionnotauthenticated_get_object_v2_response_m_payload_instance = InscriptionnotauthenticatedGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_object_v2_response_m_payload_dict = inscriptionnotauthenticated_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetObjectV2ResponseMPayload from a dict
inscriptionnotauthenticated_get_object_v2_response_m_payload_from_dict = InscriptionnotauthenticatedGetObjectV2ResponseMPayload.from_dict(inscriptionnotauthenticated_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


