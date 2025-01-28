# CreditcardmerchantResponseCompound

A Creditcardmerchant Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**s_bankaccount_bankname** | **str** | The name of the bank | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | [optional] 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | [optional] 
**b_creditcardmerchant_denyvisa** | **bool** | Whether if visa are denied | 
**b_creditcardmerchant_denymastercard** | **bool** | Whether if mastercard are denied | 
**b_creditcardmerchant_denyamex** | **bool** | Whether if amex are denied | 
**b_creditcardmerchant_isactive** | **bool** | Whether the creditcardmerchant is active or not | 
**s_creditcardmerchant_description** | **str** | The description of the Creditcardmerchant | 
**s_creditcardmerchant_storeid** | **str** | The storeid of the Creditcardmerchant | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_response_compound import CreditcardmerchantResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantResponseCompound from a JSON string
creditcardmerchant_response_compound_instance = CreditcardmerchantResponseCompound.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantResponseCompound.to_json())

# convert the object into a dict
creditcardmerchant_response_compound_dict = creditcardmerchant_response_compound_instance.to_dict()
# create an instance of CreditcardmerchantResponseCompound from a dict
creditcardmerchant_response_compound_from_dict = CreditcardmerchantResponseCompound.from_dict(creditcardmerchant_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


