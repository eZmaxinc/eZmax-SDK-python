# EzsigntemplatepackagesignerDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignerDeleteObjectV1ResponseMPayload**](EzsigntemplatepackagesignerDeleteObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_delete_object_v1_response import EzsigntemplatepackagesignerDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerDeleteObjectV1Response from a JSON string
ezsigntemplatepackagesigner_delete_object_v1_response_instance = EzsigntemplatepackagesignerDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_delete_object_v1_response_dict = ezsigntemplatepackagesigner_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerDeleteObjectV1Response from a dict
ezsigntemplatepackagesigner_delete_object_v1_response_from_dict = EzsigntemplatepackagesignerDeleteObjectV1Response.from_dict(ezsigntemplatepackagesigner_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


