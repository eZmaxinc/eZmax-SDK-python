# AuthenticationexternalResetAuthorizationV1Response

Response for POST /1/object/authenticationexternal/{pkiAuthenticationexternalID}/resetAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.authenticationexternal_reset_authorization_v1_response import AuthenticationexternalResetAuthorizationV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalResetAuthorizationV1Response from a JSON string
authenticationexternal_reset_authorization_v1_response_instance = AuthenticationexternalResetAuthorizationV1Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalResetAuthorizationV1Response.to_json())

# convert the object into a dict
authenticationexternal_reset_authorization_v1_response_dict = authenticationexternal_reset_authorization_v1_response_instance.to_dict()
# create an instance of AuthenticationexternalResetAuthorizationV1Response from a dict
authenticationexternal_reset_authorization_v1_response_from_dict = AuthenticationexternalResetAuthorizationV1Response.from_dict(authenticationexternal_reset_authorization_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


