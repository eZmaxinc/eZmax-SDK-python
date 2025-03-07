# PaymentgatewayRequestCompound

A Paymentgateway Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentgateway_id** | **int** | The unique ID of the Paymentgateway | [optional] 
**e_paymentgateway_processor** | [**FieldEPaymentgatewayProcessor**](FieldEPaymentgatewayProcessor.md) |  | 
**obj_paymentgateway_description** | [**MultilingualPaymentgatewayDescription**](MultilingualPaymentgatewayDescription.md) |  | 
**obj_creditcardmerchant** | [**CreditcardmerchantRequestCompound**](CreditcardmerchantRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.paymentgateway_request_compound import PaymentgatewayRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayRequestCompound from a JSON string
paymentgateway_request_compound_instance = PaymentgatewayRequestCompound.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayRequestCompound.to_json())

# convert the object into a dict
paymentgateway_request_compound_dict = paymentgateway_request_compound_instance.to_dict()
# create an instance of PaymentgatewayRequestCompound from a dict
paymentgateway_request_compound_from_dict = PaymentgatewayRequestCompound.from_dict(paymentgateway_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


