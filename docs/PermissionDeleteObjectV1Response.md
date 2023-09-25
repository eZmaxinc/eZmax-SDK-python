# PermissionDeleteObjectV1Response

Response for DELETE /1/object/permission/{pkiPermissionID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.permission_delete_object_v1_response import PermissionDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDeleteObjectV1Response from a JSON string
permission_delete_object_v1_response_instance = PermissionDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print PermissionDeleteObjectV1Response.to_json()

# convert the object into a dict
permission_delete_object_v1_response_dict = permission_delete_object_v1_response_instance.to_dict()
# create an instance of PermissionDeleteObjectV1Response from a dict
permission_delete_object_v1_response_form_dict = permission_delete_object_v1_response.from_dict(permission_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


