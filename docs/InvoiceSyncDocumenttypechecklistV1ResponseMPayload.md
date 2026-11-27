# InvoiceSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/invoice/{pkiInvoiceID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_sync_documenttypechecklist_v1_response_m_payload import InvoiceSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
invoice_sync_documenttypechecklist_v1_response_m_payload_instance = InvoiceSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InvoiceSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
invoice_sync_documenttypechecklist_v1_response_m_payload_dict = invoice_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of InvoiceSyncDocumenttypechecklistV1ResponseMPayload from a dict
invoice_sync_documenttypechecklist_v1_response_m_payload_from_dict = InvoiceSyncDocumenttypechecklistV1ResponseMPayload.from_dict(invoice_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


