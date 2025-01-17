# EzmaxinvoicingsummaryinternalResponseCompound

A Ezmaxinvoicingsummaryinternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryinternal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryinternal | [optional] 
**obj_ezmaxinvoicingsummaryinternal_description** | [**MultilingualEzmaxinvoicingsummaryinternalDescription**](MultilingualEzmaxinvoicingsummaryinternalDescription.md) |  | 
**s_ezmaxinvoicingsummaryinternal_description_x** | **str** | The Ezmaxinvoicingsummaryinternal description in the language of the requester | 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**a_obj_ezmaxinvoicingsummaryinternaldetail** | [**List[EzmaxinvoicingsummaryinternaldetailResponseCompound]**](EzmaxinvoicingsummaryinternaldetailResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryinternal_response_compound import EzmaxinvoicingsummaryinternalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryinternalResponseCompound from a JSON string
ezmaxinvoicingsummaryinternal_response_compound_instance = EzmaxinvoicingsummaryinternalResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryinternalResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryinternal_response_compound_dict = ezmaxinvoicingsummaryinternal_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryinternalResponseCompound from a dict
ezmaxinvoicingsummaryinternal_response_compound_from_dict = EzmaxinvoicingsummaryinternalResponseCompound.from_dict(ezmaxinvoicingsummaryinternal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


