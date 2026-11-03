# DocumenttypechecklistRequestPatch

A Documenttypechecklist Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_documenttypechecklist_status** | [**FieldEDocumenttypechecklistStatus**](FieldEDocumenttypechecklistStatus.md) |  | [optional] 
**t_documenttypechecklist_comment** | **str** | The comment of the Documenttypechecklist | [optional] 

## Example

```python
from eZmaxApi.models.documenttypechecklist_request_patch import DocumenttypechecklistRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistRequestPatch from a JSON string
documenttypechecklist_request_patch_instance = DocumenttypechecklistRequestPatch.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistRequestPatch.to_json())

# convert the object into a dict
documenttypechecklist_request_patch_dict = documenttypechecklist_request_patch_instance.to_dict()
# create an instance of DocumenttypechecklistRequestPatch from a dict
documenttypechecklist_request_patch_from_dict = DocumenttypechecklistRequestPatch.from_dict(documenttypechecklist_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


