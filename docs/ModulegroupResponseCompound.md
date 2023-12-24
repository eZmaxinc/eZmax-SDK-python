# ModulegroupResponseCompound

A Modulegroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_modulegroup_id** | **int** | The unique ID of the Modulegroup | 
**s_modulegroup_name_x** | **str** | The name of the Modulegroup in the language of the requester | 
**a_obj_module** | [**List[ModuleResponseCompound]**](ModuleResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.modulegroup_response_compound import ModulegroupResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ModulegroupResponseCompound from a JSON string
modulegroup_response_compound_instance = ModulegroupResponseCompound.from_json(json)
# print the JSON string representation of the object
print ModulegroupResponseCompound.to_json()

# convert the object into a dict
modulegroup_response_compound_dict = modulegroup_response_compound_instance.to_dict()
# create an instance of ModulegroupResponseCompound from a dict
modulegroup_response_compound_form_dict = modulegroup_response_compound.from_dict(modulegroup_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


