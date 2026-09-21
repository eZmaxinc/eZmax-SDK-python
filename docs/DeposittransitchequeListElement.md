# DeposittransitchequeListElement

A Deposittransitcheque List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_deposittransitcheque_id** | **int** | The unique ID of the Deposittransitcheque | 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**fki_deposit_id** | **int** | The unique ID of the Deposit | [optional] 
**s_deposittransitcheque_number** | **str** | The number of the Deposittransitcheque | 
**dt_deposittransitcheque_date** | **str** | The date of the Deposittransitcheque | 
**d_deposittransitcheque_amount** | **str** | The amount of the Deposittransitcheque | 
**s_bankaccount_bankname** | **str** | The name of the bank | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | 
**s_customer_name** | **str** | The name of the Customer | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_list_element import DeposittransitchequeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeListElement from a JSON string
deposittransitcheque_list_element_instance = DeposittransitchequeListElement.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeListElement.to_json())

# convert the object into a dict
deposittransitcheque_list_element_dict = deposittransitcheque_list_element_instance.to_dict()
# create an instance of DeposittransitchequeListElement from a dict
deposittransitcheque_list_element_from_dict = DeposittransitchequeListElement.from_dict(deposittransitcheque_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


