# BrokerBatchDownloadV1Request

Request for POST /1/object/broker/{pkiBrokerID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.broker_batch_download_v1_request import BrokerBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerBatchDownloadV1Request from a JSON string
broker_batch_download_v1_request_instance = BrokerBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(BrokerBatchDownloadV1Request.to_json())

# convert the object into a dict
broker_batch_download_v1_request_dict = broker_batch_download_v1_request_instance.to_dict()
# create an instance of BrokerBatchDownloadV1Request from a dict
broker_batch_download_v1_request_from_dict = BrokerBatchDownloadV1Request.from_dict(broker_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


