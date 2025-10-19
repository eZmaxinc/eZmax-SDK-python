# InscriptionchecklistGetAutocompleteV3Response

Response for GET /3/object/inscriptionchecklist/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionchecklistGetAutocompleteV3ResponseMPayload**](InscriptionchecklistGetAutocompleteV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionchecklist_get_autocomplete_v3_response import InscriptionchecklistGetAutocompleteV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionchecklistGetAutocompleteV3Response from a JSON string
inscriptionchecklist_get_autocomplete_v3_response_instance = InscriptionchecklistGetAutocompleteV3Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionchecklistGetAutocompleteV3Response.to_json())

# convert the object into a dict
inscriptionchecklist_get_autocomplete_v3_response_dict = inscriptionchecklist_get_autocomplete_v3_response_instance.to_dict()
# create an instance of InscriptionchecklistGetAutocompleteV3Response from a dict
inscriptionchecklist_get_autocomplete_v3_response_from_dict = InscriptionchecklistGetAutocompleteV3Response.from_dict(inscriptionchecklist_get_autocomplete_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


