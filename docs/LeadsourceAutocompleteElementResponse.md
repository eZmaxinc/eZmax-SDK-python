# LeadsourceAutocompleteElementResponse

A Leadsource AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_leadsource_id** | **int** | The unique ID of the Leadsource | 
**s_leadsource_name_x** | **str** | The name of the Leadsource in the language of the requester | 
**b_leadsource_isactive** | **bool** | Whether the Leadsource is active or not | 

## Example

```python
from eZmaxApi.models.leadsource_autocomplete_element_response import LeadsourceAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeadsourceAutocompleteElementResponse from a JSON string
leadsource_autocomplete_element_response_instance = LeadsourceAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(LeadsourceAutocompleteElementResponse.to_json())

# convert the object into a dict
leadsource_autocomplete_element_response_dict = leadsource_autocomplete_element_response_instance.to_dict()
# create an instance of LeadsourceAutocompleteElementResponse from a dict
leadsource_autocomplete_element_response_from_dict = LeadsourceAutocompleteElementResponse.from_dict(leadsource_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


