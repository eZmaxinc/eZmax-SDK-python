# EzsignbulksendsignermappingCreateObjectV1Response

Response for POST /1/object/ezsignbulksendsignermapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendsignermappingCreateObjectV1ResponseMPayload**](EzsignbulksendsignermappingCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_response import EzsignbulksendsignermappingCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingCreateObjectV1Response from a JSON string
ezsignbulksendsignermapping_create_object_v1_response_instance = EzsignbulksendsignermappingCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_create_object_v1_response_dict = ezsignbulksendsignermapping_create_object_v1_response_instance.to_dict()
# create an instance of EzsignbulksendsignermappingCreateObjectV1Response from a dict
ezsignbulksendsignermapping_create_object_v1_response_form_dict = ezsignbulksendsignermapping_create_object_v1_response.from_dict(ezsignbulksendsignermapping_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


