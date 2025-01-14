# UserEditColleaguesV2ResponseMPayload

Payload for PUT /2/object/user/{pkiUserID}/editColleagues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_colleague_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.user_edit_colleagues_v2_response_m_payload import UserEditColleaguesV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditColleaguesV2ResponseMPayload from a JSON string
user_edit_colleagues_v2_response_m_payload_instance = UserEditColleaguesV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserEditColleaguesV2ResponseMPayload.to_json())

# convert the object into a dict
user_edit_colleagues_v2_response_m_payload_dict = user_edit_colleagues_v2_response_m_payload_instance.to_dict()
# create an instance of UserEditColleaguesV2ResponseMPayload from a dict
user_edit_colleagues_v2_response_m_payload_from_dict = UserEditColleaguesV2ResponseMPayload.from_dict(user_edit_colleagues_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


