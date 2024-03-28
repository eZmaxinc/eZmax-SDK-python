# EzmaxinvoicingsummaryexternaldetailResponseCompound

A Ezmaxinvoicingsummaryexternaldetail Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryexternaldetail_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryexternaldetail | [optional] 
**fki_ezmaxinvoicingsummaryexternal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryexternal | [optional] 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**s_ezmaxproduct_description_x** | **str** | The description of the Ezmaxproduct in the language of the requester | 
**d_ezmaxinvoicingsummaryexternaldetail_countreal** | **str** | The count item invoiced for the product | 
**d_ezmaxinvoicingsummaryexternaldetail_subtotal** | **str** | The subtotal invoiced for the product | 
**d_ezmaxinvoicingsummaryexternaldetail_rebate** | **str** | The rebate for the product | 
**d_ezmaxinvoicingsummaryexternaldetail_total** | **str** | The total invoiced for the product | 
**b_ezmaxinvoicingsummaryexternaldetail_adjustment** | **bool** | Whether it&#39;s an adjustment | 
**t_ezmaxproduct_help_x** | **str** | The help message of the Ezmaxproduct in the language of the requester | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryexternaldetail_response_compound import EzmaxinvoicingsummaryexternaldetailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryexternaldetailResponseCompound from a JSON string
ezmaxinvoicingsummaryexternaldetail_response_compound_instance = EzmaxinvoicingsummaryexternaldetailResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryexternaldetailResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryexternaldetail_response_compound_dict = ezmaxinvoicingsummaryexternaldetail_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryexternaldetailResponseCompound from a dict
ezmaxinvoicingsummaryexternaldetail_response_compound_form_dict = ezmaxinvoicingsummaryexternaldetail_response_compound.from_dict(ezmaxinvoicingsummaryexternaldetail_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


