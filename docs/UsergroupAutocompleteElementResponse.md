# UsergroupAutocompleteElementResponse

A Usergroup AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | 
**pki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**b_usergroup_isactive** | **bool** | Whether the Usergroup is active or not | 

## Example

```python
from eZmaxApi.models.usergroup_autocomplete_element_response import UsergroupAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupAutocompleteElementResponse from a JSON string
usergroup_autocomplete_element_response_instance = UsergroupAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(UsergroupAutocompleteElementResponse.to_json())

# convert the object into a dict
usergroup_autocomplete_element_response_dict = usergroup_autocomplete_element_response_instance.to_dict()
# create an instance of UsergroupAutocompleteElementResponse from a dict
usergroup_autocomplete_element_response_form_dict = usergroup_autocomplete_element_response.from_dict(usergroup_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


