# BuyercontractBatchDownloadV1Request

Request for POST /1/object/buyercontract/{pkiBuyercontractID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.buyercontract_batch_download_v1_request import BuyercontractBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractBatchDownloadV1Request from a JSON string
buyercontract_batch_download_v1_request_instance = BuyercontractBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(BuyercontractBatchDownloadV1Request.to_json())

# convert the object into a dict
buyercontract_batch_download_v1_request_dict = buyercontract_batch_download_v1_request_instance.to_dict()
# create an instance of BuyercontractBatchDownloadV1Request from a dict
buyercontract_batch_download_v1_request_from_dict = BuyercontractBatchDownloadV1Request.from_dict(buyercontract_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


