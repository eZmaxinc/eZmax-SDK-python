# VariableexpenseAutocompleteElementResponse

A Variableexpense AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_variableexpense_description_x** | **str** | The description of the Variableexpense in the language of the requester | 
**pki_variableexpense_id** | **int** | The unique ID of the Variableexpense | 
**b_variableexpense_isactive** | **bool** | Whether the variableexpense is active or not | 

## Example

```python
from eZmaxApi.models.variableexpense_autocomplete_element_response import VariableexpenseAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseAutocompleteElementResponse from a JSON string
variableexpense_autocomplete_element_response_instance = VariableexpenseAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print VariableexpenseAutocompleteElementResponse.to_json()

# convert the object into a dict
variableexpense_autocomplete_element_response_dict = variableexpense_autocomplete_element_response_instance.to_dict()
# create an instance of VariableexpenseAutocompleteElementResponse from a dict
variableexpense_autocomplete_element_response_form_dict = variableexpense_autocomplete_element_response.from_dict(variableexpense_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


