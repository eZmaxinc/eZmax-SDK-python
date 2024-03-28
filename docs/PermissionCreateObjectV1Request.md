# PermissionCreateObjectV1Request

Request for POST /1/object/permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_permission** | [**List[PermissionRequestCompound]**](PermissionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.permission_create_object_v1_request import PermissionCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCreateObjectV1Request from a JSON string
permission_create_object_v1_request_instance = PermissionCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(PermissionCreateObjectV1Request.to_json())

# convert the object into a dict
permission_create_object_v1_request_dict = permission_create_object_v1_request_instance.to_dict()
# create an instance of PermissionCreateObjectV1Request from a dict
permission_create_object_v1_request_form_dict = permission_create_object_v1_request.from_dict(permission_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


