# BankaccountBatchDownloadV1Request

Request for POST /1/object/bankaccount/{pkiBankaccountID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.bankaccount_batch_download_v1_request import BankaccountBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountBatchDownloadV1Request from a JSON string
bankaccount_batch_download_v1_request_instance = BankaccountBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(BankaccountBatchDownloadV1Request.to_json())

# convert the object into a dict
bankaccount_batch_download_v1_request_dict = bankaccount_batch_download_v1_request_instance.to_dict()
# create an instance of BankaccountBatchDownloadV1Request from a dict
bankaccount_batch_download_v1_request_from_dict = BankaccountBatchDownloadV1Request.from_dict(bankaccount_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


