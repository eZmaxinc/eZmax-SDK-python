# CommunicationGetObjectV2ResponseMPayload

Payload for GET /2/object/communication/{pkiCommunicationID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_communication** | [**CommunicationResponseCompound**](CommunicationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.communication_get_object_v2_response_m_payload import CommunicationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationGetObjectV2ResponseMPayload from a JSON string
communication_get_object_v2_response_m_payload_instance = CommunicationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print CommunicationGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
communication_get_object_v2_response_m_payload_dict = communication_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of CommunicationGetObjectV2ResponseMPayload from a dict
communication_get_object_v2_response_m_payload_form_dict = communication_get_object_v2_response_m_payload.from_dict(communication_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


