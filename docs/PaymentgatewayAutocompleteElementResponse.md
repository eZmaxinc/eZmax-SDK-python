# PaymentgatewayAutocompleteElementResponse

A Paymentgateway AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentgateway_id** | **int** | The unique ID of the Paymentgateway | 
**s_paymentgateway_description_x** | **str** | The description of the Paymentgateway in the language of the requester | 
**b_paymentgateway_isactive** | **bool** | Whether the Currency is active or not | 

## Example

```python
from eZmaxApi.models.paymentgateway_autocomplete_element_response import PaymentgatewayAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayAutocompleteElementResponse from a JSON string
paymentgateway_autocomplete_element_response_instance = PaymentgatewayAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayAutocompleteElementResponse.to_json())

# convert the object into a dict
paymentgateway_autocomplete_element_response_dict = paymentgateway_autocomplete_element_response_instance.to_dict()
# create an instance of PaymentgatewayAutocompleteElementResponse from a dict
paymentgateway_autocomplete_element_response_from_dict = PaymentgatewayAutocompleteElementResponse.from_dict(paymentgateway_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


