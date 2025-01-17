# EzsigndocumentPatchObjectV1Response

Response for PATCH /1/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_patch_object_v1_response import EzsigndocumentPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentPatchObjectV1Response from a JSON string
ezsigndocument_patch_object_v1_response_instance = EzsigndocumentPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentPatchObjectV1Response.to_json())

# convert the object into a dict
ezsigndocument_patch_object_v1_response_dict = ezsigndocument_patch_object_v1_response_instance.to_dict()
# create an instance of EzsigndocumentPatchObjectV1Response from a dict
ezsigndocument_patch_object_v1_response_from_dict = EzsigndocumentPatchObjectV1Response.from_dict(ezsigndocument_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


