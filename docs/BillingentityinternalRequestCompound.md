# BillingentityinternalRequestCompound

A Billingentityinternal Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**obj_billingentityinternal_description** | [**MultilingualBillingentityinternalDescription**](MultilingualBillingentityinternalDescription.md) |  | 
**a_obj_billingentityinternalproduct** | [**List[BillingentityinternalproductRequestCompound]**](BillingentityinternalproductRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_request_compound import BillingentityinternalRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalRequestCompound from a JSON string
billingentityinternal_request_compound_instance = BillingentityinternalRequestCompound.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalRequestCompound.to_json())

# convert the object into a dict
billingentityinternal_request_compound_dict = billingentityinternal_request_compound_instance.to_dict()
# create an instance of BillingentityinternalRequestCompound from a dict
billingentityinternal_request_compound_form_dict = billingentityinternal_request_compound.from_dict(billingentityinternal_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


