# UserGetUsergroupsV1ResponseMPayload

Response for GET /1/object/user/{pkiUserID}/getUsergroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroup** | [**List[UsergroupResponseCompound]**](UsergroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_usergroups_v1_response_m_payload import UserGetUsergroupsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetUsergroupsV1ResponseMPayload from a JSON string
user_get_usergroups_v1_response_m_payload_instance = UserGetUsergroupsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetUsergroupsV1ResponseMPayload.to_json())

# convert the object into a dict
user_get_usergroups_v1_response_m_payload_dict = user_get_usergroups_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetUsergroupsV1ResponseMPayload from a dict
user_get_usergroups_v1_response_m_payload_form_dict = user_get_usergroups_v1_response_m_payload.from_dict(user_get_usergroups_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


