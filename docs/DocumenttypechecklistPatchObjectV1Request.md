# DocumenttypechecklistPatchObjectV1Request

Request for PATCH /1/object/documenttypechecklist/{pkiDocumenttypechecklistID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_documenttypechecklist** | [**DocumenttypechecklistRequestPatch**](DocumenttypechecklistRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_patch_object_v1_request import DocumenttypechecklistPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistPatchObjectV1Request from a JSON string
documenttypechecklist_patch_object_v1_request_instance = DocumenttypechecklistPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistPatchObjectV1Request.to_json())

# convert the object into a dict
documenttypechecklist_patch_object_v1_request_dict = documenttypechecklist_patch_object_v1_request_instance.to_dict()
# create an instance of DocumenttypechecklistPatchObjectV1Request from a dict
documenttypechecklist_patch_object_v1_request_from_dict = DocumenttypechecklistPatchObjectV1Request.from_dict(documenttypechecklist_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


