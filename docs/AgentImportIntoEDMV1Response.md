# AgentImportIntoEDMV1Response

Response for POST /1/object/agent/{pkiAgentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentImportIntoEDMV1ResponseMPayload**](AgentImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_import_into_edmv1_response import AgentImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentImportIntoEDMV1Response from a JSON string
agent_import_into_edmv1_response_instance = AgentImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(AgentImportIntoEDMV1Response.to_json())

# convert the object into a dict
agent_import_into_edmv1_response_dict = agent_import_into_edmv1_response_instance.to_dict()
# create an instance of AgentImportIntoEDMV1Response from a dict
agent_import_into_edmv1_response_from_dict = AgentImportIntoEDMV1Response.from_dict(agent_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


