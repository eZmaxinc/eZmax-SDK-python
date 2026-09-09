# EmployeeBatchDownloadV1Request

Request for POST /1/object/employee/{pkiEmployeeID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.employee_batch_download_v1_request import EmployeeBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBatchDownloadV1Request from a JSON string
employee_batch_download_v1_request_instance = EmployeeBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(EmployeeBatchDownloadV1Request.to_json())

# convert the object into a dict
employee_batch_download_v1_request_dict = employee_batch_download_v1_request_instance.to_dict()
# create an instance of EmployeeBatchDownloadV1Request from a dict
employee_batch_download_v1_request_from_dict = EmployeeBatchDownloadV1Request.from_dict(employee_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


