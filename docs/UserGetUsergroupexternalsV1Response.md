# UserGetUsergroupexternalsV1Response

Response for GET /1/object/user/{pkiUserID}/getUsergroupexternals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UserGetUsergroupexternalsV1ResponseMPayload**](UserGetUsergroupexternalsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_usergroupexternals_v1_response import UserGetUsergroupexternalsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetUsergroupexternalsV1Response from a JSON string
user_get_usergroupexternals_v1_response_instance = UserGetUsergroupexternalsV1Response.from_json(json)
# print the JSON string representation of the object
print(UserGetUsergroupexternalsV1Response.to_json())

# convert the object into a dict
user_get_usergroupexternals_v1_response_dict = user_get_usergroupexternals_v1_response_instance.to_dict()
# create an instance of UserGetUsergroupexternalsV1Response from a dict
user_get_usergroupexternals_v1_response_from_dict = UserGetUsergroupexternalsV1Response.from_dict(user_get_usergroupexternals_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


