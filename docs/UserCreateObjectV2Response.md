# UserCreateObjectV2Response

Response for POST /1/object/user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserCreateObjectV2ResponseMPayload**](UserCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_create_object_v2_response import UserCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateObjectV2Response from a JSON string
user_create_object_v2_response_instance = UserCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(UserCreateObjectV2Response.to_json())

# convert the object into a dict
user_create_object_v2_response_dict = user_create_object_v2_response_instance.to_dict()
# create an instance of UserCreateObjectV2Response from a dict
user_create_object_v2_response_from_dict = UserCreateObjectV2Response.from_dict(user_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


