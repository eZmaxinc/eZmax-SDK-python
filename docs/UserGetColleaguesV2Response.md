# UserGetColleaguesV2Response

Response for GET /2/object/user/{pkiUserID}/getColleagues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserGetColleaguesV2ResponseMPayload**](UserGetColleaguesV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_colleagues_v2_response import UserGetColleaguesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetColleaguesV2Response from a JSON string
user_get_colleagues_v2_response_instance = UserGetColleaguesV2Response.from_json(json)
# print the JSON string representation of the object
print(UserGetColleaguesV2Response.to_json())

# convert the object into a dict
user_get_colleagues_v2_response_dict = user_get_colleagues_v2_response_instance.to_dict()
# create an instance of UserGetColleaguesV2Response from a dict
user_get_colleagues_v2_response_from_dict = UserGetColleaguesV2Response.from_dict(user_get_colleagues_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


