# CompanyAutocompleteElementResponse

A Company AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_company_id** | **int** | The unique ID of the Company | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | 
**b_company_isactive** | **bool** | Whether the Company is active or not | 

## Example

```python
from eZmaxApi.models.company_autocomplete_element_response import CompanyAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyAutocompleteElementResponse from a JSON string
company_autocomplete_element_response_instance = CompanyAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyAutocompleteElementResponse.to_json())

# convert the object into a dict
company_autocomplete_element_response_dict = company_autocomplete_element_response_instance.to_dict()
# create an instance of CompanyAutocompleteElementResponse from a dict
company_autocomplete_element_response_from_dict = CompanyAutocompleteElementResponse.from_dict(company_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


