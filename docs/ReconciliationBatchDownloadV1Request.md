# ReconciliationBatchDownloadV1Request

Request for POST /1/object/reconciliation/{pkiReconciliationID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.reconciliation_batch_download_v1_request import ReconciliationBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationBatchDownloadV1Request from a JSON string
reconciliation_batch_download_v1_request_instance = ReconciliationBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(ReconciliationBatchDownloadV1Request.to_json())

# convert the object into a dict
reconciliation_batch_download_v1_request_dict = reconciliation_batch_download_v1_request_instance.to_dict()
# create an instance of ReconciliationBatchDownloadV1Request from a dict
reconciliation_batch_download_v1_request_from_dict = ReconciliationBatchDownloadV1Request.from_dict(reconciliation_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


