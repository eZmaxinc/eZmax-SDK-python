# CustomCreditcardtransactionResponse

A custom Creditcardtransaction Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_creditcardtype_codename** | [**FieldECreditcardtypeCodename**](FieldECreditcardtypeCodename.md) |  | 
**d_creditcardtransaction_amount** | **str** | The amount of the Creditcardtransaction | 
**s_creditcardtransaction_partiallydecryptednumber** | **str** | The partially decrypted credit card number used in the Creditcardtransaction | 
**s_creditcardtransaction_referencenumber** | **str** | The reference number on the creditcard service for the Creditcardtransaction | 

## Example

```python
from eZmaxApi.models.custom_creditcardtransaction_response import CustomCreditcardtransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCreditcardtransactionResponse from a JSON string
custom_creditcardtransaction_response_instance = CustomCreditcardtransactionResponse.from_json(json)
# print the JSON string representation of the object
print CustomCreditcardtransactionResponse.to_json()

# convert the object into a dict
custom_creditcardtransaction_response_dict = custom_creditcardtransaction_response_instance.to_dict()
# create an instance of CustomCreditcardtransactionResponse from a dict
custom_creditcardtransaction_response_form_dict = custom_creditcardtransaction_response.from_dict(custom_creditcardtransaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


