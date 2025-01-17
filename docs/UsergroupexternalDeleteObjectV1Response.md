# UsergroupexternalDeleteObjectV1Response

Response for DELETE /1/object/usergroupexternal/{pkiUsergroupexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.usergroupexternal_delete_object_v1_response import UsergroupexternalDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalDeleteObjectV1Response from a JSON string
usergroupexternal_delete_object_v1_response_instance = UsergroupexternalDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalDeleteObjectV1Response.to_json())

# convert the object into a dict
usergroupexternal_delete_object_v1_response_dict = usergroupexternal_delete_object_v1_response_instance.to_dict()
# create an instance of UsergroupexternalDeleteObjectV1Response from a dict
usergroupexternal_delete_object_v1_response_from_dict = UsergroupexternalDeleteObjectV1Response.from_dict(usergroupexternal_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


