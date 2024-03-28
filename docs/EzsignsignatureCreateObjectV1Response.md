# EzsignsignatureCreateObjectV1Response

Response for POST /1/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignatureCreateObjectV1ResponseMPayload**](EzsignsignatureCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v1_response import EzsignsignatureCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV1Response from a JSON string
ezsignsignature_create_object_v1_response_instance = EzsignsignatureCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignsignature_create_object_v1_response_dict = ezsignsignature_create_object_v1_response_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV1Response from a dict
ezsignsignature_create_object_v1_response_form_dict = ezsignsignature_create_object_v1_response.from_dict(ezsignsignature_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


