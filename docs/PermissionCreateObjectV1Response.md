# PermissionCreateObjectV1Response

Response for POST /1/object/permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PermissionCreateObjectV1ResponseMPayload**](PermissionCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.permission_create_object_v1_response import PermissionCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCreateObjectV1Response from a JSON string
permission_create_object_v1_response_instance = PermissionCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(PermissionCreateObjectV1Response.to_json())

# convert the object into a dict
permission_create_object_v1_response_dict = permission_create_object_v1_response_instance.to_dict()
# create an instance of PermissionCreateObjectV1Response from a dict
permission_create_object_v1_response_from_dict = PermissionCreateObjectV1Response.from_dict(permission_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


