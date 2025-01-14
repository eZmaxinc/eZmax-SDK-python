# UserCreateEzsignuserV1Response

Response for POST /1/module/user/createEzsignuser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserCreateEzsignuserV1ResponseMPayload**](UserCreateEzsignuserV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_create_ezsignuser_v1_response import UserCreateEzsignuserV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateEzsignuserV1Response from a JSON string
user_create_ezsignuser_v1_response_instance = UserCreateEzsignuserV1Response.from_json(json)
# print the JSON string representation of the object
print(UserCreateEzsignuserV1Response.to_json())

# convert the object into a dict
user_create_ezsignuser_v1_response_dict = user_create_ezsignuser_v1_response_instance.to_dict()
# create an instance of UserCreateEzsignuserV1Response from a dict
user_create_ezsignuser_v1_response_from_dict = UserCreateEzsignuserV1Response.from_dict(user_create_ezsignuser_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


