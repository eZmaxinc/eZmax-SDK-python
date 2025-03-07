# CustomerAutocompleteElementResponse

A Customer AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_customer_id** | **int** | The unique ID of the Customer. | 
**s_customer_name** | **str** | The name of the Customer | 
**b_customer_isactive** | **bool** | Whether the customer is active or not | 

## Example

```python
from eZmaxApi.models.customer_autocomplete_element_response import CustomerAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAutocompleteElementResponse from a JSON string
customer_autocomplete_element_response_instance = CustomerAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerAutocompleteElementResponse.to_json())

# convert the object into a dict
customer_autocomplete_element_response_dict = customer_autocomplete_element_response_instance.to_dict()
# create an instance of CustomerAutocompleteElementResponse from a dict
customer_autocomplete_element_response_from_dict = CustomerAutocompleteElementResponse.from_dict(customer_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


