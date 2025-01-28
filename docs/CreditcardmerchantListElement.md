# CreditcardmerchantListElement

A Creditcardmerchant List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | [optional] 
**b_creditcardmerchant_denyvisa** | **bool** | Whether if visa are denied | 
**b_creditcardmerchant_denymastercard** | **bool** | Whether if mastercard are denied | 
**b_creditcardmerchant_denyamex** | **bool** | Whether if amex are denied | 
**b_creditcardmerchant_isactive** | **bool** | Whether the creditcardmerchant is active or not | 
**s_creditcardmerchant_description** | **str** | The description of the Creditcardmerchant | 
**s_creditcardmerchant_storeid** | **str** | The storeid of the Creditcardmerchant | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_list_element import CreditcardmerchantListElement

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantListElement from a JSON string
creditcardmerchant_list_element_instance = CreditcardmerchantListElement.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantListElement.to_json())

# convert the object into a dict
creditcardmerchant_list_element_dict = creditcardmerchant_list_element_instance.to_dict()
# create an instance of CreditcardmerchantListElement from a dict
creditcardmerchant_list_element_from_dict = CreditcardmerchantListElement.from_dict(creditcardmerchant_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


