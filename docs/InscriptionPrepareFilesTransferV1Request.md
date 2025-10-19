# InscriptionPrepareFilesTransferV1Request

Request for POST /1/object/inscription/{pkiInscriptionID}/prepareFilesTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentPrepareFilesTransferRequest]**](CustomAttachmentPrepareFilesTransferRequest.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_prepare_files_transfer_v1_request import InscriptionPrepareFilesTransferV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionPrepareFilesTransferV1Request from a JSON string
inscription_prepare_files_transfer_v1_request_instance = InscriptionPrepareFilesTransferV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionPrepareFilesTransferV1Request.to_json())

# convert the object into a dict
inscription_prepare_files_transfer_v1_request_dict = inscription_prepare_files_transfer_v1_request_instance.to_dict()
# create an instance of InscriptionPrepareFilesTransferV1Request from a dict
inscription_prepare_files_transfer_v1_request_from_dict = InscriptionPrepareFilesTransferV1Request.from_dict(inscription_prepare_files_transfer_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


