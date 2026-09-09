# InvoiceBatchDownloadV1Request

Request for POST /1/object/invoice/{pkiInvoiceID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.invoice_batch_download_v1_request import InvoiceBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceBatchDownloadV1Request from a JSON string
invoice_batch_download_v1_request_instance = InvoiceBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(InvoiceBatchDownloadV1Request.to_json())

# convert the object into a dict
invoice_batch_download_v1_request_dict = invoice_batch_download_v1_request_instance.to_dict()
# create an instance of InvoiceBatchDownloadV1Request from a dict
invoice_batch_download_v1_request_from_dict = InvoiceBatchDownloadV1Request.from_dict(invoice_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


