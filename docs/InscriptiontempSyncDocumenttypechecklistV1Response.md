# InscriptiontempSyncDocumenttypechecklistV1Response

Response for POST /1/object/inscriptiontemp/{pkiInscriptiontempID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload**](InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_sync_documenttypechecklist_v1_response import InscriptiontempSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempSyncDocumenttypechecklistV1Response from a JSON string
inscriptiontemp_sync_documenttypechecklist_v1_response_instance = InscriptiontempSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
inscriptiontemp_sync_documenttypechecklist_v1_response_dict = inscriptiontemp_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InscriptiontempSyncDocumenttypechecklistV1Response from a dict
inscriptiontemp_sync_documenttypechecklist_v1_response_from_dict = InscriptiontempSyncDocumenttypechecklistV1Response.from_dict(inscriptiontemp_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


