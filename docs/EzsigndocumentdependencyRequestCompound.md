# EzsigndocumentdependencyRequestCompound

An Ezsigndocumentdependency Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocumentdependency_id** | **int** | The unique ID of the Ezsigndocumentdependency | [optional] 
**fki_ezsigndocument_i_ddependency** | **int** | The unique ID of the Ezsigndocument | 

## Example

```python
from eZmaxApi.models.ezsigndocumentdependency_request_compound import EzsigndocumentdependencyRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentdependencyRequestCompound from a JSON string
ezsigndocumentdependency_request_compound_instance = EzsigndocumentdependencyRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentdependencyRequestCompound.to_json())

# convert the object into a dict
ezsigndocumentdependency_request_compound_dict = ezsigndocumentdependency_request_compound_instance.to_dict()
# create an instance of EzsigndocumentdependencyRequestCompound from a dict
ezsigndocumentdependency_request_compound_from_dict = EzsigndocumentdependencyRequestCompound.from_dict(ezsigndocumentdependency_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


