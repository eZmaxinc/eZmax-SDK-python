# SupplyRequestCompound

A Supply Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_supply_id** | **int** | The unique ID of the Supply | [optional] 
**fki_glaccount_id** | **int** | The unique ID of the Glaccount | [optional] 
**fki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | [optional] 
**fki_variableexpense_id** | **int** | The unique ID of the Variableexpense | 
**s_supply_code** | **str** | The code of the Supply | 
**obj_supply_description** | [**MultilingualSupplyDescription**](MultilingualSupplyDescription.md) |  | 
**d_supply_unitprice** | **str** | The unit price of the Supply | 
**b_supply_isactive** | **bool** | Whether the supply is active or not | 
**b_supply_variableprice** | **bool** | Whether if the price is variable | 

## Example

```python
from eZmaxApi.models.supply_request_compound import SupplyRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyRequestCompound from a JSON string
supply_request_compound_instance = SupplyRequestCompound.from_json(json)
# print the JSON string representation of the object
print(SupplyRequestCompound.to_json())

# convert the object into a dict
supply_request_compound_dict = supply_request_compound_instance.to_dict()
# create an instance of SupplyRequestCompound from a dict
supply_request_compound_from_dict = SupplyRequestCompound.from_dict(supply_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


