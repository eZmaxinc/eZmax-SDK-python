# InvoiceImportIntoEDMV1Response

Response for POST /1/object/invoice/{pkiInvoiceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InvoiceImportIntoEDMV1ResponseMPayload**](InvoiceImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_import_into_edmv1_response import InvoiceImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceImportIntoEDMV1Response from a JSON string
invoice_import_into_edmv1_response_instance = InvoiceImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceImportIntoEDMV1Response.to_json())

# convert the object into a dict
invoice_import_into_edmv1_response_dict = invoice_import_into_edmv1_response_instance.to_dict()
# create an instance of InvoiceImportIntoEDMV1Response from a dict
invoice_import_into_edmv1_response_from_dict = InvoiceImportIntoEDMV1Response.from_dict(invoice_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


