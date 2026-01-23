# SystemconfigurationtypeAutocompleteElementResponse

A Systemconfigurationtype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | 
**s_systemconfigurationtype_description_x** | **str** | The description of the Systemconfigurationtype in the language of the requester | 
**b_systemconfigurationtype_isactive** | **bool** | Whether Systemconfigurationtype is active or not | 

## Example

```python
from eZmaxApi.models.systemconfigurationtype_autocomplete_element_response import SystemconfigurationtypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationtypeAutocompleteElementResponse from a JSON string
systemconfigurationtype_autocomplete_element_response_instance = SystemconfigurationtypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationtypeAutocompleteElementResponse.to_json())

# convert the object into a dict
systemconfigurationtype_autocomplete_element_response_dict = systemconfigurationtype_autocomplete_element_response_instance.to_dict()
# create an instance of SystemconfigurationtypeAutocompleteElementResponse from a dict
systemconfigurationtype_autocomplete_element_response_from_dict = SystemconfigurationtypeAutocompleteElementResponse.from_dict(systemconfigurationtype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


