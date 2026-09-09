# DeposittransitchequeBatchDownloadV1Request

Request for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_batch_download_v1_request import DeposittransitchequeBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeBatchDownloadV1Request from a JSON string
deposittransitcheque_batch_download_v1_request_instance = DeposittransitchequeBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeBatchDownloadV1Request.to_json())

# convert the object into a dict
deposittransitcheque_batch_download_v1_request_dict = deposittransitcheque_batch_download_v1_request_instance.to_dict()
# create an instance of DeposittransitchequeBatchDownloadV1Request from a dict
deposittransitcheque_batch_download_v1_request_from_dict = DeposittransitchequeBatchDownloadV1Request.from_dict(deposittransitcheque_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


