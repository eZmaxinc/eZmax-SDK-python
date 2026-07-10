# EzsignfoldersignerassociationCreateObjectV3Response

Response for POST /2/object/ezsignfoldersignerassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationCreateObjectV3ResponseMPayload**](EzsignfoldersignerassociationCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v3_response import EzsignfoldersignerassociationCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV3Response from a JSON string
ezsignfoldersignerassociation_create_object_v3_response_instance = EzsignfoldersignerassociationCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateObjectV3Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v3_response_dict = ezsignfoldersignerassociation_create_object_v3_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV3Response from a dict
ezsignfoldersignerassociation_create_object_v3_response_from_dict = EzsignfoldersignerassociationCreateObjectV3Response.from_dict(ezsignfoldersignerassociation_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


