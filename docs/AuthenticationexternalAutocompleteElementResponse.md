# AuthenticationexternalAutocompleteElementResponse

A Authenticationexternal AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_authenticationexternal_id** | **int** | The unique ID of the Authenticationexternal | 
**s_authenticationexternal_description** | **str** | The description of the Authenticationexternal | 
**b_authenticationexternal_isactive** | **bool** | Whether the Authenticationexternal is active or not | 

## Example

```python
from eZmaxApi.models.authenticationexternal_autocomplete_element_response import AuthenticationexternalAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalAutocompleteElementResponse from a JSON string
authenticationexternal_autocomplete_element_response_instance = AuthenticationexternalAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalAutocompleteElementResponse.to_json())

# convert the object into a dict
authenticationexternal_autocomplete_element_response_dict = authenticationexternal_autocomplete_element_response_instance.to_dict()
# create an instance of AuthenticationexternalAutocompleteElementResponse from a dict
authenticationexternal_autocomplete_element_response_from_dict = AuthenticationexternalAutocompleteElementResponse.from_dict(authenticationexternal_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


