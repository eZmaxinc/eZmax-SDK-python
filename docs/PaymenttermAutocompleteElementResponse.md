# PaymenttermAutocompleteElementResponse

A Paymentterm AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentterm_id** | **int** | The unique ID of the Paymentterm | 
**s_paymentterm_description_x** | **str** | The description of the Paymentterm in the language of the requester | 
**b_paymentterm_isactive** | **bool** | Whether the Paymentterm is active or not | 

## Example

```python
from eZmaxApi.models.paymentterm_autocomplete_element_response import PaymenttermAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermAutocompleteElementResponse from a JSON string
paymentterm_autocomplete_element_response_instance = PaymenttermAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print PaymenttermAutocompleteElementResponse.to_json()

# convert the object into a dict
paymentterm_autocomplete_element_response_dict = paymentterm_autocomplete_element_response_instance.to_dict()
# create an instance of PaymenttermAutocompleteElementResponse from a dict
paymentterm_autocomplete_element_response_form_dict = paymentterm_autocomplete_element_response.from_dict(paymentterm_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


