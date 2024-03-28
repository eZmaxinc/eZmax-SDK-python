# EzsigndocumentPatchObjectV1Request

Request for PATCH /1/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentRequestPatch**](EzsigndocumentRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_patch_object_v1_request import EzsigndocumentPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentPatchObjectV1Request from a JSON string
ezsigndocument_patch_object_v1_request_instance = EzsigndocumentPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentPatchObjectV1Request.to_json())

# convert the object into a dict
ezsigndocument_patch_object_v1_request_dict = ezsigndocument_patch_object_v1_request_instance.to_dict()
# create an instance of EzsigndocumentPatchObjectV1Request from a dict
ezsigndocument_patch_object_v1_request_form_dict = ezsigndocument_patch_object_v1_request.from_dict(ezsigndocument_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


