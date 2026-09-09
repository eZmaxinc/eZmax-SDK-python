# AgentGetAttachmentsV1Response

Response for GET /1/object/agent/{pkiAgentID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentGetAttachmentsV1ResponseMPayload**](AgentGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_attachments_v1_response import AgentGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetAttachmentsV1Response from a JSON string
agent_get_attachments_v1_response_instance = AgentGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(AgentGetAttachmentsV1Response.to_json())

# convert the object into a dict
agent_get_attachments_v1_response_dict = agent_get_attachments_v1_response_instance.to_dict()
# create an instance of AgentGetAttachmentsV1Response from a dict
agent_get_attachments_v1_response_from_dict = AgentGetAttachmentsV1Response.from_dict(agent_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


