# EzsignbulksendCreateObjectV1Response

Response for POST /1/object/ezsignbulksend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendCreateObjectV1ResponseMPayload**](EzsignbulksendCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_object_v1_response import EzsignbulksendCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateObjectV1Response from a JSON string
ezsignbulksend_create_object_v1_response_instance = EzsignbulksendCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignbulksend_create_object_v1_response_dict = ezsignbulksend_create_object_v1_response_instance.to_dict()
# create an instance of EzsignbulksendCreateObjectV1Response from a dict
ezsignbulksend_create_object_v1_response_from_dict = EzsignbulksendCreateObjectV1Response.from_dict(ezsignbulksend_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


