# EzsignsignatureCreateObjectV4Response

Response for POST /4/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignatureCreateObjectV4ResponseMPayload**](EzsignsignatureCreateObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v4_response import EzsignsignatureCreateObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV4Response from a JSON string
ezsignsignature_create_object_v4_response_instance = EzsignsignatureCreateObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV4Response.to_json())

# convert the object into a dict
ezsignsignature_create_object_v4_response_dict = ezsignsignature_create_object_v4_response_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV4Response from a dict
ezsignsignature_create_object_v4_response_from_dict = EzsignsignatureCreateObjectV4Response.from_dict(ezsignsignature_create_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


