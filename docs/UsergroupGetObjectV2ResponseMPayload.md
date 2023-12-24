# UsergroupGetObjectV2ResponseMPayload

Payload for GET /2/object/usergroup/{pkiUsergroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroup** | [**UsergroupResponseCompound**](UsergroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_object_v2_response_m_payload import UsergroupGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetObjectV2ResponseMPayload from a JSON string
usergroup_get_object_v2_response_m_payload_instance = UsergroupGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
usergroup_get_object_v2_response_m_payload_dict = usergroup_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupGetObjectV2ResponseMPayload from a dict
usergroup_get_object_v2_response_m_payload_form_dict = usergroup_get_object_v2_response_m_payload.from_dict(usergroup_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


