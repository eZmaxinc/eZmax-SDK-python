# EzsignfoldersignerassociationGetObjectV3Response

Response for GET /3/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationGetObjectV3ResponseMPayload**](EzsignfoldersignerassociationGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v3_response import EzsignfoldersignerassociationGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetObjectV3Response from a JSON string
ezsignfoldersignerassociation_get_object_v3_response_instance = EzsignfoldersignerassociationGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationGetObjectV3Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_get_object_v3_response_dict = ezsignfoldersignerassociation_get_object_v3_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetObjectV3Response from a dict
ezsignfoldersignerassociation_get_object_v3_response_from_dict = EzsignfoldersignerassociationGetObjectV3Response.from_dict(ezsignfoldersignerassociation_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


