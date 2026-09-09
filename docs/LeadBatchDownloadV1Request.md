# LeadBatchDownloadV1Request

Request for POST /1/object/lead/{pkiLeadID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.lead_batch_download_v1_request import LeadBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of LeadBatchDownloadV1Request from a JSON string
lead_batch_download_v1_request_instance = LeadBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(LeadBatchDownloadV1Request.to_json())

# convert the object into a dict
lead_batch_download_v1_request_dict = lead_batch_download_v1_request_instance.to_dict()
# create an instance of LeadBatchDownloadV1Request from a dict
lead_batch_download_v1_request_from_dict = LeadBatchDownloadV1Request.from_dict(lead_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


