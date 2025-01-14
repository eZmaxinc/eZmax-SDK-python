# GlaccountAutocompleteElementResponse

A Glaccount AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_glaccount_id** | **int** | The unique ID of the Glaccount | 
**i_glaccount_code** | **int** | The Code of the Glaccount | 
**s_glaccount_description_x** | **str** | The Description for the Glaccount in the language of the requester | 
**b_glaccount_isactive** | **bool** | Whether the Glaccount is active or not | 

## Example

```python
from eZmaxApi.models.glaccount_autocomplete_element_response import GlaccountAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountAutocompleteElementResponse from a JSON string
glaccount_autocomplete_element_response_instance = GlaccountAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(GlaccountAutocompleteElementResponse.to_json())

# convert the object into a dict
glaccount_autocomplete_element_response_dict = glaccount_autocomplete_element_response_instance.to_dict()
# create an instance of GlaccountAutocompleteElementResponse from a dict
glaccount_autocomplete_element_response_from_dict = GlaccountAutocompleteElementResponse.from_dict(glaccount_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


