# EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_sync_documenttypechecklist_v1_response_m_payload import EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
ezsignfolder_sync_documenttypechecklist_v1_response_m_payload_instance = EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_sync_documenttypechecklist_v1_response_m_payload_dict = ezsignfolder_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload from a dict
ezsignfolder_sync_documenttypechecklist_v1_response_m_payload_from_dict = EzsignfolderSyncDocumenttypechecklistV1ResponseMPayload.from_dict(ezsignfolder_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


