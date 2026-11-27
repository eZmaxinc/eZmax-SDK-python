# FolderSyncDocumenttypechecklistV1Response

Response for POST /1/object/folder/{pkiFolderID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FolderSyncDocumenttypechecklistV1ResponseMPayload**](FolderSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.folder_sync_documenttypechecklist_v1_response import FolderSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of FolderSyncDocumenttypechecklistV1Response from a JSON string
folder_sync_documenttypechecklist_v1_response_instance = FolderSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(FolderSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
folder_sync_documenttypechecklist_v1_response_dict = folder_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of FolderSyncDocumenttypechecklistV1Response from a dict
folder_sync_documenttypechecklist_v1_response_from_dict = FolderSyncDocumenttypechecklistV1Response.from_dict(folder_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


