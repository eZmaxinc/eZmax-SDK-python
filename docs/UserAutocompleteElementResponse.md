# UserAutocompleteElementResponse

A User AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_user_type** | [**FieldEUserType**](FieldEUserType.md) |  | 
**s_user_name** | **str** | The description of the User in the language of the requester | 
**pki_user_id** | **int** | The unique ID of the User | 
**b_user_isactive** | **bool** | Whether the User is active or not | 

## Example

```python
from eZmaxApi.models.user_autocomplete_element_response import UserAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserAutocompleteElementResponse from a JSON string
user_autocomplete_element_response_instance = UserAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(UserAutocompleteElementResponse.to_json())

# convert the object into a dict
user_autocomplete_element_response_dict = user_autocomplete_element_response_instance.to_dict()
# create an instance of UserAutocompleteElementResponse from a dict
user_autocomplete_element_response_from_dict = UserAutocompleteElementResponse.from_dict(user_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


