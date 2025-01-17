# UsergroupGetUsergroupmembershipsV1Response

Response for GET /1/object/usergroup/{pkiUsergroupID}/getUsergroupmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupGetUsergroupmembershipsV1ResponseMPayload**](UsergroupGetUsergroupmembershipsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_usergroupmemberships_v1_response import UsergroupGetUsergroupmembershipsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetUsergroupmembershipsV1Response from a JSON string
usergroup_get_usergroupmemberships_v1_response_instance = UsergroupGetUsergroupmembershipsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupGetUsergroupmembershipsV1Response.to_json())

# convert the object into a dict
usergroup_get_usergroupmemberships_v1_response_dict = usergroup_get_usergroupmemberships_v1_response_instance.to_dict()
# create an instance of UsergroupGetUsergroupmembershipsV1Response from a dict
usergroup_get_usergroupmemberships_v1_response_from_dict = UsergroupGetUsergroupmembershipsV1Response.from_dict(usergroup_get_usergroupmemberships_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


