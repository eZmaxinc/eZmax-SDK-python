# UsergroupEditUsergroupmembershipsV1Response

Response for PUT /1/object/usergroup/{pkiUsergroupID}/editUsergroupmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupEditUsergroupmembershipsV1ResponseMPayload**](UsergroupEditUsergroupmembershipsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_response import UsergroupEditUsergroupmembershipsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupmembershipsV1Response from a JSON string
usergroup_edit_usergroupmemberships_v1_response_instance = UsergroupEditUsergroupmembershipsV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupEditUsergroupmembershipsV1Response.to_json())

# convert the object into a dict
usergroup_edit_usergroupmemberships_v1_response_dict = usergroup_edit_usergroupmemberships_v1_response_instance.to_dict()
# create an instance of UsergroupEditUsergroupmembershipsV1Response from a dict
usergroup_edit_usergroupmemberships_v1_response_form_dict = usergroup_edit_usergroupmemberships_v1_response.from_dict(usergroup_edit_usergroupmemberships_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


