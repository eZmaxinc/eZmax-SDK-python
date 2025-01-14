# UsergroupexternalGetUsergroupsV1Response

Response for GET /1/object/usergroupexternal/{pkiUsergroupexternalID}/getUsergroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupexternalGetUsergroupsV1ResponseMPayload**](UsergroupexternalGetUsergroupsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_usergroups_v1_response import UsergroupexternalGetUsergroupsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetUsergroupsV1Response from a JSON string
usergroupexternal_get_usergroups_v1_response_instance = UsergroupexternalGetUsergroupsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetUsergroupsV1Response.to_json())

# convert the object into a dict
usergroupexternal_get_usergroups_v1_response_dict = usergroupexternal_get_usergroups_v1_response_instance.to_dict()
# create an instance of UsergroupexternalGetUsergroupsV1Response from a dict
usergroupexternal_get_usergroups_v1_response_from_dict = UsergroupexternalGetUsergroupsV1Response.from_dict(usergroupexternal_get_usergroups_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


