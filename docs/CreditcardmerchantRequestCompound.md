# CreditcardmerchantRequestCompound

A Creditcardmerchant Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | [optional] 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | [optional] 
**b_creditcardmerchant_denyvisa** | **bool** | Whether if visa are denied | 
**b_creditcardmerchant_denymastercard** | **bool** | Whether if mastercard are denied | 
**b_creditcardmerchant_denyamex** | **bool** | Whether if amex are denied | 
**b_creditcardmerchant_isactive** | **bool** | Whether the creditcardmerchant is active or not | 
**s_creditcardmerchant_apitoken** | **str** | The apitoken of the Creditcardmerchant | [optional] 
**s_creditcardmerchant_description** | **str** | The description of the Creditcardmerchant | 
**s_creditcardmerchant_storeid** | **str** | The storeid of the Creditcardmerchant | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_request_compound import CreditcardmerchantRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantRequestCompound from a JSON string
creditcardmerchant_request_compound_instance = CreditcardmerchantRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantRequestCompound.to_json())

# convert the object into a dict
creditcardmerchant_request_compound_dict = creditcardmerchant_request_compound_instance.to_dict()
# create an instance of CreditcardmerchantRequestCompound from a dict
creditcardmerchant_request_compound_from_dict = CreditcardmerchantRequestCompound.from_dict(creditcardmerchant_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


