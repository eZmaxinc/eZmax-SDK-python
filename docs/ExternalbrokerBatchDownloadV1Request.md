# ExternalbrokerBatchDownloadV1Request

Request for POST /1/object/externalbroker/{pkiExternalbrokerID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.externalbroker_batch_download_v1_request import ExternalbrokerBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerBatchDownloadV1Request from a JSON string
externalbroker_batch_download_v1_request_instance = ExternalbrokerBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerBatchDownloadV1Request.to_json())

# convert the object into a dict
externalbroker_batch_download_v1_request_dict = externalbroker_batch_download_v1_request_instance.to_dict()
# create an instance of ExternalbrokerBatchDownloadV1Request from a dict
externalbroker_batch_download_v1_request_from_dict = ExternalbrokerBatchDownloadV1Request.from_dict(externalbroker_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


