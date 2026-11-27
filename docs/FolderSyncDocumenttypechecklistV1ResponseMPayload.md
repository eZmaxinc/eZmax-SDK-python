# FolderSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/folder/{pkiFolderID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.folder_sync_documenttypechecklist_v1_response_m_payload import FolderSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FolderSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
folder_sync_documenttypechecklist_v1_response_m_payload_instance = FolderSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(FolderSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
folder_sync_documenttypechecklist_v1_response_m_payload_dict = folder_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of FolderSyncDocumenttypechecklistV1ResponseMPayload from a dict
folder_sync_documenttypechecklist_v1_response_m_payload_from_dict = FolderSyncDocumenttypechecklistV1ResponseMPayload.from_dict(folder_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


