# PaymentmethodAutocompleteElementResponse

A Paymentmethod AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentmethod_id** | **int** | The unique ID of the Paymentmethod | 
**s_paymentmethod_description_x** | **str** | The description of the Paymentmethod in the language of the requester | 
**b_paymentmethod_isactive** | **bool** | Whether the Paymentmethod is active or not | 

## Example

```python
from eZmaxApi.models.paymentmethod_autocomplete_element_response import PaymentmethodAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentmethodAutocompleteElementResponse from a JSON string
paymentmethod_autocomplete_element_response_instance = PaymentmethodAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentmethodAutocompleteElementResponse.to_json())

# convert the object into a dict
paymentmethod_autocomplete_element_response_dict = paymentmethod_autocomplete_element_response_instance.to_dict()
# create an instance of PaymentmethodAutocompleteElementResponse from a dict
paymentmethod_autocomplete_element_response_from_dict = PaymentmethodAutocompleteElementResponse.from_dict(paymentmethod_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


