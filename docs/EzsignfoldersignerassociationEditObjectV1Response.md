# EzsignfoldersignerassociationEditObjectV1Response

Response for PUT /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v1_response import EzsignfoldersignerassociationEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationEditObjectV1Response from a JSON string
ezsignfoldersignerassociation_edit_object_v1_response_instance = EzsignfoldersignerassociationEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationEditObjectV1Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_edit_object_v1_response_dict = ezsignfoldersignerassociation_edit_object_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationEditObjectV1Response from a dict
ezsignfoldersignerassociation_edit_object_v1_response_from_dict = EzsignfoldersignerassociationEditObjectV1Response.from_dict(ezsignfoldersignerassociation_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


