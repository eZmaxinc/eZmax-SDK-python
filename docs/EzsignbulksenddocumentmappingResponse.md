# EzsignbulksenddocumentmappingResponse

A Ezsignbulksenddocumentmapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksenddocumentmapping_id** | **int** | The unique ID of the Ezsignbulksenddocumentmapping. | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**i_ezsignbulksenddocumentmapping_order** | **int** | The order in which the Ezsigntemplate or Ezsigntemplatepackage will be presented to the signatory in the Ezsignfolder. | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_response import EzsignbulksenddocumentmappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingResponse from a JSON string
ezsignbulksenddocumentmapping_response_instance = EzsignbulksenddocumentmappingResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingResponse.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_response_dict = ezsignbulksenddocumentmapping_response_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingResponse from a dict
ezsignbulksenddocumentmapping_response_from_dict = EzsignbulksenddocumentmappingResponse.from_dict(ezsignbulksenddocumentmapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


