# EzsignbulksenddocumentmappingRequest

A Ezsignbulksenddocumentmapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksenddocumentmapping_id** | **int** | The unique ID of the Ezsignbulksenddocumentmapping. | [optional] 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_request import EzsignbulksenddocumentmappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingRequest from a JSON string
ezsignbulksenddocumentmapping_request_instance = EzsignbulksenddocumentmappingRequest.from_json(json)
# print the JSON string representation of the object
print EzsignbulksenddocumentmappingRequest.to_json()

# convert the object into a dict
ezsignbulksenddocumentmapping_request_dict = ezsignbulksenddocumentmapping_request_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingRequest from a dict
ezsignbulksenddocumentmapping_request_form_dict = ezsignbulksenddocumentmapping_request.from_dict(ezsignbulksenddocumentmapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


