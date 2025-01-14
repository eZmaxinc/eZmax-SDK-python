# SupplyResponseCompound

A Supply Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_supply_id** | **int** | The unique ID of the Supply | 
**fki_glaccount_id** | **int** | The unique ID of the Glaccount | [optional] 
**fki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | [optional] 
**fki_variableexpense_id** | **int** | The unique ID of the Variableexpense | 
**s_supply_code** | **str** | The code of the Supply | 
**obj_supply_description** | [**MultilingualSupplyDescription**](MultilingualSupplyDescription.md) |  | 
**d_supply_unitprice** | **str** | The unit price of the Supply | 
**b_supply_isactive** | **bool** | Whether the supply is active or not | 
**b_supply_variableprice** | **bool** | Whether if the price is variable | 
**s_glaccount_description_x** | **str** | The Description for the Glaccount in the language of the requester | [optional] 
**s_glaccountcontainer_longdescription_x** | **str** | The Description for the Glaccountcontainer in the language of the requester | [optional] 
**s_variableexpense_description_x** | **str** | The description of the Variableexpense in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.supply_response_compound import SupplyResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyResponseCompound from a JSON string
supply_response_compound_instance = SupplyResponseCompound.from_json(json)
# print the JSON string representation of the object
print(SupplyResponseCompound.to_json())

# convert the object into a dict
supply_response_compound_dict = supply_response_compound_instance.to_dict()
# create an instance of SupplyResponseCompound from a dict
supply_response_compound_from_dict = SupplyResponseCompound.from_dict(supply_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


