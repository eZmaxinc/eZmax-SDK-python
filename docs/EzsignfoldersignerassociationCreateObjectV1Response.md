# EzsignfoldersignerassociationCreateObjectV1Response

Response for POST /1/object/ezsignfoldersignerassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationCreateObjectV1ResponseMPayload**](EzsignfoldersignerassociationCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v1_response import EzsignfoldersignerassociationCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV1Response from a JSON string
ezsignfoldersignerassociation_create_object_v1_response_instance = EzsignfoldersignerassociationCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v1_response_dict = ezsignfoldersignerassociation_create_object_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV1Response from a dict
ezsignfoldersignerassociation_create_object_v1_response_from_dict = EzsignfoldersignerassociationCreateObjectV1Response.from_dict(ezsignfoldersignerassociation_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


