# UserGetApikeysV1ResponseMPayload

Response for GET /1/object/user/{pkiUserID}/getApikeys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_apikey** | [**List[ApikeyResponseCompound]**](ApikeyResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_apikeys_v1_response_m_payload import UserGetApikeysV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetApikeysV1ResponseMPayload from a JSON string
user_get_apikeys_v1_response_m_payload_instance = UserGetApikeysV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetApikeysV1ResponseMPayload.to_json())

# convert the object into a dict
user_get_apikeys_v1_response_m_payload_dict = user_get_apikeys_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetApikeysV1ResponseMPayload from a dict
user_get_apikeys_v1_response_m_payload_from_dict = UserGetApikeysV1ResponseMPayload.from_dict(user_get_apikeys_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


