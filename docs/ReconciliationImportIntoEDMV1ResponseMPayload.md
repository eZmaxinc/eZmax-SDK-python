# ReconciliationImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/reconciliation/{pkiReconciliationID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_import_into_edmv1_response_m_payload import ReconciliationImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationImportIntoEDMV1ResponseMPayload from a JSON string
reconciliation_import_into_edmv1_response_m_payload_instance = ReconciliationImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ReconciliationImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
reconciliation_import_into_edmv1_response_m_payload_dict = reconciliation_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of ReconciliationImportIntoEDMV1ResponseMPayload from a dict
reconciliation_import_into_edmv1_response_m_payload_from_dict = ReconciliationImportIntoEDMV1ResponseMPayload.from_dict(reconciliation_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


