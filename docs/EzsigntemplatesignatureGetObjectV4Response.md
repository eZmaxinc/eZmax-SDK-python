# EzsigntemplatesignatureGetObjectV4Response

Response for GET /4/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignatureGetObjectV4ResponseMPayload**](EzsigntemplatesignatureGetObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_get_object_v4_response import EzsigntemplatesignatureGetObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureGetObjectV4Response from a JSON string
ezsigntemplatesignature_get_object_v4_response_instance = EzsigntemplatesignatureGetObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureGetObjectV4Response.to_json())

# convert the object into a dict
ezsigntemplatesignature_get_object_v4_response_dict = ezsigntemplatesignature_get_object_v4_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureGetObjectV4Response from a dict
ezsigntemplatesignature_get_object_v4_response_from_dict = EzsigntemplatesignatureGetObjectV4Response.from_dict(ezsigntemplatesignature_get_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


