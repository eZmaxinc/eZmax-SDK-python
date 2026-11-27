# InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response

Response for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload**](InscriptionnotauthenticatedSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_sync_documenttypechecklist_v1_response import InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response from a JSON string
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_instance = InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_dict = inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response from a dict
inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_from_dict = InscriptionnotauthenticatedSyncDocumenttypechecklistV1Response.from_dict(inscriptionnotauthenticated_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


