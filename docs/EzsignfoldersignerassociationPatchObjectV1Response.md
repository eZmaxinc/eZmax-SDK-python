# EzsignfoldersignerassociationPatchObjectV1Response

Response for PATCH /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_patch_object_v1_response import EzsignfoldersignerassociationPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationPatchObjectV1Response from a JSON string
ezsignfoldersignerassociation_patch_object_v1_response_instance = EzsignfoldersignerassociationPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationPatchObjectV1Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_patch_object_v1_response_dict = ezsignfoldersignerassociation_patch_object_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationPatchObjectV1Response from a dict
ezsignfoldersignerassociation_patch_object_v1_response_from_dict = EzsignfoldersignerassociationPatchObjectV1Response.from_dict(ezsignfoldersignerassociation_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


