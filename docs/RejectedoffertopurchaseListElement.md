# RejectedoffertopurchaseListElement

A Rejectedoffertopurchase List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_rejectedoffertopurchase_id** | **int** | The unique ID of the Rejectedoffertopurchase | 
**s_rejectedoffertopurchase_number** | **str** | The number of the Rejectedoffertopurchase | 
**dt_rejectedoffertopurchase_date** | **str** | The date of the Rejectedoffertopurchase | 
**b_rejectedoffertopurchase_isactive** | **bool** | Whether the rejectedoffertopurchase is active or not | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 
**b_rejectedoffertopurchase_linkedtoinscription** | **bool** | Indicate if the Rejectedoffertopurchase is linked to an inscription | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_list_element import RejectedoffertopurchaseListElement

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseListElement from a JSON string
rejectedoffertopurchase_list_element_instance = RejectedoffertopurchaseListElement.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseListElement.to_json())

# convert the object into a dict
rejectedoffertopurchase_list_element_dict = rejectedoffertopurchase_list_element_instance.to_dict()
# create an instance of RejectedoffertopurchaseListElement from a dict
rejectedoffertopurchase_list_element_from_dict = RejectedoffertopurchaseListElement.from_dict(rejectedoffertopurchase_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


