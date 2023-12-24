# CustomAutocompleteElementResponse

Generic AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_category** | **str** | The Category for the dropdown or an empty string if not categorized | 
**s_label** | **str** | The Description of the element | 
**s_value** | **str** | The Unique ID of the element | 
**m_value** | **str** | The Unique ID of the element | [optional] 
**b_active** | **bool** | Indicates if the element is active | 

## Example

```python
from eZmaxApi.models.custom_autocomplete_element_response import CustomAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAutocompleteElementResponse from a JSON string
custom_autocomplete_element_response_instance = CustomAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print CustomAutocompleteElementResponse.to_json()

# convert the object into a dict
custom_autocomplete_element_response_dict = custom_autocomplete_element_response_instance.to_dict()
# create an instance of CustomAutocompleteElementResponse from a dict
custom_autocomplete_element_response_form_dict = custom_autocomplete_element_response.from_dict(custom_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


