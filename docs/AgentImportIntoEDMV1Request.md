# AgentImportIntoEDMV1Request

Request for POST /1/object/agent/{pkiAgentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.agent_import_into_edmv1_request import AgentImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AgentImportIntoEDMV1Request from a JSON string
agent_import_into_edmv1_request_instance = AgentImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(AgentImportIntoEDMV1Request.to_json())

# convert the object into a dict
agent_import_into_edmv1_request_dict = agent_import_into_edmv1_request_instance.to_dict()
# create an instance of AgentImportIntoEDMV1Request from a dict
agent_import_into_edmv1_request_from_dict = AgentImportIntoEDMV1Request.from_dict(agent_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


