# InscriptionnotauthenticatedGetCommunicationListV1Response

Response for GET /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload**](InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_communication_list_v1_response import InscriptionnotauthenticatedGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetCommunicationListV1Response from a JSON string
inscriptionnotauthenticated_get_communication_list_v1_response_instance = InscriptionnotauthenticatedGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetCommunicationListV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_communication_list_v1_response_dict = inscriptionnotauthenticated_get_communication_list_v1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetCommunicationListV1Response from a dict
inscriptionnotauthenticated_get_communication_list_v1_response_from_dict = InscriptionnotauthenticatedGetCommunicationListV1Response.from_dict(inscriptionnotauthenticated_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


