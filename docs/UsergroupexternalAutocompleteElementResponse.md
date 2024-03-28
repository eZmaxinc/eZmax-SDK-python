# UsergroupexternalAutocompleteElementResponse

A Usergroupexternal AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**b_usergroupexternal_isactive** | **bool** | Whether the Usergroupexternal is active or not | 

## Example

```python
from eZmaxApi.models.usergroupexternal_autocomplete_element_response import UsergroupexternalAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalAutocompleteElementResponse from a JSON string
usergroupexternal_autocomplete_element_response_instance = UsergroupexternalAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalAutocompleteElementResponse.to_json())

# convert the object into a dict
usergroupexternal_autocomplete_element_response_dict = usergroupexternal_autocomplete_element_response_instance.to_dict()
# create an instance of UsergroupexternalAutocompleteElementResponse from a dict
usergroupexternal_autocomplete_element_response_form_dict = usergroupexternal_autocomplete_element_response.from_dict(usergroupexternal_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


