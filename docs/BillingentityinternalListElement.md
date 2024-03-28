# BillingentityinternalListElement

A Billingentityinternal List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 

## Example

```python
from eZmaxApi.models.billingentityinternal_list_element import BillingentityinternalListElement

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalListElement from a JSON string
billingentityinternal_list_element_instance = BillingentityinternalListElement.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalListElement.to_json())

# convert the object into a dict
billingentityinternal_list_element_dict = billingentityinternal_list_element_instance.to_dict()
# create an instance of BillingentityinternalListElement from a dict
billingentityinternal_list_element_form_dict = billingentityinternal_list_element.from_dict(billingentityinternal_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


