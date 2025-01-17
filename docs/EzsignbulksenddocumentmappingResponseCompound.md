# EzsignbulksenddocumentmappingResponseCompound

A Ezsignbulksenddocumentmapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompound**](EzsigntemplateResponseCompound.md) |  | [optional] 
**obj_ezsigntemplatepackage** | [**EzsigntemplatepackageResponseCompound**](EzsigntemplatepackageResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_response_compound import EzsignbulksenddocumentmappingResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingResponseCompound from a JSON string
ezsignbulksenddocumentmapping_response_compound_instance = EzsignbulksenddocumentmappingResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingResponseCompound.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_response_compound_dict = ezsignbulksenddocumentmapping_response_compound_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingResponseCompound from a dict
ezsignbulksenddocumentmapping_response_compound_from_dict = EzsignbulksenddocumentmappingResponseCompound.from_dict(ezsignbulksenddocumentmapping_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


