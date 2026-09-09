# ElectronicfundstransferBatchDownloadV1Request

Request for POST /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_batch_download_v1_request import ElectronicfundstransferBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferBatchDownloadV1Request from a JSON string
electronicfundstransfer_batch_download_v1_request_instance = ElectronicfundstransferBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferBatchDownloadV1Request.to_json())

# convert the object into a dict
electronicfundstransfer_batch_download_v1_request_dict = electronicfundstransfer_batch_download_v1_request_instance.to_dict()
# create an instance of ElectronicfundstransferBatchDownloadV1Request from a dict
electronicfundstransfer_batch_download_v1_request_from_dict = ElectronicfundstransferBatchDownloadV1Request.from_dict(electronicfundstransfer_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


