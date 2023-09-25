# UserEditPermissionsV1Response

Response for PUT /1/object/user/{pkiUserID}/editPermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserEditPermissionsV1ResponseMPayload**](UserEditPermissionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_edit_permissions_v1_response import UserEditPermissionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditPermissionsV1Response from a JSON string
user_edit_permissions_v1_response_instance = UserEditPermissionsV1Response.from_json(json)
# print the JSON string representation of the object
print UserEditPermissionsV1Response.to_json()

# convert the object into a dict
user_edit_permissions_v1_response_dict = user_edit_permissions_v1_response_instance.to_dict()
# create an instance of UserEditPermissionsV1Response from a dict
user_edit_permissions_v1_response_form_dict = user_edit_permissions_v1_response.from_dict(user_edit_permissions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


