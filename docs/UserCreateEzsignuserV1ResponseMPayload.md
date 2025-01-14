# UserCreateEzsignuserV1ResponseMPayload

Payload for POST /1/module/user/createEzsignuser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_s_email_address_success** | **List[str]** | An array of email addresses that succeeded. | 
**a_s_email_address_failure** | **List[str]** | An array of email addresses that failed. | 

## Example

```python
from eZmaxApi.models.user_create_ezsignuser_v1_response_m_payload import UserCreateEzsignuserV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateEzsignuserV1ResponseMPayload from a JSON string
user_create_ezsignuser_v1_response_m_payload_instance = UserCreateEzsignuserV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserCreateEzsignuserV1ResponseMPayload.to_json())

# convert the object into a dict
user_create_ezsignuser_v1_response_m_payload_dict = user_create_ezsignuser_v1_response_m_payload_instance.to_dict()
# create an instance of UserCreateEzsignuserV1ResponseMPayload from a dict
user_create_ezsignuser_v1_response_m_payload_from_dict = UserCreateEzsignuserV1ResponseMPayload.from_dict(user_create_ezsignuser_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


