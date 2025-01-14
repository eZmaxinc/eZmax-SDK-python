# FranchiseofficeAutocompleteElementResponse

A Franchiseoffice AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_franchiseoffice_description** | **str** | The description of the Franchiseoffice in the language of the requester | 
**pki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | 
**b_franchiseoffice_isactive** | **bool** | Whether the Franchiseoffice is active or not | 

## Example

```python
from eZmaxApi.models.franchiseoffice_autocomplete_element_response import FranchiseofficeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseofficeAutocompleteElementResponse from a JSON string
franchiseoffice_autocomplete_element_response_instance = FranchiseofficeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(FranchiseofficeAutocompleteElementResponse.to_json())

# convert the object into a dict
franchiseoffice_autocomplete_element_response_dict = franchiseoffice_autocomplete_element_response_instance.to_dict()
# create an instance of FranchiseofficeAutocompleteElementResponse from a dict
franchiseoffice_autocomplete_element_response_from_dict = FranchiseofficeAutocompleteElementResponse.from_dict(franchiseoffice_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


