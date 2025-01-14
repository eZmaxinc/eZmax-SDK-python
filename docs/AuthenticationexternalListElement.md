# AuthenticationexternalListElement

A Authenticationexternal List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_authenticationexternal_id** | **int** | The unique ID of the Authenticationexternal | 
**s_authenticationexternal_description** | **str** | The description of the Authenticationexternal | 
**e_authenticationexternal_type** | [**FieldEAuthenticationexternalType**](FieldEAuthenticationexternalType.md) |  | 
**b_authenticationexternal_connected** | **bool** | Whether the Authenticationexternal has been connected or not | 

## Example

```python
from eZmaxApi.models.authenticationexternal_list_element import AuthenticationexternalListElement

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalListElement from a JSON string
authenticationexternal_list_element_instance = AuthenticationexternalListElement.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalListElement.to_json())

# convert the object into a dict
authenticationexternal_list_element_dict = authenticationexternal_list_element_instance.to_dict()
# create an instance of AuthenticationexternalListElement from a dict
authenticationexternal_list_element_from_dict = AuthenticationexternalListElement.from_dict(authenticationexternal_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


