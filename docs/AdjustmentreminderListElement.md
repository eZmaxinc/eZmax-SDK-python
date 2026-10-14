# AdjustmentreminderListElement

A Adjustmentreminder List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_adjustmentreminder_id** | **int** | The unique ID of the Adjustmentreminder | 
**fki_adjustment_id** | **int** | The unique ID of the Adjustment | 
**fki_period_id** | **int** | The unique ID of the Period | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | [optional] 
**fki_user_id_created** | **int** | The unique ID of the User | [optional] 
**s_user_loginname** | **str** | The login name of the User. | [optional] 
**e_adjustmentreminder_type** | [**FieldEAdjustmentreminderType**](FieldEAdjustmentreminderType.md) |  | 
**s_adjustment_number** | **str** | The number of the Adjustment | [optional] 
**s_adjustment_comment** | **str** | The comment of the Adjustment | [optional] 
**d_adjustment_totaldebit** | **str** | The total debit of Adjustment | [optional] 
**d_adjustment_totalcredit** | **str** | The total credit of Adjustment | [optional] 

## Example

```python
from eZmaxApi.models.adjustmentreminder_list_element import AdjustmentreminderListElement

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentreminderListElement from a JSON string
adjustmentreminder_list_element_instance = AdjustmentreminderListElement.from_json(json)
# print the JSON string representation of the object
print(AdjustmentreminderListElement.to_json())

# convert the object into a dict
adjustmentreminder_list_element_dict = adjustmentreminder_list_element_instance.to_dict()
# create an instance of AdjustmentreminderListElement from a dict
adjustmentreminder_list_element_from_dict = AdjustmentreminderListElement.from_dict(adjustmentreminder_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


