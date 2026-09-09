# SalaryBatchDownloadV1Request

Request for POST /1/object/salary/{pkiSalaryID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.salary_batch_download_v1_request import SalaryBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryBatchDownloadV1Request from a JSON string
salary_batch_download_v1_request_instance = SalaryBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(SalaryBatchDownloadV1Request.to_json())

# convert the object into a dict
salary_batch_download_v1_request_dict = salary_batch_download_v1_request_instance.to_dict()
# create an instance of SalaryBatchDownloadV1Request from a dict
salary_batch_download_v1_request_from_dict = SalaryBatchDownloadV1Request.from_dict(salary_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


