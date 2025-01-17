# UsergroupEditPermissionsV1Response

Response for PUT /1/object/usergroup/{pkiUsergroupID}/editPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupEditPermissionsV1ResponseMPayload**](UsergroupEditPermissionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_permissions_v1_response import UsergroupEditPermissionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditPermissionsV1Response from a JSON string
usergroup_edit_permissions_v1_response_instance = UsergroupEditPermissionsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupEditPermissionsV1Response.to_json())

# convert the object into a dict
usergroup_edit_permissions_v1_response_dict = usergroup_edit_permissions_v1_response_instance.to_dict()
# create an instance of UsergroupEditPermissionsV1Response from a dict
usergroup_edit_permissions_v1_response_from_dict = UsergroupEditPermissionsV1Response.from_dict(usergroup_edit_permissions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


