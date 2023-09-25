# UsergroupGetPermissionsV1ResponseMPayload

Response for GET /1/object/usergroup/{pkiUsergroupID}/getPermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_modulegroup** | [**List[ModulegroupResponseCompound]**](ModulegroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_permissions_v1_response_m_payload import UsergroupGetPermissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetPermissionsV1ResponseMPayload from a JSON string
usergroup_get_permissions_v1_response_m_payload_instance = UsergroupGetPermissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupGetPermissionsV1ResponseMPayload.to_json()

# convert the object into a dict
usergroup_get_permissions_v1_response_m_payload_dict = usergroup_get_permissions_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupGetPermissionsV1ResponseMPayload from a dict
usergroup_get_permissions_v1_response_m_payload_form_dict = usergroup_get_permissions_v1_response_m_payload.from_dict(usergroup_get_permissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


