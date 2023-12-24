# BillingentityinternalproductRequestCompound

A Billingentityinternalproduct Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternalproduct_id** | **int** | The unique ID of the Billingentityinternalproduct | [optional] 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 

## Example

```python
from eZmaxApi.models.billingentityinternalproduct_request_compound import BillingentityinternalproductRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalproductRequestCompound from a JSON string
billingentityinternalproduct_request_compound_instance = BillingentityinternalproductRequestCompound.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalproductRequestCompound.to_json()

# convert the object into a dict
billingentityinternalproduct_request_compound_dict = billingentityinternalproduct_request_compound_instance.to_dict()
# create an instance of BillingentityinternalproductRequestCompound from a dict
billingentityinternalproduct_request_compound_form_dict = billingentityinternalproduct_request_compound.from_dict(billingentityinternalproduct_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


