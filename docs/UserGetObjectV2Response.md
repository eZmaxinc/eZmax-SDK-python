# UserGetObjectV2Response

Response for GET /2/object/user/{pkiUserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserGetObjectV2ResponseMPayload**](UserGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_object_v2_response import UserGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetObjectV2Response from a JSON string
user_get_object_v2_response_instance = UserGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(UserGetObjectV2Response.to_json())

# convert the object into a dict
user_get_object_v2_response_dict = user_get_object_v2_response_instance.to_dict()
# create an instance of UserGetObjectV2Response from a dict
user_get_object_v2_response_from_dict = UserGetObjectV2Response.from_dict(user_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


