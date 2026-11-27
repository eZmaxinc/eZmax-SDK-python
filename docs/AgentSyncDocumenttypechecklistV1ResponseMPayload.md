# AgentSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/agent/{pkiAgentID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.agent_sync_documenttypechecklist_v1_response_m_payload import AgentSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
agent_sync_documenttypechecklist_v1_response_m_payload_instance = AgentSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgentSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
agent_sync_documenttypechecklist_v1_response_m_payload_dict = agent_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of AgentSyncDocumenttypechecklistV1ResponseMPayload from a dict
agent_sync_documenttypechecklist_v1_response_m_payload_from_dict = AgentSyncDocumenttypechecklistV1ResponseMPayload.from_dict(agent_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


