# AgentAutocompleteElementResponse

A Agent AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_agent_id** | **int** | The unique ID of the Agent. | 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**b_agent_isactive** | **bool** | Whether the Agent is active or not | 

## Example

```python
from eZmaxApi.models.agent_autocomplete_element_response import AgentAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAutocompleteElementResponse from a JSON string
agent_autocomplete_element_response_instance = AgentAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(AgentAutocompleteElementResponse.to_json())

# convert the object into a dict
agent_autocomplete_element_response_dict = agent_autocomplete_element_response_instance.to_dict()
# create an instance of AgentAutocompleteElementResponse from a dict
agent_autocomplete_element_response_from_dict = AgentAutocompleteElementResponse.from_dict(agent_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


