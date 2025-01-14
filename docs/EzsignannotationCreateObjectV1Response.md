# EzsignannotationCreateObjectV1Response

Response for POST /1/object/ezsignannotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignannotationCreateObjectV1ResponseMPayload**](EzsignannotationCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignannotation_create_object_v1_response import EzsignannotationCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationCreateObjectV1Response from a JSON string
ezsignannotation_create_object_v1_response_instance = EzsignannotationCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignannotation_create_object_v1_response_dict = ezsignannotation_create_object_v1_response_instance.to_dict()
# create an instance of EzsignannotationCreateObjectV1Response from a dict
ezsignannotation_create_object_v1_response_from_dict = EzsignannotationCreateObjectV1Response.from_dict(ezsignannotation_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


