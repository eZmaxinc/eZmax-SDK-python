# AgentGetDocumenttypechecklistV1Response

Response for GET /1/object/agent/{pkiAgentID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentGetDocumenttypechecklistV1ResponseMPayload**](AgentGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_documenttypechecklist_v1_response import AgentGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetDocumenttypechecklistV1Response from a JSON string
agent_get_documenttypechecklist_v1_response_instance = AgentGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(AgentGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
agent_get_documenttypechecklist_v1_response_dict = agent_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of AgentGetDocumenttypechecklistV1Response from a dict
agent_get_documenttypechecklist_v1_response_from_dict = AgentGetDocumenttypechecklistV1Response.from_dict(agent_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


