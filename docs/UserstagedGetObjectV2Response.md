# UserstagedGetObjectV2Response

Response for GET /2/object/userstaged/{pkiUserstagedID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UserstagedGetObjectV2ResponseMPayload**](UserstagedGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.userstaged_get_object_v2_response import UserstagedGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedGetObjectV2Response from a JSON string
userstaged_get_object_v2_response_instance = UserstagedGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(UserstagedGetObjectV2Response.to_json())

# convert the object into a dict
userstaged_get_object_v2_response_dict = userstaged_get_object_v2_response_instance.to_dict()
# create an instance of UserstagedGetObjectV2Response from a dict
userstaged_get_object_v2_response_from_dict = UserstagedGetObjectV2Response.from_dict(userstaged_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


