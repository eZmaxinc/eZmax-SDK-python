# UsergroupGetUsergroupdelegationsV1ResponseMPayload

Response for GET /1/object/usergroup/{pkiUsergroupID}/getUsergroupdelegations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupdelegation** | [**List[UsergroupdelegationResponseCompound]**](UsergroupdelegationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_usergroupdelegations_v1_response_m_payload import UsergroupGetUsergroupdelegationsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetUsergroupdelegationsV1ResponseMPayload from a JSON string
usergroup_get_usergroupdelegations_v1_response_m_payload_instance = UsergroupGetUsergroupdelegationsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupGetUsergroupdelegationsV1ResponseMPayload.to_json()

# convert the object into a dict
usergroup_get_usergroupdelegations_v1_response_m_payload_dict = usergroup_get_usergroupdelegations_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupGetUsergroupdelegationsV1ResponseMPayload from a dict
usergroup_get_usergroupdelegations_v1_response_m_payload_form_dict = usergroup_get_usergroupdelegations_v1_response_m_payload.from_dict(usergroup_get_usergroupdelegations_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


