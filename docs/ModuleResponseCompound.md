# ModuleResponseCompound

A Module Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_module_id** | **int** | The unique ID of the Module | 
**fki_modulegroup_id** | **int** | The unique ID of the Modulegroup | 
**e_module_internalname** | **str** | The Internal name of the Module.  This is theoretically an enum field but there are so many possibles values we decided not to list them all. | 
**s_module_name_x** | **str** | The Name of the Module in the language of the requester | 
**b_module_registered** | **bool** | Whether the Module is registered or not | 
**b_module_registeredapi** | **bool** | Whether the Module is registered or not for api use | 
**a_obj_modulesection** | [**List[ModulesectionResponseCompound]**](ModulesectionResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.module_response_compound import ModuleResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleResponseCompound from a JSON string
module_response_compound_instance = ModuleResponseCompound.from_json(json)
# print the JSON string representation of the object
print(ModuleResponseCompound.to_json())

# convert the object into a dict
module_response_compound_dict = module_response_compound_instance.to_dict()
# create an instance of ModuleResponseCompound from a dict
module_response_compound_from_dict = ModuleResponseCompound.from_dict(module_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


