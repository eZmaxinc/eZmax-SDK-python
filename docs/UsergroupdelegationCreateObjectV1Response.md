# UsergroupdelegationCreateObjectV1Response

Response for POST /1/object/usergroupdelegation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupdelegationCreateObjectV1ResponseMPayload**](UsergroupdelegationCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_create_object_v1_response import UsergroupdelegationCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationCreateObjectV1Response from a JSON string
usergroupdelegation_create_object_v1_response_instance = UsergroupdelegationCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationCreateObjectV1Response.to_json())

# convert the object into a dict
usergroupdelegation_create_object_v1_response_dict = usergroupdelegation_create_object_v1_response_instance.to_dict()
# create an instance of UsergroupdelegationCreateObjectV1Response from a dict
usergroupdelegation_create_object_v1_response_form_dict = usergroupdelegation_create_object_v1_response.from_dict(usergroupdelegation_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


