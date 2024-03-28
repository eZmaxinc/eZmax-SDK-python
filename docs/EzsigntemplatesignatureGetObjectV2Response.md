# EzsigntemplatesignatureGetObjectV2Response

Response for GET /2/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignatureGetObjectV2ResponseMPayload**](EzsigntemplatesignatureGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_get_object_v2_response import EzsigntemplatesignatureGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureGetObjectV2Response from a JSON string
ezsigntemplatesignature_get_object_v2_response_instance = EzsigntemplatesignatureGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatesignature_get_object_v2_response_dict = ezsigntemplatesignature_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureGetObjectV2Response from a dict
ezsigntemplatesignature_get_object_v2_response_form_dict = ezsigntemplatesignature_get_object_v2_response.from_dict(ezsigntemplatesignature_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


