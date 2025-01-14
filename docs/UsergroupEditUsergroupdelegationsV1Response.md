# UsergroupEditUsergroupdelegationsV1Response

Response for PUT /1/object/usergroup/{pkiUsergroupID}/editUsergroupdelegations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupEditUsergroupdelegationsV1ResponseMPayload**](UsergroupEditUsergroupdelegationsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupdelegations_v1_response import UsergroupEditUsergroupdelegationsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupdelegationsV1Response from a JSON string
usergroup_edit_usergroupdelegations_v1_response_instance = UsergroupEditUsergroupdelegationsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupEditUsergroupdelegationsV1Response.to_json())

# convert the object into a dict
usergroup_edit_usergroupdelegations_v1_response_dict = usergroup_edit_usergroupdelegations_v1_response_instance.to_dict()
# create an instance of UsergroupEditUsergroupdelegationsV1Response from a dict
usergroup_edit_usergroupdelegations_v1_response_from_dict = UsergroupEditUsergroupdelegationsV1Response.from_dict(usergroup_edit_usergroupdelegations_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


