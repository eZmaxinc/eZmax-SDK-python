# BankaccountListElement

A Bankaccount List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**s_bankaccount_bankname** | **str** | The name of the bank | 
**s_bankaccount_transit** | **str** | The transit of the Bankaccount | 
**s_bankaccount_institution** | **str** | The institution of the Bankaccount | 
**s_bankaccount_account** | **str** | The account of the Bankaccount | 
**s_bankaccount_number** | **str** | The account number of the Bankaccount | 
**e_bankaccount_type** | [**FieldEBankaccountType**](FieldEBankaccountType.md) |  | [optional] 
**b_bankaccount_commissionprocessing** | **bool** | Whether if it&#39;s an commissionprocessing | [optional] 
**b_bankaccount_isactive** | **bool** | Whether the Bankaccount is active or not | 
**i_glaccount_code** | **int** | The Code of the Glaccount | 
**s_glaccount_description_x** | **str** | The Description for the Glaccount in the language of the requester | 

## Example

```python
from eZmaxApi.models.bankaccount_list_element import BankaccountListElement

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountListElement from a JSON string
bankaccount_list_element_instance = BankaccountListElement.from_json(json)
# print the JSON string representation of the object
print(BankaccountListElement.to_json())

# convert the object into a dict
bankaccount_list_element_dict = bankaccount_list_element_instance.to_dict()
# create an instance of BankaccountListElement from a dict
bankaccount_list_element_from_dict = BankaccountListElement.from_dict(bankaccount_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


