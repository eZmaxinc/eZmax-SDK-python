# EzsigntemplatesignerGetObjectV2Response

Response for GET /2/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignerGetObjectV2ResponseMPayload**](EzsigntemplatesignerGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_get_object_v2_response import EzsigntemplatesignerGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerGetObjectV2Response from a JSON string
ezsigntemplatesigner_get_object_v2_response_instance = EzsigntemplatesignerGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatesigner_get_object_v2_response_dict = ezsigntemplatesigner_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatesignerGetObjectV2Response from a dict
ezsigntemplatesigner_get_object_v2_response_from_dict = EzsigntemplatesignerGetObjectV2Response.from_dict(ezsigntemplatesigner_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


