# FontAutocompleteElementResponse

A Font AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_font_name** | **str** | The name of the Font | 
**pki_font_id** | **int** | The unique ID of the Font | 
**b_font_isactive** | **bool** | Whether the Font is active or not | 

## Example

```python
from eZmaxApi.models.font_autocomplete_element_response import FontAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FontAutocompleteElementResponse from a JSON string
font_autocomplete_element_response_instance = FontAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(FontAutocompleteElementResponse.to_json())

# convert the object into a dict
font_autocomplete_element_response_dict = font_autocomplete_element_response_instance.to_dict()
# create an instance of FontAutocompleteElementResponse from a dict
font_autocomplete_element_response_from_dict = FontAutocompleteElementResponse.from_dict(font_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


