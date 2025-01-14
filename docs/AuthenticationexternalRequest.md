# AuthenticationexternalRequest

A Authenticationexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_authenticationexternal_id** | **int** | The unique ID of the Authenticationexternal | [optional] 
**s_authenticationexternal_description** | **str** | The description of the Authenticationexternal | 
**e_authenticationexternal_type** | [**FieldEAuthenticationexternalType**](FieldEAuthenticationexternalType.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_request import AuthenticationexternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalRequest from a JSON string
authenticationexternal_request_instance = AuthenticationexternalRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalRequest.to_json())

# convert the object into a dict
authenticationexternal_request_dict = authenticationexternal_request_instance.to_dict()
# create an instance of AuthenticationexternalRequest from a dict
authenticationexternal_request_from_dict = AuthenticationexternalRequest.from_dict(authenticationexternal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


