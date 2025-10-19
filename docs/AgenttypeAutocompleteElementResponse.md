# AgenttypeAutocompleteElementResponse

A Agenttype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_agenttype_id** | **int** | The unique ID of the Agenttype | 
**s_agenttype_name_x** | **str** | The name of the Agenttype in the language of the requester | 
**b_agenttype_isactive** | **bool** | Whether the Agenttype is active or not | 

## Example

```python
from eZmaxApi.models.agenttype_autocomplete_element_response import AgenttypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgenttypeAutocompleteElementResponse from a JSON string
agenttype_autocomplete_element_response_instance = AgenttypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(AgenttypeAutocompleteElementResponse.to_json())

# convert the object into a dict
agenttype_autocomplete_element_response_dict = agenttype_autocomplete_element_response_instance.to_dict()
# create an instance of AgenttypeAutocompleteElementResponse from a dict
agenttype_autocomplete_element_response_from_dict = AgenttypeAutocompleteElementResponse.from_dict(agenttype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


