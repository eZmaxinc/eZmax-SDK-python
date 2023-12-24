# BillingentityinternalproductResponseCompound

A Billingentityinternalproduct Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternalproduct_id** | **int** | The unique ID of the Billingentityinternalproduct | 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**s_ezmaxproduct_description_x** | **str** | The description of the Ezmaxproduct in the language of the requester | 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 
**s_billingentityexternal_description** | **str** | The description of the Billingentityexternal | 

## Example

```python
from eZmaxApi.models.billingentityinternalproduct_response_compound import BillingentityinternalproductResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalproductResponseCompound from a JSON string
billingentityinternalproduct_response_compound_instance = BillingentityinternalproductResponseCompound.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalproductResponseCompound.to_json()

# convert the object into a dict
billingentityinternalproduct_response_compound_dict = billingentityinternalproduct_response_compound_instance.to_dict()
# create an instance of BillingentityinternalproductResponseCompound from a dict
billingentityinternalproduct_response_compound_form_dict = billingentityinternalproduct_response_compound.from_dict(billingentityinternalproduct_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


