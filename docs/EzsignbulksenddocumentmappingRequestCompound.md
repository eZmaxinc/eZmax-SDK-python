# EzsignbulksenddocumentmappingRequestCompound

A Ezsignbulksenddocumentmapping Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksenddocumentmapping_id** | **int** | The unique ID of the Ezsignbulksenddocumentmapping. | [optional] 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_request_compound import EzsignbulksenddocumentmappingRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingRequestCompound from a JSON string
ezsignbulksenddocumentmapping_request_compound_instance = EzsignbulksenddocumentmappingRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsignbulksenddocumentmappingRequestCompound.to_json()

# convert the object into a dict
ezsignbulksenddocumentmapping_request_compound_dict = ezsignbulksenddocumentmapping_request_compound_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingRequestCompound from a dict
ezsignbulksenddocumentmapping_request_compound_form_dict = ezsignbulksenddocumentmapping_request_compound.from_dict(ezsignbulksenddocumentmapping_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


