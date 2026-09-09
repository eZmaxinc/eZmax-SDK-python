# OtherincomeBatchDownloadV1Request

Request for POST /1/object/otherincome/{pkiOtherincomeID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.otherincome_batch_download_v1_request import OtherincomeBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeBatchDownloadV1Request from a JSON string
otherincome_batch_download_v1_request_instance = OtherincomeBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(OtherincomeBatchDownloadV1Request.to_json())

# convert the object into a dict
otherincome_batch_download_v1_request_dict = otherincome_batch_download_v1_request_instance.to_dict()
# create an instance of OtherincomeBatchDownloadV1Request from a dict
otherincome_batch_download_v1_request_from_dict = OtherincomeBatchDownloadV1Request.from_dict(otherincome_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


