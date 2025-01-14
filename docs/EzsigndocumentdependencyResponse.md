# EzsigndocumentdependencyResponse

An Ezsigndocumentdependency Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocumentdependency_id** | **int** | The unique ID of the Ezsigndocumentdependency | 
**fki_ezsigndocument_i_ddependency** | **int** | The unique ID of the Ezsigndocument | 

## Example

```python
from eZmaxApi.models.ezsigndocumentdependency_response import EzsigndocumentdependencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentdependencyResponse from a JSON string
ezsigndocumentdependency_response_instance = EzsigndocumentdependencyResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentdependencyResponse.to_json())

# convert the object into a dict
ezsigndocumentdependency_response_dict = ezsigndocumentdependency_response_instance.to_dict()
# create an instance of EzsigndocumentdependencyResponse from a dict
ezsigndocumentdependency_response_from_dict = EzsigndocumentdependencyResponse.from_dict(ezsigndocumentdependency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


