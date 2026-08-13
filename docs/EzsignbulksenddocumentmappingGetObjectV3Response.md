# EzsignbulksenddocumentmappingGetObjectV3Response

Response for GET /3/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload**](EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_get_object_v3_response import EzsignbulksenddocumentmappingGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingGetObjectV3Response from a JSON string
ezsignbulksenddocumentmapping_get_object_v3_response_instance = EzsignbulksenddocumentmappingGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingGetObjectV3Response.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_get_object_v3_response_dict = ezsignbulksenddocumentmapping_get_object_v3_response_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingGetObjectV3Response from a dict
ezsignbulksenddocumentmapping_get_object_v3_response_from_dict = EzsignbulksenddocumentmappingGetObjectV3Response.from_dict(ezsignbulksenddocumentmapping_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


