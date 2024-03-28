# UserstagedCreateUserV1ResponseMPayload

Payload for POST /1/object/userstaged/{pkiUserstagedID}/createUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_user_id** | **int** | The unique ID of the User | 

## Example

```python
from eZmaxApi.models.userstaged_create_user_v1_response_m_payload import UserstagedCreateUserV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedCreateUserV1ResponseMPayload from a JSON string
userstaged_create_user_v1_response_m_payload_instance = UserstagedCreateUserV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserstagedCreateUserV1ResponseMPayload.to_json())

# convert the object into a dict
userstaged_create_user_v1_response_m_payload_dict = userstaged_create_user_v1_response_m_payload_instance.to_dict()
# create an instance of UserstagedCreateUserV1ResponseMPayload from a dict
userstaged_create_user_v1_response_m_payload_form_dict = userstaged_create_user_v1_response_m_payload.from_dict(userstaged_create_user_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


