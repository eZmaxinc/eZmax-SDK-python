# InscriptiontempBatchDownloadV1Request

Request for POST /1/object/inscriptiontemp/{pkiInscriptiontempID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_batch_download_v1_request import InscriptiontempBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempBatchDownloadV1Request from a JSON string
inscriptiontemp_batch_download_v1_request_instance = InscriptiontempBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempBatchDownloadV1Request.to_json())

# convert the object into a dict
inscriptiontemp_batch_download_v1_request_dict = inscriptiontemp_batch_download_v1_request_instance.to_dict()
# create an instance of InscriptiontempBatchDownloadV1Request from a dict
inscriptiontemp_batch_download_v1_request_from_dict = InscriptiontempBatchDownloadV1Request.from_dict(inscriptiontemp_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


