# CommissionadvanceBatchDownloadV1Request

Request for POST /1/object/commissionadvance/{pkiCommissionadvanceID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_batch_download_v1_request import CommissionadvanceBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceBatchDownloadV1Request from a JSON string
commissionadvance_batch_download_v1_request_instance = CommissionadvanceBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceBatchDownloadV1Request.to_json())

# convert the object into a dict
commissionadvance_batch_download_v1_request_dict = commissionadvance_batch_download_v1_request_instance.to_dict()
# create an instance of CommissionadvanceBatchDownloadV1Request from a dict
commissionadvance_batch_download_v1_request_from_dict = CommissionadvanceBatchDownloadV1Request.from_dict(commissionadvance_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


