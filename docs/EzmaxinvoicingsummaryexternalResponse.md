# EzmaxinvoicingsummaryexternalResponse

A Ezmaxinvoicingsummaryexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryexternal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryexternal | [optional] 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 
**s_billingentityexternal_description** | **str** | The description of the Billingentityexternal | 
**s_ezmaxinvoicingsummaryexternal_description** | **str** | The description of the Ezmaxinvoicingsummaryexternal | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryexternal_response import EzmaxinvoicingsummaryexternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryexternalResponse from a JSON string
ezmaxinvoicingsummaryexternal_response_instance = EzmaxinvoicingsummaryexternalResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryexternalResponse.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryexternal_response_dict = ezmaxinvoicingsummaryexternal_response_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryexternalResponse from a dict
ezmaxinvoicingsummaryexternal_response_from_dict = EzmaxinvoicingsummaryexternalResponse.from_dict(ezmaxinvoicingsummaryexternal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


