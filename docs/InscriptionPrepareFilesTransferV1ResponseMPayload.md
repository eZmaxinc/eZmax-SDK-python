# InscriptionPrepareFilesTransferV1ResponseMPayload

Payload for POST /1/object/inscription/{pkiInscriptionID}/prepareFilesTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**CustomAttachmentPrepareFilesTransferResponse**](CustomAttachmentPrepareFilesTransferResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_prepare_files_transfer_v1_response_m_payload import InscriptionPrepareFilesTransferV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionPrepareFilesTransferV1ResponseMPayload from a JSON string
inscription_prepare_files_transfer_v1_response_m_payload_instance = InscriptionPrepareFilesTransferV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionPrepareFilesTransferV1ResponseMPayload.to_json())

# convert the object into a dict
inscription_prepare_files_transfer_v1_response_m_payload_dict = inscription_prepare_files_transfer_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionPrepareFilesTransferV1ResponseMPayload from a dict
inscription_prepare_files_transfer_v1_response_m_payload_from_dict = InscriptionPrepareFilesTransferV1ResponseMPayload.from_dict(inscription_prepare_files_transfer_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


