# DepartmentAutocompleteElementResponse

A Department AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | 
**pki_department_id** | **int** | The unique ID of the Department | 
**b_department_isactive** | **bool** | Whether the Department is active or not | 

## Example

```python
from eZmaxApi.models.department_autocomplete_element_response import DepartmentAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAutocompleteElementResponse from a JSON string
department_autocomplete_element_response_instance = DepartmentAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(DepartmentAutocompleteElementResponse.to_json())

# convert the object into a dict
department_autocomplete_element_response_dict = department_autocomplete_element_response_instance.to_dict()
# create an instance of DepartmentAutocompleteElementResponse from a dict
department_autocomplete_element_response_from_dict = DepartmentAutocompleteElementResponse.from_dict(department_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


