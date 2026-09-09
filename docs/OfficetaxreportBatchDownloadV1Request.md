# OfficetaxreportBatchDownloadV1Request

Request for POST /1/object/officetaxreport/{pkiOfficetaxreportID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_batch_download_v1_request import OfficetaxreportBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportBatchDownloadV1Request from a JSON string
officetaxreport_batch_download_v1_request_instance = OfficetaxreportBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportBatchDownloadV1Request.to_json())

# convert the object into a dict
officetaxreport_batch_download_v1_request_dict = officetaxreport_batch_download_v1_request_instance.to_dict()
# create an instance of OfficetaxreportBatchDownloadV1Request from a dict
officetaxreport_batch_download_v1_request_from_dict = OfficetaxreportBatchDownloadV1Request.from_dict(officetaxreport_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


