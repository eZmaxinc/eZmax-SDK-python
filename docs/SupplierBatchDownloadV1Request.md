# SupplierBatchDownloadV1Request

Request for POST /1/object/supplier/{pkiSupplierID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.supplier_batch_download_v1_request import SupplierBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierBatchDownloadV1Request from a JSON string
supplier_batch_download_v1_request_instance = SupplierBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(SupplierBatchDownloadV1Request.to_json())

# convert the object into a dict
supplier_batch_download_v1_request_dict = supplier_batch_download_v1_request_instance.to_dict()
# create an instance of SupplierBatchDownloadV1Request from a dict
supplier_batch_download_v1_request_from_dict = SupplierBatchDownloadV1Request.from_dict(supplier_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


