# UserstagedCreateUserV1Response

Response for POST /1/object/userstaged/{pkiUserstagedID}/createUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserstagedCreateUserV1ResponseMPayload**](UserstagedCreateUserV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.userstaged_create_user_v1_response import UserstagedCreateUserV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedCreateUserV1Response from a JSON string
userstaged_create_user_v1_response_instance = UserstagedCreateUserV1Response.from_json(json)
# print the JSON string representation of the object
print(UserstagedCreateUserV1Response.to_json())

# convert the object into a dict
userstaged_create_user_v1_response_dict = userstaged_create_user_v1_response_instance.to_dict()
# create an instance of UserstagedCreateUserV1Response from a dict
userstaged_create_user_v1_response_from_dict = UserstagedCreateUserV1Response.from_dict(userstaged_create_user_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


