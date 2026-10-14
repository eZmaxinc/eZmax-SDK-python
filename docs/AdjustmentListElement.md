# AdjustmentListElement

A Adjustment List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_adjustment_id** | **int** | The unique ID of the Adjustment | 
**fki_period_id** | **int** | The unique ID of the Period | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | [optional] 
**fki_user_id_created** | **int** | The unique ID of the User | [optional] 
**s_user_loginname** | **str** | The login name of the User. | [optional] 
**dt_adjustment_date** | **str** | The date of the Adjustment | 
**s_adjustment_number** | **str** | The number of the Adjustment | 
**s_adjustment_comment** | **str** | The comment of the Adjustment | 
**d_adjustment_totaldebit** | **str** | The total debit of Adjustment | [optional] 
**d_adjustment_totalcredit** | **str** | The total credit of Adjustment | [optional] 

## Example

```python
from eZmaxApi.models.adjustment_list_element import AdjustmentListElement

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentListElement from a JSON string
adjustment_list_element_instance = AdjustmentListElement.from_json(json)
# print the JSON string representation of the object
print(AdjustmentListElement.to_json())

# convert the object into a dict
adjustment_list_element_dict = adjustment_list_element_instance.to_dict()
# create an instance of AdjustmentListElement from a dict
adjustment_list_element_from_dict = AdjustmentListElement.from_dict(adjustment_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


