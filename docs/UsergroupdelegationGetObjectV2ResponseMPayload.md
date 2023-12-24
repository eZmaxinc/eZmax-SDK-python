# UsergroupdelegationGetObjectV2ResponseMPayload

Payload for GET /2/object/usergroupdelegation/{pkiUsergroupdelegationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupdelegation** | [**UsergroupdelegationResponseCompound**](UsergroupdelegationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_get_object_v2_response_m_payload import UsergroupdelegationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationGetObjectV2ResponseMPayload from a JSON string
usergroupdelegation_get_object_v2_response_m_payload_instance = UsergroupdelegationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupdelegationGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
usergroupdelegation_get_object_v2_response_m_payload_dict = usergroupdelegation_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupdelegationGetObjectV2ResponseMPayload from a dict
usergroupdelegation_get_object_v2_response_m_payload_form_dict = usergroupdelegation_get_object_v2_response_m_payload.from_dict(usergroupdelegation_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


