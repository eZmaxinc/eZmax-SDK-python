# UsergroupEditUsergroupmembershipsV1ResponseMPayload

Response for PUT /1/object/usergroup/{pkiUsergroupID}/editUsergroupmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_usergroupmembership_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_response_m_payload import UsergroupEditUsergroupmembershipsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupmembershipsV1ResponseMPayload from a JSON string
usergroup_edit_usergroupmemberships_v1_response_m_payload_instance = UsergroupEditUsergroupmembershipsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupEditUsergroupmembershipsV1ResponseMPayload.to_json())

# convert the object into a dict
usergroup_edit_usergroupmemberships_v1_response_m_payload_dict = usergroup_edit_usergroupmemberships_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupEditUsergroupmembershipsV1ResponseMPayload from a dict
usergroup_edit_usergroupmemberships_v1_response_m_payload_from_dict = UsergroupEditUsergroupmembershipsV1ResponseMPayload.from_dict(usergroup_edit_usergroupmemberships_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


