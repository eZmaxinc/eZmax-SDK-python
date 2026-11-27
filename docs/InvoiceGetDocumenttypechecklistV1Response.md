# InvoiceGetDocumenttypechecklistV1Response

Response for GET /1/object/invoice/{pkiInvoiceID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InvoiceGetDocumenttypechecklistV1ResponseMPayload**](InvoiceGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_documenttypechecklist_v1_response import InvoiceGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetDocumenttypechecklistV1Response from a JSON string
invoice_get_documenttypechecklist_v1_response_instance = InvoiceGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
invoice_get_documenttypechecklist_v1_response_dict = invoice_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InvoiceGetDocumenttypechecklistV1Response from a dict
invoice_get_documenttypechecklist_v1_response_from_dict = InvoiceGetDocumenttypechecklistV1Response.from_dict(invoice_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


