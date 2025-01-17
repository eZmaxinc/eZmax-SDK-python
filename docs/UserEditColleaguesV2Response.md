# UserEditColleaguesV2Response

Response for PUT /2/object/user/{pkiUserID}/editColleagues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserEditColleaguesV2ResponseMPayload**](UserEditColleaguesV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_edit_colleagues_v2_response import UserEditColleaguesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditColleaguesV2Response from a JSON string
user_edit_colleagues_v2_response_instance = UserEditColleaguesV2Response.from_json(json)
# print the JSON string representation of the object
print(UserEditColleaguesV2Response.to_json())

# convert the object into a dict
user_edit_colleagues_v2_response_dict = user_edit_colleagues_v2_response_instance.to_dict()
# create an instance of UserEditColleaguesV2Response from a dict
user_edit_colleagues_v2_response_from_dict = UserEditColleaguesV2Response.from_dict(user_edit_colleagues_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


