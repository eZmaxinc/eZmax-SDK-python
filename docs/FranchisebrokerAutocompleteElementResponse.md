# FranchisebrokerAutocompleteElementResponse

A Franchisebroker AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_franchisebroker_name** | **str** | The name of the Franchisebroker in the language of the requester | 
**pki_franchisebroker_id** | **int** | The unique ID of the Franchisebroker | 
**b_franchisebroker_isactive** | **bool** | Whether the Franchisebroker is active or not | 

## Example

```python
from eZmaxApi.models.franchisebroker_autocomplete_element_response import FranchisebrokerAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisebrokerAutocompleteElementResponse from a JSON string
franchisebroker_autocomplete_element_response_instance = FranchisebrokerAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print FranchisebrokerAutocompleteElementResponse.to_json()

# convert the object into a dict
franchisebroker_autocomplete_element_response_dict = franchisebroker_autocomplete_element_response_instance.to_dict()
# create an instance of FranchisebrokerAutocompleteElementResponse from a dict
franchisebroker_autocomplete_element_response_form_dict = franchisebroker_autocomplete_element_response.from_dict(franchisebroker_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


