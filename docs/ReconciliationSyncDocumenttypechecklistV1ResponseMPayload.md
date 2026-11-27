# ReconciliationSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/reconciliation/{pkiReconciliationID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_sync_documenttypechecklist_v1_response_m_payload import ReconciliationSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
reconciliation_sync_documenttypechecklist_v1_response_m_payload_instance = ReconciliationSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ReconciliationSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
reconciliation_sync_documenttypechecklist_v1_response_m_payload_dict = reconciliation_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of ReconciliationSyncDocumenttypechecklistV1ResponseMPayload from a dict
reconciliation_sync_documenttypechecklist_v1_response_m_payload_from_dict = ReconciliationSyncDocumenttypechecklistV1ResponseMPayload.from_dict(reconciliation_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


