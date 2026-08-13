# EzsigntemplatepackagesignerCreateObjectV2Response

Response for POST /2/object/ezsigntemplatepackagesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload**](EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v2_response import EzsigntemplatepackagesignerCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerCreateObjectV2Response from a JSON string
ezsigntemplatepackagesigner_create_object_v2_response_instance = EzsigntemplatepackagesignerCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerCreateObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_create_object_v2_response_dict = ezsigntemplatepackagesigner_create_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerCreateObjectV2Response from a dict
ezsigntemplatepackagesigner_create_object_v2_response_from_dict = EzsigntemplatepackagesignerCreateObjectV2Response.from_dict(ezsigntemplatepackagesigner_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


