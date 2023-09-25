# UsergroupEditUsergroupdelegationsV1ResponseMPayload

Response for PUT /1/object/usergroup/{pkiUsergroupID}/EditUsergroupdelegations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_usergroupdelegation_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupdelegations_v1_response_m_payload import UsergroupEditUsergroupdelegationsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupdelegationsV1ResponseMPayload from a JSON string
usergroup_edit_usergroupdelegations_v1_response_m_payload_instance = UsergroupEditUsergroupdelegationsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupEditUsergroupdelegationsV1ResponseMPayload.to_json()

# convert the object into a dict
usergroup_edit_usergroupdelegations_v1_response_m_payload_dict = usergroup_edit_usergroupdelegations_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupEditUsergroupdelegationsV1ResponseMPayload from a dict
usergroup_edit_usergroupdelegations_v1_response_m_payload_form_dict = usergroup_edit_usergroupdelegations_v1_response_m_payload.from_dict(usergroup_edit_usergroupdelegations_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


