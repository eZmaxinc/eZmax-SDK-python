# EzsignannotationGetObjectV2Response

Response for GET /2/object/ezsignannotation/{pkiEzsignannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignannotationGetObjectV2ResponseMPayload**](EzsignannotationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignannotation_get_object_v2_response import EzsignannotationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationGetObjectV2Response from a JSON string
ezsignannotation_get_object_v2_response_instance = EzsignannotationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationGetObjectV2Response.to_json())

# convert the object into a dict
ezsignannotation_get_object_v2_response_dict = ezsignannotation_get_object_v2_response_instance.to_dict()
# create an instance of EzsignannotationGetObjectV2Response from a dict
ezsignannotation_get_object_v2_response_from_dict = EzsignannotationGetObjectV2Response.from_dict(ezsignannotation_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


