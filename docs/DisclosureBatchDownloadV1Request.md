# DisclosureBatchDownloadV1Request

Request for POST /1/object/disclosure/{pkiDisclosureID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.disclosure_batch_download_v1_request import DisclosureBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureBatchDownloadV1Request from a JSON string
disclosure_batch_download_v1_request_instance = DisclosureBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(DisclosureBatchDownloadV1Request.to_json())

# convert the object into a dict
disclosure_batch_download_v1_request_dict = disclosure_batch_download_v1_request_instance.to_dict()
# create an instance of DisclosureBatchDownloadV1Request from a dict
disclosure_batch_download_v1_request_from_dict = DisclosureBatchDownloadV1Request.from_dict(disclosure_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


