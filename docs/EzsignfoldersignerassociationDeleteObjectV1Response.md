# EzsignfoldersignerassociationDeleteObjectV1Response

Response for DELETE /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_delete_object_v1_response import EzsignfoldersignerassociationDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationDeleteObjectV1Response from a JSON string
ezsignfoldersignerassociation_delete_object_v1_response_instance = EzsignfoldersignerassociationDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_delete_object_v1_response_dict = ezsignfoldersignerassociation_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationDeleteObjectV1Response from a dict
ezsignfoldersignerassociation_delete_object_v1_response_form_dict = ezsignfoldersignerassociation_delete_object_v1_response.from_dict(ezsignfoldersignerassociation_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


