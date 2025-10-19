# EzsigntemplatesignatureCreateObjectV3Response

Response for POST /3/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignatureCreateObjectV3ResponseMPayload**](EzsigntemplatesignatureCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v3_response import EzsigntemplatesignatureCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV3Response from a JSON string
ezsigntemplatesignature_create_object_v3_response_instance = EzsigntemplatesignatureCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureCreateObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatesignature_create_object_v3_response_dict = ezsigntemplatesignature_create_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV3Response from a dict
ezsigntemplatesignature_create_object_v3_response_from_dict = EzsigntemplatesignatureCreateObjectV3Response.from_dict(ezsigntemplatesignature_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


