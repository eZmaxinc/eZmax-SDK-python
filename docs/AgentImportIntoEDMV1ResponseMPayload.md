# AgentImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/agent/{pkiAgentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.agent_import_into_edmv1_response_m_payload import AgentImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgentImportIntoEDMV1ResponseMPayload from a JSON string
agent_import_into_edmv1_response_m_payload_instance = AgentImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgentImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
agent_import_into_edmv1_response_m_payload_dict = agent_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of AgentImportIntoEDMV1ResponseMPayload from a dict
agent_import_into_edmv1_response_m_payload_from_dict = AgentImportIntoEDMV1ResponseMPayload.from_dict(agent_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


