# UserImpersonateV1ResponseMPayload

Payload for POST /1/object/user/{pkiUserID}/impersonate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikey** | [**CustomApikey**](CustomApikey.md) |  | 

## Example

```python
from eZmaxApi.models.user_impersonate_v1_response_m_payload import UserImpersonateV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserImpersonateV1ResponseMPayload from a JSON string
user_impersonate_v1_response_m_payload_instance = UserImpersonateV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserImpersonateV1ResponseMPayload.to_json())

# convert the object into a dict
user_impersonate_v1_response_m_payload_dict = user_impersonate_v1_response_m_payload_instance.to_dict()
# create an instance of UserImpersonateV1ResponseMPayload from a dict
user_impersonate_v1_response_m_payload_from_dict = UserImpersonateV1ResponseMPayload.from_dict(user_impersonate_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


