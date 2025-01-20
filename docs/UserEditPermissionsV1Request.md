# UserEditPermissionsV1Request

Request for PUT /1/object/user/{pkiUserID}/editPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_permission** | [**List[PermissionRequestCompound]**](PermissionRequest.md) |  | 

## Example

```python
from eZmaxApi.models.user_edit_permissions_v1_request import UserEditPermissionsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditPermissionsV1Request from a JSON string
user_edit_permissions_v1_request_instance = UserEditPermissionsV1Request.from_json(json)
# print the JSON string representation of the object
print(UserEditPermissionsV1Request.to_json())

# convert the object into a dict
user_edit_permissions_v1_request_dict = user_edit_permissions_v1_request_instance.to_dict()
# create an instance of UserEditPermissionsV1Request from a dict
user_edit_permissions_v1_request_from_dict = UserEditPermissionsV1Request.from_dict(user_edit_permissions_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


