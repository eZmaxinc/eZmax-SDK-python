# AgentGetAttachmentsV1ResponseMPayload

Response for GET /1/object/agent/{pkiAgentID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_attachments_v1_response_m_payload import AgentGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetAttachmentsV1ResponseMPayload from a JSON string
agent_get_attachments_v1_response_m_payload_instance = AgentGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgentGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
agent_get_attachments_v1_response_m_payload_dict = agent_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of AgentGetAttachmentsV1ResponseMPayload from a dict
agent_get_attachments_v1_response_m_payload_from_dict = AgentGetAttachmentsV1ResponseMPayload.from_dict(agent_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


