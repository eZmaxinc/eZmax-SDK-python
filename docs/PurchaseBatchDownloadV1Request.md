# PurchaseBatchDownloadV1Request

Request for POST /1/object/purchase/{pkiPurchaseID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.purchase_batch_download_v1_request import PurchaseBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseBatchDownloadV1Request from a JSON string
purchase_batch_download_v1_request_instance = PurchaseBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(PurchaseBatchDownloadV1Request.to_json())

# convert the object into a dict
purchase_batch_download_v1_request_dict = purchase_batch_download_v1_request_instance.to_dict()
# create an instance of PurchaseBatchDownloadV1Request from a dict
purchase_batch_download_v1_request_from_dict = PurchaseBatchDownloadV1Request.from_dict(purchase_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


