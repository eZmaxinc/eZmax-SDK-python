# InvoiceImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/invoice/{pkiInvoiceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.invoice_import_into_edmv1_response_m_payload import InvoiceImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceImportIntoEDMV1ResponseMPayload from a JSON string
invoice_import_into_edmv1_response_m_payload_instance = InvoiceImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InvoiceImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
invoice_import_into_edmv1_response_m_payload_dict = invoice_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of InvoiceImportIntoEDMV1ResponseMPayload from a dict
invoice_import_into_edmv1_response_m_payload_from_dict = InvoiceImportIntoEDMV1ResponseMPayload.from_dict(invoice_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


