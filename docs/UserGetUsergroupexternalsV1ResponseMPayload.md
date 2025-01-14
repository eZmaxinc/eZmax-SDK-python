# UserGetUsergroupexternalsV1ResponseMPayload

Response for GET /1/object/user/{pkiUserID}/getUsergroupexternals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupexternal** | [**List[UsergroupexternalResponseCompound]**](UsergroupexternalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_usergroupexternals_v1_response_m_payload import UserGetUsergroupexternalsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetUsergroupexternalsV1ResponseMPayload from a JSON string
user_get_usergroupexternals_v1_response_m_payload_instance = UserGetUsergroupexternalsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetUsergroupexternalsV1ResponseMPayload.to_json())

# convert the object into a dict
user_get_usergroupexternals_v1_response_m_payload_dict = user_get_usergroupexternals_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetUsergroupexternalsV1ResponseMPayload from a dict
user_get_usergroupexternals_v1_response_m_payload_from_dict = UserGetUsergroupexternalsV1ResponseMPayload.from_dict(user_get_usergroupexternals_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


