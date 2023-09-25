# UserEditPermissionsV1ResponseMPayload

Payload for PUT /1/object/user/{pkiUserID}/editPermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_permission_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.user_edit_permissions_v1_response_m_payload import UserEditPermissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditPermissionsV1ResponseMPayload from a JSON string
user_edit_permissions_v1_response_m_payload_instance = UserEditPermissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UserEditPermissionsV1ResponseMPayload.to_json()

# convert the object into a dict
user_edit_permissions_v1_response_m_payload_dict = user_edit_permissions_v1_response_m_payload_instance.to_dict()
# create an instance of UserEditPermissionsV1ResponseMPayload from a dict
user_edit_permissions_v1_response_m_payload_form_dict = user_edit_permissions_v1_response_m_payload.from_dict(user_edit_permissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


