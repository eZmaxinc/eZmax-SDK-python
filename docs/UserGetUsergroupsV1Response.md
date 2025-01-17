# UserGetUsergroupsV1Response

Response for GET /1/object/user/{pkiUserID}/getUsergroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UserGetUsergroupsV1ResponseMPayload**](UserGetUsergroupsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_usergroups_v1_response import UserGetUsergroupsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetUsergroupsV1Response from a JSON string
user_get_usergroups_v1_response_instance = UserGetUsergroupsV1Response.from_json(json)
# print the JSON string representation of the object
print(UserGetUsergroupsV1Response.to_json())

# convert the object into a dict
user_get_usergroups_v1_response_dict = user_get_usergroups_v1_response_instance.to_dict()
# create an instance of UserGetUsergroupsV1Response from a dict
user_get_usergroups_v1_response_from_dict = UserGetUsergroupsV1Response.from_dict(user_get_usergroups_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


