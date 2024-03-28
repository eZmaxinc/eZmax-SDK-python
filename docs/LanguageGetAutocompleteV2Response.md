# LanguageGetAutocompleteV2Response

Response for GET /2/object/language/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LanguageGetAutocompleteV2ResponseMPayload**](LanguageGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.language_get_autocomplete_v2_response import LanguageGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageGetAutocompleteV2Response from a JSON string
language_get_autocomplete_v2_response_instance = LanguageGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(LanguageGetAutocompleteV2Response.to_json())

# convert the object into a dict
language_get_autocomplete_v2_response_dict = language_get_autocomplete_v2_response_instance.to_dict()
# create an instance of LanguageGetAutocompleteV2Response from a dict
language_get_autocomplete_v2_response_form_dict = language_get_autocomplete_v2_response.from_dict(language_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


