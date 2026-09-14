# AgentGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/agent/{pkiAgentID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_communicationrecipients_v1_response_m_payload import AgentGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetCommunicationrecipientsV1ResponseMPayload from a JSON string
agent_get_communicationrecipients_v1_response_m_payload_instance = AgentGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgentGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
agent_get_communicationrecipients_v1_response_m_payload_dict = agent_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of AgentGetCommunicationrecipientsV1ResponseMPayload from a dict
agent_get_communicationrecipients_v1_response_m_payload_from_dict = AgentGetCommunicationrecipientsV1ResponseMPayload.from_dict(agent_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


