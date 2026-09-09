# InscriptionBatchDownloadV1Request

Request for POST /1/object/inscription/{pkiInscriptionID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.inscription_batch_download_v1_request import InscriptionBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionBatchDownloadV1Request from a JSON string
inscription_batch_download_v1_request_instance = InscriptionBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionBatchDownloadV1Request.to_json())

# convert the object into a dict
inscription_batch_download_v1_request_dict = inscription_batch_download_v1_request_instance.to_dict()
# create an instance of InscriptionBatchDownloadV1Request from a dict
inscription_batch_download_v1_request_from_dict = InscriptionBatchDownloadV1Request.from_dict(inscription_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


