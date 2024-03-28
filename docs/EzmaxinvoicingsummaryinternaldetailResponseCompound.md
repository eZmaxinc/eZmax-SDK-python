# EzmaxinvoicingsummaryinternaldetailResponseCompound

A Ezmaxinvoicingsummaryinternaldetail Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryinternaldetail_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryinternaldetail | [optional] 
**fki_ezmaxinvoicingsummaryinternal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryinternal | [optional] 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**s_ezmaxproduct_description_x** | **str** | The description of the Ezmaxproduct in the language of the requester | 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 
**s_billingentityexternal_description** | **str** | The description of the Billingentityexternal | 
**d_ezmaxinvoicingsummaryinternaldetail_countreal** | **str** | The count item invoiced for the product | 
**d_ezmaxinvoicingsummaryinternaldetail_subtotal** | **str** | The subtotal invoiced for the product | 
**d_ezmaxinvoicingsummaryinternaldetail_rebate** | **str** | The rebate for the product | 
**d_ezmaxinvoicingsummaryinternaldetail_total** | **str** | The total invoiced for the product | 
**b_ezmaxinvoicingsummaryinternaldetail_adjustment** | **bool** | Whether if it&#39;s an adjustment | 
**t_ezmaxproduct_help_x** | **str** | The help message of the Ezmaxproduct in the language of the requester | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryinternaldetail_response_compound import EzmaxinvoicingsummaryinternaldetailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryinternaldetailResponseCompound from a JSON string
ezmaxinvoicingsummaryinternaldetail_response_compound_instance = EzmaxinvoicingsummaryinternaldetailResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryinternaldetailResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryinternaldetail_response_compound_dict = ezmaxinvoicingsummaryinternaldetail_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryinternaldetailResponseCompound from a dict
ezmaxinvoicingsummaryinternaldetail_response_compound_form_dict = ezmaxinvoicingsummaryinternaldetail_response_compound.from_dict(ezmaxinvoicingsummaryinternaldetail_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


