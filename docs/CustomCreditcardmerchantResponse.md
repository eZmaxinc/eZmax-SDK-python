# CustomCreditcardmerchantResponse

A Creditcardmerchant Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_creditcardmerchant_denyamex** | **bool** | Whether if amex are denied | [optional] 
**b_creditcardmerchant_denymastercard** | **bool** | Whether if mastercard are denied | [optional] 
**b_creditcardmerchant_denyvisa** | **bool** | Whether if visa are denied | [optional] 

## Example

```python
from eZmaxApi.models.custom_creditcardmerchant_response import CustomCreditcardmerchantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCreditcardmerchantResponse from a JSON string
custom_creditcardmerchant_response_instance = CustomCreditcardmerchantResponse.from_json(json)
# print the JSON string representation of the object
print(CustomCreditcardmerchantResponse.to_json())

# convert the object into a dict
custom_creditcardmerchant_response_dict = custom_creditcardmerchant_response_instance.to_dict()
# create an instance of CustomCreditcardmerchantResponse from a dict
custom_creditcardmerchant_response_from_dict = CustomCreditcardmerchantResponse.from_dict(custom_creditcardmerchant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


