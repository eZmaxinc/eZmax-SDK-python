# InscriptionnotauthenticatedBatchDownloadV1Request

Request for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_batch_download_v1_request import InscriptionnotauthenticatedBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedBatchDownloadV1Request from a JSON string
inscriptionnotauthenticated_batch_download_v1_request_instance = InscriptionnotauthenticatedBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedBatchDownloadV1Request.to_json())

# convert the object into a dict
inscriptionnotauthenticated_batch_download_v1_request_dict = inscriptionnotauthenticated_batch_download_v1_request_instance.to_dict()
# create an instance of InscriptionnotauthenticatedBatchDownloadV1Request from a dict
inscriptionnotauthenticated_batch_download_v1_request_from_dict = InscriptionnotauthenticatedBatchDownloadV1Request.from_dict(inscriptionnotauthenticated_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


