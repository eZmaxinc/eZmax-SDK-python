# AgentSyncDocumenttypechecklistV1Response

Response for POST /1/object/agent/{pkiAgentID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentSyncDocumenttypechecklistV1ResponseMPayload**](AgentSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_sync_documenttypechecklist_v1_response import AgentSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSyncDocumenttypechecklistV1Response from a JSON string
agent_sync_documenttypechecklist_v1_response_instance = AgentSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(AgentSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
agent_sync_documenttypechecklist_v1_response_dict = agent_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of AgentSyncDocumenttypechecklistV1Response from a dict
agent_sync_documenttypechecklist_v1_response_from_dict = AgentSyncDocumenttypechecklistV1Response.from_dict(agent_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


