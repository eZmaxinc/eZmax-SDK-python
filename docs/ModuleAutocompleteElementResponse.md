# ModuleAutocompleteElementResponse

A Module AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_module_id** | **int** | The unique ID of the Module | 
**s_module_name_x** | **str** | The Name of the Module in the language of the requester | 
**b_module_isactive** | **bool** | Whether the Module is active or not | 

## Example

```python
from eZmaxApi.models.module_autocomplete_element_response import ModuleAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleAutocompleteElementResponse from a JSON string
module_autocomplete_element_response_instance = ModuleAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(ModuleAutocompleteElementResponse.to_json())

# convert the object into a dict
module_autocomplete_element_response_dict = module_autocomplete_element_response_instance.to_dict()
# create an instance of ModuleAutocompleteElementResponse from a dict
module_autocomplete_element_response_form_dict = module_autocomplete_element_response.from_dict(module_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


