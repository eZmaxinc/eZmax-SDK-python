# DomainAutocompleteElementResponse

A Domain AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_domain_id** | **int** | The unique ID of the Domain | 
**s_domain_name** | **str** | The name of the Domain | 
**b_domain_isactive** | **bool** | Whether the Domain is active or not | 

## Example

```python
from eZmaxApi.models.domain_autocomplete_element_response import DomainAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAutocompleteElementResponse from a JSON string
domain_autocomplete_element_response_instance = DomainAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(DomainAutocompleteElementResponse.to_json())

# convert the object into a dict
domain_autocomplete_element_response_dict = domain_autocomplete_element_response_instance.to_dict()
# create an instance of DomainAutocompleteElementResponse from a dict
domain_autocomplete_element_response_from_dict = DomainAutocompleteElementResponse.from_dict(domain_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


