# EzsignfolderSyncDocumenttypechecklistV1Response

Response for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload**](EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_sync_documenttypechecklist_v1_response import EzsignfolderSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSyncDocumenttypechecklistV1Response from a JSON string
ezsignfolder_sync_documenttypechecklist_v1_response_instance = EzsignfolderSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
ezsignfolder_sync_documenttypechecklist_v1_response_dict = ezsignfolder_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of EzsignfolderSyncDocumenttypechecklistV1Response from a dict
ezsignfolder_sync_documenttypechecklist_v1_response_from_dict = EzsignfolderSyncDocumenttypechecklistV1Response.from_dict(ezsignfolder_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


