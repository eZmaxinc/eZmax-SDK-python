# PermissionGetObjectV2ResponseMPayload

Payload for GET /2/object/permission/{pkiPermissionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_permission** | [**PermissionResponse**](PermissionResponse.md) | A Permission Object and children to create a complete structure | 

## Example

```python
from eZmaxApi.models.permission_get_object_v2_response_m_payload import PermissionGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionGetObjectV2ResponseMPayload from a JSON string
permission_get_object_v2_response_m_payload_instance = PermissionGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PermissionGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
permission_get_object_v2_response_m_payload_dict = permission_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of PermissionGetObjectV2ResponseMPayload from a dict
permission_get_object_v2_response_m_payload_from_dict = PermissionGetObjectV2ResponseMPayload.from_dict(permission_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


