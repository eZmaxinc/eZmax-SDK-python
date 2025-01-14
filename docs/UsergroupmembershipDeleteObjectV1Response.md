# UsergroupmembershipDeleteObjectV1Response

Response for DELETE /1/object/usergroupmembership/{pkiUsergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.usergroupmembership_delete_object_v1_response import UsergroupmembershipDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipDeleteObjectV1Response from a JSON string
usergroupmembership_delete_object_v1_response_instance = UsergroupmembershipDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipDeleteObjectV1Response.to_json())

# convert the object into a dict
usergroupmembership_delete_object_v1_response_dict = usergroupmembership_delete_object_v1_response_instance.to_dict()
# create an instance of UsergroupmembershipDeleteObjectV1Response from a dict
usergroupmembership_delete_object_v1_response_from_dict = UsergroupmembershipDeleteObjectV1Response.from_dict(usergroupmembership_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


