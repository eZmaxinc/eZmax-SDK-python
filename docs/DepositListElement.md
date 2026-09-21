# DepositListElement

A Deposit List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_deposit_id** | **int** | The unique ID of the Deposit | 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**fki_period_id** | **int** | The unique ID of the Period | 
**fki_user_id_created** | **int** | The unique ID of the User | 
**s_deposit_number** | **str** | The number of the Deposit | 
**dt_deposit_date** | **str** | The date of the Deposit | 
**d_deposit_total** | **str** | The total of the Deposit | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**b_deposit_draft** | **bool** | Whether if it&#39;s an draft | 
**b_deposit_reconciled** | **bool** | Whether if it&#39;s reconciled | 
**fki_reconciliation_id** | **int** | The unique ID of the Reconciliation | [optional] 
**s_bankaccount_bankname** | **str** | The name of the bank | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | 
**s_user_loginname** | **str** | The login name of the User. | 

## Example

```python
from eZmaxApi.models.deposit_list_element import DepositListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DepositListElement from a JSON string
deposit_list_element_instance = DepositListElement.from_json(json)
# print the JSON string representation of the object
print(DepositListElement.to_json())

# convert the object into a dict
deposit_list_element_dict = deposit_list_element_instance.to_dict()
# create an instance of DepositListElement from a dict
deposit_list_element_from_dict = DepositListElement.from_dict(deposit_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


