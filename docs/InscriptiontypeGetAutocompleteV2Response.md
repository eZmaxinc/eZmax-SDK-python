# InscriptiontypeGetAutocompleteV2Response

Response for GET /2/object/inscriptiontype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontypeGetAutocompleteV2ResponseMPayload**](InscriptiontypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontype_get_autocomplete_v2_response import InscriptiontypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontypeGetAutocompleteV2Response from a JSON string
inscriptiontype_get_autocomplete_v2_response_instance = InscriptiontypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
inscriptiontype_get_autocomplete_v2_response_dict = inscriptiontype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of InscriptiontypeGetAutocompleteV2Response from a dict
inscriptiontype_get_autocomplete_v2_response_from_dict = InscriptiontypeGetAutocompleteV2Response.from_dict(inscriptiontype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


