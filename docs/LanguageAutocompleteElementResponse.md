# LanguageAutocompleteElementResponse

A Language AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**b_language_isactive** | **bool** | Whether the Language is active or not | 

## Example

```python
from eZmaxApi.models.language_autocomplete_element_response import LanguageAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageAutocompleteElementResponse from a JSON string
language_autocomplete_element_response_instance = LanguageAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(LanguageAutocompleteElementResponse.to_json())

# convert the object into a dict
language_autocomplete_element_response_dict = language_autocomplete_element_response_instance.to_dict()
# create an instance of LanguageAutocompleteElementResponse from a dict
language_autocomplete_element_response_form_dict = language_autocomplete_element_response.from_dict(language_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


