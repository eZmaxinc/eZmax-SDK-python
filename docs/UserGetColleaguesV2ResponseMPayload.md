# UserGetColleaguesV2ResponseMPayload

Response for GET /2/object/user/{pkiUserID}/getColleagues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_colleague** | [**List[ColleagueResponseCompoundV2]**](ColleagueResponseCompoundV2.md) |  | 
**a_obj_colleague_clonable** | [**List[ColleagueResponseCompoundV2]**](ColleagueResponseCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_colleagues_v2_response_m_payload import UserGetColleaguesV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetColleaguesV2ResponseMPayload from a JSON string
user_get_colleagues_v2_response_m_payload_instance = UserGetColleaguesV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetColleaguesV2ResponseMPayload.to_json())

# convert the object into a dict
user_get_colleagues_v2_response_m_payload_dict = user_get_colleagues_v2_response_m_payload_instance.to_dict()
# create an instance of UserGetColleaguesV2ResponseMPayload from a dict
user_get_colleagues_v2_response_m_payload_from_dict = UserGetColleaguesV2ResponseMPayload.from_dict(user_get_colleagues_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


