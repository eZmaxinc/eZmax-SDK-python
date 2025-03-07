# PaymentgatewayResponse

A Paymentgateway Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentgateway_id** | **int** | The unique ID of the Paymentgateway | 
**fki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | [optional] 
**s_creditcardmerchant_description** | **str** | The description of the Creditcardmerchant | [optional] 
**e_paymentgateway_processor** | [**FieldEPaymentgatewayProcessor**](FieldEPaymentgatewayProcessor.md) |  | 
**obj_paymentgateway_description** | [**MultilingualPaymentgatewayDescription**](MultilingualPaymentgatewayDescription.md) |  | 
**obj_creditcardmerchant** | [**CreditcardmerchantResponseCompound**](CreditcardmerchantResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.paymentgateway_response import PaymentgatewayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayResponse from a JSON string
paymentgateway_response_instance = PaymentgatewayResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayResponse.to_json())

# convert the object into a dict
paymentgateway_response_dict = paymentgateway_response_instance.to_dict()
# create an instance of PaymentgatewayResponse from a dict
paymentgateway_response_from_dict = PaymentgatewayResponse.from_dict(paymentgateway_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


