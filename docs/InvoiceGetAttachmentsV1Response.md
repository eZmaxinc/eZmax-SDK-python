# InvoiceGetAttachmentsV1Response

Response for GET /1/object/invoice/{pkiInvoiceID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InvoiceGetAttachmentsV1ResponseMPayload**](InvoiceGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_attachments_v1_response import InvoiceGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetAttachmentsV1Response from a JSON string
invoice_get_attachments_v1_response_instance = InvoiceGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetAttachmentsV1Response.to_json())

# convert the object into a dict
invoice_get_attachments_v1_response_dict = invoice_get_attachments_v1_response_instance.to_dict()
# create an instance of InvoiceGetAttachmentsV1Response from a dict
invoice_get_attachments_v1_response_form_dict = invoice_get_attachments_v1_response.from_dict(invoice_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


