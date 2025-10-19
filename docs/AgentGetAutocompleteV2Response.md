# AgentGetAutocompleteV2Response

Response for GET /2/object/agent/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgentGetAutocompleteV2ResponseMPayload**](AgentGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agent_get_autocomplete_v2_response import AgentGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetAutocompleteV2Response from a JSON string
agent_get_autocomplete_v2_response_instance = AgentGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(AgentGetAutocompleteV2Response.to_json())

# convert the object into a dict
agent_get_autocomplete_v2_response_dict = agent_get_autocomplete_v2_response_instance.to_dict()
# create an instance of AgentGetAutocompleteV2Response from a dict
agent_get_autocomplete_v2_response_from_dict = AgentGetAutocompleteV2Response.from_dict(agent_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


