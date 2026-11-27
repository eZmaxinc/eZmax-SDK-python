# InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload import InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload_instance = InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload_dict = inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload from a dict
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload_from_dict = InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload.from_dict(inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


