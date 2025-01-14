# EzsignfoldersignerassociationPatchObjectV1Request

Request for PATCH /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationRequestPatch**](EzsignfoldersignerassociationRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_patch_object_v1_request import EzsignfoldersignerassociationPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationPatchObjectV1Request from a JSON string
ezsignfoldersignerassociation_patch_object_v1_request_instance = EzsignfoldersignerassociationPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationPatchObjectV1Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_patch_object_v1_request_dict = ezsignfoldersignerassociation_patch_object_v1_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationPatchObjectV1Request from a dict
ezsignfoldersignerassociation_patch_object_v1_request_from_dict = EzsignfoldersignerassociationPatchObjectV1Request.from_dict(ezsignfoldersignerassociation_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


