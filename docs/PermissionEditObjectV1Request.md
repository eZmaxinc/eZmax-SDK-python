# PermissionEditObjectV1Request

Request for PUT /1/object/permission/{pkiPermissionID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_permission** | [**PermissionRequestCompound**](PermissionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.permission_edit_object_v1_request import PermissionEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionEditObjectV1Request from a JSON string
permission_edit_object_v1_request_instance = PermissionEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print PermissionEditObjectV1Request.to_json()

# convert the object into a dict
permission_edit_object_v1_request_dict = permission_edit_object_v1_request_instance.to_dict()
# create an instance of PermissionEditObjectV1Request from a dict
permission_edit_object_v1_request_form_dict = permission_edit_object_v1_request.from_dict(permission_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


