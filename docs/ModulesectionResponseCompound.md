# ModulesectionResponseCompound

A Modulesection Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_permission** | [**List[PermissionResponseCompound]**](PermissionResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.modulesection_response_compound import ModulesectionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesectionResponseCompound from a JSON string
modulesection_response_compound_instance = ModulesectionResponseCompound.from_json(json)
# print the JSON string representation of the object
print(ModulesectionResponseCompound.to_json())

# convert the object into a dict
modulesection_response_compound_dict = modulesection_response_compound_instance.to_dict()
# create an instance of ModulesectionResponseCompound from a dict
modulesection_response_compound_from_dict = ModulesectionResponseCompound.from_dict(modulesection_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


