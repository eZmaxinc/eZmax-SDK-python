# BillingentityinternalResponseCompound

A Billingentityinternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**obj_billingentityinternal_description** | [**MultilingualBillingentityinternalDescription**](MultilingualBillingentityinternalDescription.md) |  | 
**a_obj_billingentityinternalproduct** | [**List[BillingentityinternalproductResponseCompound]**](BillingentityinternalproductResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_response_compound import BillingentityinternalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalResponseCompound from a JSON string
billingentityinternal_response_compound_instance = BillingentityinternalResponseCompound.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalResponseCompound.to_json()

# convert the object into a dict
billingentityinternal_response_compound_dict = billingentityinternal_response_compound_instance.to_dict()
# create an instance of BillingentityinternalResponseCompound from a dict
billingentityinternal_response_compound_form_dict = billingentityinternal_response_compound.from_dict(billingentityinternal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


