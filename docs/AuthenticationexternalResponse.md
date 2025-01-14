# AuthenticationexternalResponse

A Authenticationexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_authenticationexternal_id** | **int** | The unique ID of the Authenticationexternal | 
**s_authenticationexternal_description** | **str** | The description of the Authenticationexternal | 
**e_authenticationexternal_type** | [**FieldEAuthenticationexternalType**](FieldEAuthenticationexternalType.md) |  | 
**b_authenticationexternal_connected** | **bool** | Whether the Authenticationexternal has been connected or not | [optional] 
**s_authenticationexternal_authorizationurl** | **str** | The url to authorize the Authenticationexternal | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_response import AuthenticationexternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalResponse from a JSON string
authenticationexternal_response_instance = AuthenticationexternalResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalResponse.to_json())

# convert the object into a dict
authenticationexternal_response_dict = authenticationexternal_response_instance.to_dict()
# create an instance of AuthenticationexternalResponse from a dict
authenticationexternal_response_from_dict = AuthenticationexternalResponse.from_dict(authenticationexternal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


