# InscriptionnotauthenticatedImportIntoEDMV1Response

Response for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload**](InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_import_into_edmv1_response import InscriptionnotauthenticatedImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1Response from a JSON string
inscriptionnotauthenticated_import_into_edmv1_response_instance = InscriptionnotauthenticatedImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedImportIntoEDMV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_import_into_edmv1_response_dict = inscriptionnotauthenticated_import_into_edmv1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1Response from a dict
inscriptionnotauthenticated_import_into_edmv1_response_from_dict = InscriptionnotauthenticatedImportIntoEDMV1Response.from_dict(inscriptionnotauthenticated_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


