# DepositBatchDownloadV1Request

Request for POST /1/object/deposit/{pkiDepositID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.deposit_batch_download_v1_request import DepositBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DepositBatchDownloadV1Request from a JSON string
deposit_batch_download_v1_request_instance = DepositBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(DepositBatchDownloadV1Request.to_json())

# convert the object into a dict
deposit_batch_download_v1_request_dict = deposit_batch_download_v1_request_instance.to_dict()
# create an instance of DepositBatchDownloadV1Request from a dict
deposit_batch_download_v1_request_from_dict = DepositBatchDownloadV1Request.from_dict(deposit_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


