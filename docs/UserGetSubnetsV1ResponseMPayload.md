# UserGetSubnetsV1ResponseMPayload

Response for GET /1/object/user/{pkiUserID}/getSubnets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_subnet** | [**List[SubnetResponseCompound]**](SubnetResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_subnets_v1_response_m_payload import UserGetSubnetsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetSubnetsV1ResponseMPayload from a JSON string
user_get_subnets_v1_response_m_payload_instance = UserGetSubnetsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UserGetSubnetsV1ResponseMPayload.to_json()

# convert the object into a dict
user_get_subnets_v1_response_m_payload_dict = user_get_subnets_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetSubnetsV1ResponseMPayload from a dict
user_get_subnets_v1_response_m_payload_form_dict = user_get_subnets_v1_response_m_payload.from_dict(user_get_subnets_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


