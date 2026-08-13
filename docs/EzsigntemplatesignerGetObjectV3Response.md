# EzsigntemplatesignerGetObjectV3Response

Response for GET /3/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignerGetObjectV3ResponseMPayload**](EzsigntemplatesignerGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_get_object_v3_response import EzsigntemplatesignerGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerGetObjectV3Response from a JSON string
ezsigntemplatesigner_get_object_v3_response_instance = EzsigntemplatesignerGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerGetObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatesigner_get_object_v3_response_dict = ezsigntemplatesigner_get_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatesignerGetObjectV3Response from a dict
ezsigntemplatesigner_get_object_v3_response_from_dict = EzsigntemplatesignerGetObjectV3Response.from_dict(ezsigntemplatesigner_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


