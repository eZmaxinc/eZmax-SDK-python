# UserstagedGetObjectV2ResponseMPayload

Payload for GET /2/object/userstaged/{pkiUserstagedID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_userstaged** | [**UserstagedResponse**](UserstagedResponse.md) | A Userstaged Object | 

## Example

```python
from eZmaxApi.models.userstaged_get_object_v2_response_m_payload import UserstagedGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedGetObjectV2ResponseMPayload from a JSON string
userstaged_get_object_v2_response_m_payload_instance = UserstagedGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserstagedGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
userstaged_get_object_v2_response_m_payload_dict = userstaged_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UserstagedGetObjectV2ResponseMPayload from a dict
userstaged_get_object_v2_response_m_payload_from_dict = UserstagedGetObjectV2ResponseMPayload.from_dict(userstaged_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


