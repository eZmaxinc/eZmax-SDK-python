# LanguageGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/language/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_language** | [**List[LanguageAutocompleteElementResponse]**](LanguageAutocompleteElementResponse.md) | An array of Language autocomplete element response. | 

## Example

```python
from eZmaxApi.models.language_get_autocomplete_v2_response_m_payload import LanguageGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageGetAutocompleteV2ResponseMPayload from a JSON string
language_get_autocomplete_v2_response_m_payload_instance = LanguageGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(LanguageGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
language_get_autocomplete_v2_response_m_payload_dict = language_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of LanguageGetAutocompleteV2ResponseMPayload from a dict
language_get_autocomplete_v2_response_m_payload_from_dict = LanguageGetAutocompleteV2ResponseMPayload.from_dict(language_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


