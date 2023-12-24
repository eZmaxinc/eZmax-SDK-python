# ModulegroupResponse

A Modulegroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_modulegroup_id** | **int** | The unique ID of the Modulegroup | 
**s_modulegroup_name_x** | **str** | The name of the Modulegroup in the language of the requester | 

## Example

```python
from eZmaxApi.models.modulegroup_response import ModulegroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModulegroupResponse from a JSON string
modulegroup_response_instance = ModulegroupResponse.from_json(json)
# print the JSON string representation of the object
print ModulegroupResponse.to_json()

# convert the object into a dict
modulegroup_response_dict = modulegroup_response_instance.to_dict()
# create an instance of ModulegroupResponse from a dict
modulegroup_response_form_dict = modulegroup_response.from_dict(modulegroup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


