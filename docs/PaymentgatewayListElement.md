# PaymentgatewayListElement

A Paymentgateway List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentgateway_id** | **int** | The unique ID of the Paymentgateway | 
**fki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | 
**e_paymentgateway_processor** | [**FieldEPaymentgatewayProcessor**](FieldEPaymentgatewayProcessor.md) |  | 
**s_paymentgateway_description_x** | **str** | The description of the Paymentgateway in the language of the requester | 

## Example

```python
from eZmaxApi.models.paymentgateway_list_element import PaymentgatewayListElement

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayListElement from a JSON string
paymentgateway_list_element_instance = PaymentgatewayListElement.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayListElement.to_json())

# convert the object into a dict
paymentgateway_list_element_dict = paymentgateway_list_element_instance.to_dict()
# create an instance of PaymentgatewayListElement from a dict
paymentgateway_list_element_from_dict = PaymentgatewayListElement.from_dict(paymentgateway_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


