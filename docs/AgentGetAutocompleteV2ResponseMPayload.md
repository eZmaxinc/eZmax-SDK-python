# AgentGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/agent/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_agent** | [**List[AgentAutocompleteElementResponse]**](AgentAutocompleteElementResponse.md) | An array of Agent autocomplete element response. | 

## Example

```python
from eZmaxApi.models.agent_get_autocomplete_v2_response_m_payload import AgentGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetAutocompleteV2ResponseMPayload from a JSON string
agent_get_autocomplete_v2_response_m_payload_instance = AgentGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgentGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
agent_get_autocomplete_v2_response_m_payload_dict = agent_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of AgentGetAutocompleteV2ResponseMPayload from a dict
agent_get_autocomplete_v2_response_m_payload_from_dict = AgentGetAutocompleteV2ResponseMPayload.from_dict(agent_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


