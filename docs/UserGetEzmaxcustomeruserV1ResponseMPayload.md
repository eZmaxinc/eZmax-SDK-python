# UserGetEzmaxcustomeruserV1ResponseMPayload

Response for GET /1/object/user/getEzmaxcustomeruser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcustomeruser** | [**CustomEzmaxcustomeruserResponse**](CustomEzmaxcustomeruserResponse.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_ezmaxcustomeruser_v1_response_m_payload import UserGetEzmaxcustomeruserV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetEzmaxcustomeruserV1ResponseMPayload from a JSON string
user_get_ezmaxcustomeruser_v1_response_m_payload_instance = UserGetEzmaxcustomeruserV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetEzmaxcustomeruserV1ResponseMPayload.to_json())

# convert the object into a dict
user_get_ezmaxcustomeruser_v1_response_m_payload_dict = user_get_ezmaxcustomeruser_v1_response_m_payload_instance.to_dict()
# create an instance of UserGetEzmaxcustomeruserV1ResponseMPayload from a dict
user_get_ezmaxcustomeruser_v1_response_m_payload_from_dict = UserGetEzmaxcustomeruserV1ResponseMPayload.from_dict(user_get_ezmaxcustomeruser_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


