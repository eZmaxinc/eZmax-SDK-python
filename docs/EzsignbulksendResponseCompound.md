# EzsignbulksendResponseCompound

An Ezsignbulksend Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksenddocumentmapping** | [**List[EzsignbulksenddocumentmappingResponseCompound]**](EzsignbulksenddocumentmappingResponseCompound.md) |  | 
**a_obj_ezsignbulksendsignermapping** | [**List[EzsignbulksendsignermappingResponse]**](EzsignbulksendsignermappingResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_response_compound import EzsignbulksendResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendResponseCompound from a JSON string
ezsignbulksend_response_compound_instance = EzsignbulksendResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendResponseCompound.to_json())

# convert the object into a dict
ezsignbulksend_response_compound_dict = ezsignbulksend_response_compound_instance.to_dict()
# create an instance of EzsignbulksendResponseCompound from a dict
ezsignbulksend_response_compound_from_dict = EzsignbulksendResponseCompound.from_dict(ezsignbulksend_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


