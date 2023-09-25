# EzsigntemplatesignatureCreateObjectV1Response

Response for POST /1/object/ezsigntemplatesignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignatureCreateObjectV1ResponseMPayload**](EzsigntemplatesignatureCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v1_response import EzsigntemplatesignatureCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV1Response from a JSON string
ezsigntemplatesignature_create_object_v1_response_instance = EzsigntemplatesignatureCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignatureCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatesignature_create_object_v1_response_dict = ezsigntemplatesignature_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV1Response from a dict
ezsigntemplatesignature_create_object_v1_response_form_dict = ezsigntemplatesignature_create_object_v1_response.from_dict(ezsigntemplatesignature_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


