# EzsigntemplatepackagesignerGetObjectV3Response

Response for GET /3/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignerGetObjectV3ResponseMPayload**](EzsigntemplatepackagesignerGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v3_response import EzsigntemplatepackagesignerGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerGetObjectV3Response from a JSON string
ezsigntemplatepackagesigner_get_object_v3_response_instance = EzsigntemplatepackagesignerGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerGetObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_get_object_v3_response_dict = ezsigntemplatepackagesigner_get_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerGetObjectV3Response from a dict
ezsigntemplatepackagesigner_get_object_v3_response_from_dict = EzsigntemplatepackagesignerGetObjectV3Response.from_dict(ezsigntemplatepackagesigner_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


