# EzsignfoldersignerassociationCreateObjectV2Response

Response for POST /2/object/ezsignfoldersignerassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationCreateObjectV2ResponseMPayload**](EzsignfoldersignerassociationCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v2_response import EzsignfoldersignerassociationCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV2Response from a JSON string
ezsignfoldersignerassociation_create_object_v2_response_instance = EzsignfoldersignerassociationCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateObjectV2Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v2_response_dict = ezsignfoldersignerassociation_create_object_v2_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV2Response from a dict
ezsignfoldersignerassociation_create_object_v2_response_from_dict = EzsignfoldersignerassociationCreateObjectV2Response.from_dict(ezsignfoldersignerassociation_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


