# CustomerBatchDownloadV1Request

Request for POST /1/object/customer/{pkiCustomerID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.customer_batch_download_v1_request import CustomerBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerBatchDownloadV1Request from a JSON string
customer_batch_download_v1_request_instance = CustomerBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(CustomerBatchDownloadV1Request.to_json())

# convert the object into a dict
customer_batch_download_v1_request_dict = customer_batch_download_v1_request_instance.to_dict()
# create an instance of CustomerBatchDownloadV1Request from a dict
customer_batch_download_v1_request_from_dict = CustomerBatchDownloadV1Request.from_dict(customer_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


