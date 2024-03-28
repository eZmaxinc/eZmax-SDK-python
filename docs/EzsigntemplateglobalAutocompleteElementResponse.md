# EzsigntemplateglobalAutocompleteElementResponse

A Ezsigntemplate AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | 
**s_ezsigntemplateglobal_description** | **str** | The description of the Ezsigntemplate | 
**b_ezsigntemplateglobal_isactive** | **bool** | Whether the Ezsigntemplate is active or not | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_autocomplete_element_response import EzsigntemplateglobalAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalAutocompleteElementResponse from a JSON string
ezsigntemplateglobal_autocomplete_element_response_instance = EzsigntemplateglobalAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalAutocompleteElementResponse.to_json())

# convert the object into a dict
ezsigntemplateglobal_autocomplete_element_response_dict = ezsigntemplateglobal_autocomplete_element_response_instance.to_dict()
# create an instance of EzsigntemplateglobalAutocompleteElementResponse from a dict
ezsigntemplateglobal_autocomplete_element_response_form_dict = ezsigntemplateglobal_autocomplete_element_response.from_dict(ezsigntemplateglobal_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


