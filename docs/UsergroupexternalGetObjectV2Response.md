# UsergroupexternalGetObjectV2Response

Response for GET /2/object/usergroupexternal/{pkiUsergroupexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupexternalGetObjectV2ResponseMPayload**](UsergroupexternalGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_object_v2_response import UsergroupexternalGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetObjectV2Response from a JSON string
usergroupexternal_get_object_v2_response_instance = UsergroupexternalGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetObjectV2Response.to_json())

# convert the object into a dict
usergroupexternal_get_object_v2_response_dict = usergroupexternal_get_object_v2_response_instance.to_dict()
# create an instance of UsergroupexternalGetObjectV2Response from a dict
usergroupexternal_get_object_v2_response_from_dict = UsergroupexternalGetObjectV2Response.from_dict(usergroupexternal_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


