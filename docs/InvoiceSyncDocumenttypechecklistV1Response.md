# InvoiceSyncDocumenttypechecklistV1Response

Response for POST /1/object/invoice/{pkiInvoiceID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InvoiceSyncDocumenttypechecklistV1ResponseMPayload**](InvoiceSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_sync_documenttypechecklist_v1_response import InvoiceSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSyncDocumenttypechecklistV1Response from a JSON string
invoice_sync_documenttypechecklist_v1_response_instance = InvoiceSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
invoice_sync_documenttypechecklist_v1_response_dict = invoice_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InvoiceSyncDocumenttypechecklistV1Response from a dict
invoice_sync_documenttypechecklist_v1_response_from_dict = InvoiceSyncDocumenttypechecklistV1Response.from_dict(invoice_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


