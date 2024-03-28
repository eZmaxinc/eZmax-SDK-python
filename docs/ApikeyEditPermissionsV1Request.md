# ApikeyEditPermissionsV1Request

Request for PUT /1/object/apikey/{pkiApikeyID}/editPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_permission** | [**List[PermissionRequestCompound]**](PermissionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_edit_permissions_v1_request import ApikeyEditPermissionsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyEditPermissionsV1Request from a JSON string
apikey_edit_permissions_v1_request_instance = ApikeyEditPermissionsV1Request.from_json(json)
# print the JSON string representation of the object
print(ApikeyEditPermissionsV1Request.to_json())

# convert the object into a dict
apikey_edit_permissions_v1_request_dict = apikey_edit_permissions_v1_request_instance.to_dict()
# create an instance of ApikeyEditPermissionsV1Request from a dict
apikey_edit_permissions_v1_request_form_dict = apikey_edit_permissions_v1_request.from_dict(apikey_edit_permissions_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


