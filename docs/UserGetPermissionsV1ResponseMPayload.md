# UserGetPermissionsV1ResponseMPayload

Response for GET /1/object/user/{pkiUserID}/getPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_modulegroup** | [**List[ModulegroupResponseCompound]**](ModulegroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_permissions_v1_response_m_payload import UserGetPermissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetPermissionsV1ResponseMPayload from a JSON string
user_get_permissions_v1_response_m_payload_instance = UserGetPermissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetPermissionsV1ResponseMPayload.to_json())

# convert the object into a dict
user_get_permissions_v1_response_m_payload_dict = user_get_permissions_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetPermissionsV1ResponseMPayload from a dict
user_get_permissions_v1_response_m_payload_form_dict = user_get_permissions_v1_response_m_payload.from_dict(user_get_permissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


