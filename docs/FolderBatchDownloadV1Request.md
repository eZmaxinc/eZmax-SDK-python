# FolderBatchDownloadV1Request

Request for POST /1/object/folder/{pkiFolderID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.folder_batch_download_v1_request import FolderBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of FolderBatchDownloadV1Request from a JSON string
folder_batch_download_v1_request_instance = FolderBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(FolderBatchDownloadV1Request.to_json())

# convert the object into a dict
folder_batch_download_v1_request_dict = folder_batch_download_v1_request_instance.to_dict()
# create an instance of FolderBatchDownloadV1Request from a dict
folder_batch_download_v1_request_from_dict = FolderBatchDownloadV1Request.from_dict(folder_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


