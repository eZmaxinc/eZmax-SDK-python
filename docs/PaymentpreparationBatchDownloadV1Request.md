# PaymentpreparationBatchDownloadV1Request

Request for POST /1/object/paymentpreparation/{pkiPaymentpreparationID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_batch_download_v1_request import PaymentpreparationBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationBatchDownloadV1Request from a JSON string
paymentpreparation_batch_download_v1_request_instance = PaymentpreparationBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationBatchDownloadV1Request.to_json())

# convert the object into a dict
paymentpreparation_batch_download_v1_request_dict = paymentpreparation_batch_download_v1_request_instance.to_dict()
# create an instance of PaymentpreparationBatchDownloadV1Request from a dict
paymentpreparation_batch_download_v1_request_from_dict = PaymentpreparationBatchDownloadV1Request.from_dict(paymentpreparation_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


