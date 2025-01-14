# EzmaxinvoicingsummaryexternalResponseCompound

A Ezmaxinvoicingsummaryexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryexternal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryexternal | [optional] 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 
**s_billingentityexternal_description** | **str** | The description of the Billingentityexternal | 
**s_ezmaxinvoicingsummaryexternal_description** | **str** | The description of the Ezmaxinvoicingsummaryexternal | 
**a_obj_ezmaxinvoicingsummaryexternaldetail** | [**List[EzmaxinvoicingsummaryexternaldetailResponseCompound]**](EzmaxinvoicingsummaryexternaldetailResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryexternal_response_compound import EzmaxinvoicingsummaryexternalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryexternalResponseCompound from a JSON string
ezmaxinvoicingsummaryexternal_response_compound_instance = EzmaxinvoicingsummaryexternalResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryexternalResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryexternal_response_compound_dict = ezmaxinvoicingsummaryexternal_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryexternalResponseCompound from a dict
ezmaxinvoicingsummaryexternal_response_compound_from_dict = EzmaxinvoicingsummaryexternalResponseCompound.from_dict(ezmaxinvoicingsummaryexternal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


