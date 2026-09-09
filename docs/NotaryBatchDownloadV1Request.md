# NotaryBatchDownloadV1Request

Request for POST /1/object/notary/{pkiNotaryID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.notary_batch_download_v1_request import NotaryBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryBatchDownloadV1Request from a JSON string
notary_batch_download_v1_request_instance = NotaryBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(NotaryBatchDownloadV1Request.to_json())

# convert the object into a dict
notary_batch_download_v1_request_dict = notary_batch_download_v1_request_instance.to_dict()
# create an instance of NotaryBatchDownloadV1Request from a dict
notary_batch_download_v1_request_from_dict = NotaryBatchDownloadV1Request.from_dict(notary_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


