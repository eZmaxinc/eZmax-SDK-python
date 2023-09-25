# UserGetObjectV2ResponseMPayload

Payload for GET /2/object/user/{pkiUserID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_user** | [**UserResponseCompound**](UserResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_object_v2_response_m_payload import UserGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetObjectV2ResponseMPayload from a JSON string
user_get_object_v2_response_m_payload_instance = UserGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UserGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
user_get_object_v2_response_m_payload_dict = user_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UserGetObjectV2ResponseMPayload from a dict
user_get_object_v2_response_m_payload_form_dict = user_get_object_v2_response_m_payload.from_dict(user_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


