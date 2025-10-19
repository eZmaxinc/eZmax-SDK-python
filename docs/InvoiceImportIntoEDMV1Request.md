# InvoiceImportIntoEDMV1Request

Request for POST /1/object/invoice/{pkiInvoiceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_import_into_edmv1_request import InvoiceImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceImportIntoEDMV1Request from a JSON string
invoice_import_into_edmv1_request_instance = InvoiceImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(InvoiceImportIntoEDMV1Request.to_json())

# convert the object into a dict
invoice_import_into_edmv1_request_dict = invoice_import_into_edmv1_request_instance.to_dict()
# create an instance of InvoiceImportIntoEDMV1Request from a dict
invoice_import_into_edmv1_request_from_dict = InvoiceImportIntoEDMV1Request.from_dict(invoice_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


