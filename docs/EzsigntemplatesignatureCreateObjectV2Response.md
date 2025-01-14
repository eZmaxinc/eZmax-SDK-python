# EzsigntemplatesignatureCreateObjectV2Response

Response for POST /2/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignatureCreateObjectV2ResponseMPayload**](EzsigntemplatesignatureCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v2_response import EzsigntemplatesignatureCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV2Response from a JSON string
ezsigntemplatesignature_create_object_v2_response_instance = EzsigntemplatesignatureCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureCreateObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatesignature_create_object_v2_response_dict = ezsigntemplatesignature_create_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV2Response from a dict
ezsigntemplatesignature_create_object_v2_response_from_dict = EzsigntemplatesignatureCreateObjectV2Response.from_dict(ezsigntemplatesignature_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


