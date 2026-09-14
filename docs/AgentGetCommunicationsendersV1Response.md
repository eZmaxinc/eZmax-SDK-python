# AgentGetCommunicationsendersV1Response

Response for GET /1/object/agent/{pkiAgentID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentGetCommunicationsendersV1ResponseMPayload**](AgentGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_communicationsenders_v1_response import AgentGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetCommunicationsendersV1Response from a JSON string
agent_get_communicationsenders_v1_response_instance = AgentGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(AgentGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
agent_get_communicationsenders_v1_response_dict = agent_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of AgentGetCommunicationsendersV1Response from a dict
agent_get_communicationsenders_v1_response_from_dict = AgentGetCommunicationsendersV1Response.from_dict(agent_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


