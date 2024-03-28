# UsergroupexternalGetObjectV2ResponseMPayload

Payload for GET /2/object/usergroupexternal/{pkiUsergroupexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupexternal** | [**UsergroupexternalResponseCompound**](UsergroupexternalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_object_v2_response_m_payload import UsergroupexternalGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetObjectV2ResponseMPayload from a JSON string
usergroupexternal_get_object_v2_response_m_payload_instance = UsergroupexternalGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
usergroupexternal_get_object_v2_response_m_payload_dict = usergroupexternal_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupexternalGetObjectV2ResponseMPayload from a dict
usergroupexternal_get_object_v2_response_m_payload_form_dict = usergroupexternal_get_object_v2_response_m_payload.from_dict(usergroupexternal_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


