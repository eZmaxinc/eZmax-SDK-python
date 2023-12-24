# EzsignbulksenddocumentmappingCreateObjectV1Request

Request for POST /1/object/ezsignbulksenddocumentmapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksenddocumentmapping** | [**List[EzsignbulksenddocumentmappingRequestCompound]**](EzsignbulksenddocumentmappingRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_create_object_v1_request import EzsignbulksenddocumentmappingCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingCreateObjectV1Request from a JSON string
ezsignbulksenddocumentmapping_create_object_v1_request_instance = EzsignbulksenddocumentmappingCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignbulksenddocumentmappingCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignbulksenddocumentmapping_create_object_v1_request_dict = ezsignbulksenddocumentmapping_create_object_v1_request_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingCreateObjectV1Request from a dict
ezsignbulksenddocumentmapping_create_object_v1_request_form_dict = ezsignbulksenddocumentmapping_create_object_v1_request.from_dict(ezsignbulksenddocumentmapping_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


