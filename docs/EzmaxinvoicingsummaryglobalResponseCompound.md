# EzmaxinvoicingsummaryglobalResponseCompound

A Ezmaxinvoicingsummaryglobal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingsummaryglobal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryglobal | [optional] 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**s_ezmaxproduct_description_x** | **str** | The description of the Ezmaxproduct in the language of the requester | 
**dt_ezmaxinvoicingsummaryglobal_start** | **str** | The start date for the Ezmaxinvoicingsummaryglobal | 
**dt_ezmaxinvoicingsummaryglobal_end** | **str** | The end date for the Ezmaxinvoicingsummaryglobal | 
**i_ezmaxinvoicingsummaryglobal_days** | **int** | The number of days for the Ezmaxinvoicingsummaryglobal | 
**d_ezmaxinvoicingsummaryglobal_countreal** | **str** | The count item calculated | 
**d_ezmaxinvoicingsummaryglobal_countbilled** | **str** | The count item billed | 
**d_ezmaxinvoicingsummaryglobal_subtotal** | **str** | The Ezmaxinvoicingsummaryglobal subtotal | 
**d_ezmaxinvoicingsummaryglobal_rebateamount** | **str** | The rebate amount for the Ezmaxinvoicingsummaryglobal | 
**d_ezmaxinvoicingsummaryglobal_rebatepercent** | **str** | The rebate percentage of the Ezmaxinvoicingsummaryglobal | 
**d_ezmaxinvoicingsummaryglobal_rebatetotal** | **str** | The rebate amount total for the Ezmaxinvoicingsummaryglobal | 
**d_ezmaxinvoicingsummaryglobal_total** | **str** | The Ezmaxinvoicingsummaryglobal total | 
**d_ezmaxinvoicingsummaryglobal_representative** | **str** | The amount of commission for the representative | [optional] 
**d_ezmaxinvoicingsummaryglobal_partner** | **str** | The amount of commission for the partner | [optional] 
**d_ezmaxinvoicingsummaryglobal_net** | **str** | The net amount of the Ezmaxinvoicingsummaryglobal | [optional] 
**b_ezmaxinvoicingsummaryglobal_adjustment** | **bool** | Whether it is adjustment for the Ezmaxinvoicingsummaryglobal | 
**t_ezmaxproduct_help_x** | **str** | The help message of the Ezmaxproduct in the language of the requester | 
**a_obj_ezmaxinvoicingcommission** | [**List[EzmaxinvoicingcommissionResponseCompound]**](EzmaxinvoicingcommissionResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingsummaryglobal_response_compound import EzmaxinvoicingsummaryglobalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingsummaryglobalResponseCompound from a JSON string
ezmaxinvoicingsummaryglobal_response_compound_instance = EzmaxinvoicingsummaryglobalResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingsummaryglobalResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingsummaryglobal_response_compound_dict = ezmaxinvoicingsummaryglobal_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingsummaryglobalResponseCompound from a dict
ezmaxinvoicingsummaryglobal_response_compound_from_dict = EzmaxinvoicingsummaryglobalResponseCompound.from_dict(ezmaxinvoicingsummaryglobal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


