# InscriptionchecklistGetAutocompleteV2Response

Response for GET /2/object/inscriptionchecklist/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionchecklistGetAutocompleteV2ResponseMPayload**](InscriptionchecklistGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionchecklist_get_autocomplete_v2_response import InscriptionchecklistGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionchecklistGetAutocompleteV2Response from a JSON string
inscriptionchecklist_get_autocomplete_v2_response_instance = InscriptionchecklistGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionchecklistGetAutocompleteV2Response.to_json())

# convert the object into a dict
inscriptionchecklist_get_autocomplete_v2_response_dict = inscriptionchecklist_get_autocomplete_v2_response_instance.to_dict()
# create an instance of InscriptionchecklistGetAutocompleteV2Response from a dict
inscriptionchecklist_get_autocomplete_v2_response_from_dict = InscriptionchecklistGetAutocompleteV2Response.from_dict(inscriptionchecklist_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


