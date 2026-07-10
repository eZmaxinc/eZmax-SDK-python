# InscriptionnotauthenticatedGetObjectV2Response

Response for GET /2/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionnotauthenticatedGetObjectV2ResponseMPayload**](InscriptionnotauthenticatedGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_get_object_v2_response import InscriptionnotauthenticatedGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedGetObjectV2Response from a JSON string
inscriptionnotauthenticated_get_object_v2_response_instance = InscriptionnotauthenticatedGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedGetObjectV2Response.to_json())

# convert the object into a dict
inscriptionnotauthenticated_get_object_v2_response_dict = inscriptionnotauthenticated_get_object_v2_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedGetObjectV2Response from a dict
inscriptionnotauthenticated_get_object_v2_response_from_dict = InscriptionnotauthenticatedGetObjectV2Response.from_dict(inscriptionnotauthenticated_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


