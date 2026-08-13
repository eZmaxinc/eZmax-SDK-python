# EzsignbulksendsignermappingCreateObjectV2Response

Response for POST /2/object/ezsignbulksendsignermapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendsignermappingCreateObjectV2ResponseMPayload**](EzsignbulksendsignermappingCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v2_response import EzsignbulksendsignermappingCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingCreateObjectV2Response from a JSON string
ezsignbulksendsignermapping_create_object_v2_response_instance = EzsignbulksendsignermappingCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingCreateObjectV2Response.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_create_object_v2_response_dict = ezsignbulksendsignermapping_create_object_v2_response_instance.to_dict()
# create an instance of EzsignbulksendsignermappingCreateObjectV2Response from a dict
ezsignbulksendsignermapping_create_object_v2_response_from_dict = EzsignbulksendsignermappingCreateObjectV2Response.from_dict(ezsignbulksendsignermapping_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


