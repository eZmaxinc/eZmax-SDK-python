# ReconciliationGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/reconciliation/{pkiReconciliationID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_get_documenttypechecklist_v1_response_m_payload import ReconciliationGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationGetDocumenttypechecklistV1ResponseMPayload from a JSON string
reconciliation_get_documenttypechecklist_v1_response_m_payload_instance = ReconciliationGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ReconciliationGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
reconciliation_get_documenttypechecklist_v1_response_m_payload_dict = reconciliation_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of ReconciliationGetDocumenttypechecklistV1ResponseMPayload from a dict
reconciliation_get_documenttypechecklist_v1_response_m_payload_from_dict = ReconciliationGetDocumenttypechecklistV1ResponseMPayload.from_dict(reconciliation_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


