# EzsigntemplateglobalannotationGetObjectV2Response

Response for GET /2/object/ezsigntemplateglobalannotation/{pkiEzsigntemplateglobalannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateglobalannotationGetObjectV2ResponseMPayload**](EzsigntemplateglobalannotationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobalannotation_get_object_v2_response import EzsigntemplateglobalannotationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalannotationGetObjectV2Response from a JSON string
ezsigntemplateglobalannotation_get_object_v2_response_instance = EzsigntemplateglobalannotationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalannotationGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplateglobalannotation_get_object_v2_response_dict = ezsigntemplateglobalannotation_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplateglobalannotationGetObjectV2Response from a dict
ezsigntemplateglobalannotation_get_object_v2_response_from_dict = EzsigntemplateglobalannotationGetObjectV2Response.from_dict(ezsigntemplateglobalannotation_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


