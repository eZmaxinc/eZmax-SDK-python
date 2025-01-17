# UsergroupdelegationEditObjectV1Response

Response for PUT /1/object/usergroupdelegation/{pkiUsergroupdelegationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.usergroupdelegation_edit_object_v1_response import UsergroupdelegationEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationEditObjectV1Response from a JSON string
usergroupdelegation_edit_object_v1_response_instance = UsergroupdelegationEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationEditObjectV1Response.to_json())

# convert the object into a dict
usergroupdelegation_edit_object_v1_response_dict = usergroupdelegation_edit_object_v1_response_instance.to_dict()
# create an instance of UsergroupdelegationEditObjectV1Response from a dict
usergroupdelegation_edit_object_v1_response_from_dict = UsergroupdelegationEditObjectV1Response.from_dict(usergroupdelegation_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


