# ModulesectionResponse

A Modulesection Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_modulesection_id** | **int** | The unique ID of the Modulesection | 
**fki_module_id** | **int** | The unique ID of the Module | 
**s_modulesection_internalname** | **str** | The Internal name of the Module section. | 
**s_modulesection_name_x** | **str** | The Name of the Modulesection in the language of the requester | 

## Example

```python
from eZmaxApi.models.modulesection_response import ModulesectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesectionResponse from a JSON string
modulesection_response_instance = ModulesectionResponse.from_json(json)
# print the JSON string representation of the object
print(ModulesectionResponse.to_json())

# convert the object into a dict
modulesection_response_dict = modulesection_response_instance.to_dict()
# create an instance of ModulesectionResponse from a dict
modulesection_response_from_dict = ModulesectionResponse.from_dict(modulesection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


