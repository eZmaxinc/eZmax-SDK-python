# AuthenticationexternalGetObjectV2ResponseMPayload

Payload for GET /2/object/authenticationexternal/{pkiAuthenticationexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_authenticationexternal** | [**AuthenticationexternalResponseCompound**](AuthenticationexternalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_object_v2_response_m_payload import AuthenticationexternalGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetObjectV2ResponseMPayload from a JSON string
authenticationexternal_get_object_v2_response_m_payload_instance = AuthenticationexternalGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
authenticationexternal_get_object_v2_response_m_payload_dict = authenticationexternal_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of AuthenticationexternalGetObjectV2ResponseMPayload from a dict
authenticationexternal_get_object_v2_response_m_payload_from_dict = AuthenticationexternalGetObjectV2ResponseMPayload.from_dict(authenticationexternal_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


