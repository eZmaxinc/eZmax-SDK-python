# InscriptionnotauthenticatedGetDocumenttypechecklistV1Response

Response for GET /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionnotauthenticatedGetDocumenttypechecklistV1ResponseMPayload**](InscriptionnotauthenticatedGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_documenttypechecklist_v1_response import InscriptionnotauthenticatedGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetDocumenttypechecklistV1Response from a JSON string
inscriptionnotauthenticated_get_documenttypechecklist_v1_response_instance = InscriptionnotauthenticatedGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_documenttypechecklist_v1_response_dict = inscriptionnotauthenticated_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetDocumenttypechecklistV1Response from a dict
inscriptionnotauthenticated_get_documenttypechecklist_v1_response_from_dict = InscriptionnotauthenticatedGetDocumenttypechecklistV1Response.from_dict(inscriptionnotauthenticated_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


