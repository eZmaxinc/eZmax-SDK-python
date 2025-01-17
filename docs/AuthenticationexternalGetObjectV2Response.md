# AuthenticationexternalGetObjectV2Response

Response for GET /2/object/authenticationexternal/{pkiAuthenticationexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**AuthenticationexternalGetObjectV2ResponseMPayload**](AuthenticationexternalGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_object_v2_response import AuthenticationexternalGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetObjectV2Response from a JSON string
authenticationexternal_get_object_v2_response_instance = AuthenticationexternalGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetObjectV2Response.to_json())

# convert the object into a dict
authenticationexternal_get_object_v2_response_dict = authenticationexternal_get_object_v2_response_instance.to_dict()
# create an instance of AuthenticationexternalGetObjectV2Response from a dict
authenticationexternal_get_object_v2_response_from_dict = AuthenticationexternalGetObjectV2Response.from_dict(authenticationexternal_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


