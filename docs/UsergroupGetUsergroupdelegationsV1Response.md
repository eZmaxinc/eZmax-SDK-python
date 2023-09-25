# UsergroupGetUsergroupdelegationsV1Response

Response for GET /1/object/usergroup/{pkiUsergroupID}/getUsergroupdelegations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupGetUsergroupdelegationsV1ResponseMPayload**](UsergroupGetUsergroupdelegationsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_usergroupdelegations_v1_response import UsergroupGetUsergroupdelegationsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetUsergroupdelegationsV1Response from a JSON string
usergroup_get_usergroupdelegations_v1_response_instance = UsergroupGetUsergroupdelegationsV1Response.from_json(json)
# print the JSON string representation of the object
print UsergroupGetUsergroupdelegationsV1Response.to_json()

# convert the object into a dict
usergroup_get_usergroupdelegations_v1_response_dict = usergroup_get_usergroupdelegations_v1_response_instance.to_dict()
# create an instance of UsergroupGetUsergroupdelegationsV1Response from a dict
usergroup_get_usergroupdelegations_v1_response_form_dict = usergroup_get_usergroupdelegations_v1_response.from_dict(usergroup_get_usergroupdelegations_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


