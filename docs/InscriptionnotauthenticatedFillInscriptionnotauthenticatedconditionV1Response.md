# InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response

Response for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/fillInscriptionnotauthenticatedcondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response import InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response from a JSON string
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response_instance = InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response_dict = inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response from a dict
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response_from_dict = InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Response.from_dict(inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


