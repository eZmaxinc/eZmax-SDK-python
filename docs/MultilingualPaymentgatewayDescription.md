# MultilingualPaymentgatewayDescription

Description of the Paymentgateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_paymentgateway_description1** | **str** | The description of the Paymentgateway in French | [optional] 
**s_paymentgateway_description2** | **str** | The description of the Paymentgateway in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_paymentgateway_description import MultilingualPaymentgatewayDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualPaymentgatewayDescription from a JSON string
multilingual_paymentgateway_description_instance = MultilingualPaymentgatewayDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualPaymentgatewayDescription.to_json())

# convert the object into a dict
multilingual_paymentgateway_description_dict = multilingual_paymentgateway_description_instance.to_dict()
# create an instance of MultilingualPaymentgatewayDescription from a dict
multilingual_paymentgateway_description_from_dict = MultilingualPaymentgatewayDescription.from_dict(multilingual_paymentgateway_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


