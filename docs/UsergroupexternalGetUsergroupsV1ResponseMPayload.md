# UsergroupexternalGetUsergroupsV1ResponseMPayload

Response for GET /1/object/usergroupexternal/{pkiUsergroupexternalID}/getUsergroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroup** | [**List[UsergroupResponseCompound]**](UsergroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_usergroups_v1_response_m_payload import UsergroupexternalGetUsergroupsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetUsergroupsV1ResponseMPayload from a JSON string
usergroupexternal_get_usergroups_v1_response_m_payload_instance = UsergroupexternalGetUsergroupsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetUsergroupsV1ResponseMPayload.to_json())

# convert the object into a dict
usergroupexternal_get_usergroups_v1_response_m_payload_dict = usergroupexternal_get_usergroups_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupexternalGetUsergroupsV1ResponseMPayload from a dict
usergroupexternal_get_usergroups_v1_response_m_payload_from_dict = UsergroupexternalGetUsergroupsV1ResponseMPayload.from_dict(usergroupexternal_get_usergroups_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


