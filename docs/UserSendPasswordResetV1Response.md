# UserSendPasswordResetV1Response

Response for POST /1/object/user/{pkiUserID}/sendPasswordReset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.user_send_password_reset_v1_response import UserSendPasswordResetV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserSendPasswordResetV1Response from a JSON string
user_send_password_reset_v1_response_instance = UserSendPasswordResetV1Response.from_json(json)
# print the JSON string representation of the object
print UserSendPasswordResetV1Response.to_json()

# convert the object into a dict
user_send_password_reset_v1_response_dict = user_send_password_reset_v1_response_instance.to_dict()
# create an instance of UserSendPasswordResetV1Response from a dict
user_send_password_reset_v1_response_form_dict = user_send_password_reset_v1_response.from_dict(user_send_password_reset_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


