# UsergroupGetPermissionsV1Response

Response for GET /1/object/usergroup/{pkiUsergroupID}/getPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupGetPermissionsV1ResponseMPayload**](UsergroupGetPermissionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_permissions_v1_response import UsergroupGetPermissionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetPermissionsV1Response from a JSON string
usergroup_get_permissions_v1_response_instance = UsergroupGetPermissionsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupGetPermissionsV1Response.to_json())

# convert the object into a dict
usergroup_get_permissions_v1_response_dict = usergroup_get_permissions_v1_response_instance.to_dict()
# create an instance of UsergroupGetPermissionsV1Response from a dict
usergroup_get_permissions_v1_response_from_dict = UsergroupGetPermissionsV1Response.from_dict(usergroup_get_permissions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


