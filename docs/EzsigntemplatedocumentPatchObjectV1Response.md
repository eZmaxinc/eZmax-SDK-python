# EzsigntemplatedocumentPatchObjectV1Response

Response for PATCH /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_patch_object_v1_response import EzsigntemplatedocumentPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentPatchObjectV1Response from a JSON string
ezsigntemplatedocument_patch_object_v1_response_instance = EzsigntemplatedocumentPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentPatchObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_patch_object_v1_response_dict = ezsigntemplatedocument_patch_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentPatchObjectV1Response from a dict
ezsigntemplatedocument_patch_object_v1_response_form_dict = ezsigntemplatedocument_patch_object_v1_response.from_dict(ezsigntemplatedocument_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


