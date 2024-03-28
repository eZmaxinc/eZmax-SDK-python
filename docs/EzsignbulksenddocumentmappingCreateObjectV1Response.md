# EzsignbulksenddocumentmappingCreateObjectV1Response

Response for POST /1/object/ezsignbulksenddocumentmapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksenddocumentmappingCreateObjectV1ResponseMPayload**](EzsignbulksenddocumentmappingCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_create_object_v1_response import EzsignbulksenddocumentmappingCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingCreateObjectV1Response from a JSON string
ezsignbulksenddocumentmapping_create_object_v1_response_instance = EzsignbulksenddocumentmappingCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_create_object_v1_response_dict = ezsignbulksenddocumentmapping_create_object_v1_response_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingCreateObjectV1Response from a dict
ezsignbulksenddocumentmapping_create_object_v1_response_form_dict = ezsignbulksenddocumentmapping_create_object_v1_response.from_dict(ezsignbulksenddocumentmapping_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


