# EzsignfolderBatchDownloadV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigndocument_id** | **List[int]** |  | 
**a_e_document_type** | **List[str]** | The type of document to retrieve.  1. **Signed** Is the final document once all signatures were applied. 2. **Proofdocument** Is the evidence report. 3. **Proof** Is the complete evidence archive including all of the above and more. | 

## Example

```python
from eZmaxApi.models.ezsignfolder_batch_download_v1_request import EzsignfolderBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderBatchDownloadV1Request from a JSON string
ezsignfolder_batch_download_v1_request_instance = EzsignfolderBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderBatchDownloadV1Request.to_json()

# convert the object into a dict
ezsignfolder_batch_download_v1_request_dict = ezsignfolder_batch_download_v1_request_instance.to_dict()
# create an instance of EzsignfolderBatchDownloadV1Request from a dict
ezsignfolder_batch_download_v1_request_form_dict = ezsignfolder_batch_download_v1_request.from_dict(ezsignfolder_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


