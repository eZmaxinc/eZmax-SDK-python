# EzsigntemplatedocumentPatchObjectV1Request

Request for PATCH /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentRequestPatch**](EzsigntemplatedocumentRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_patch_object_v1_request import EzsigntemplatedocumentPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentPatchObjectV1Request from a JSON string
ezsigntemplatedocument_patch_object_v1_request_instance = EzsigntemplatedocumentPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentPatchObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_patch_object_v1_request_dict = ezsigntemplatedocument_patch_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentPatchObjectV1Request from a dict
ezsigntemplatedocument_patch_object_v1_request_form_dict = ezsigntemplatedocument_patch_object_v1_request.from_dict(ezsigntemplatedocument_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


