# InscriptionPrepareFilesTransferV1Response

Response for POST /1/object/inscription/{pkiInscriptionID}/prepareFilesTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionPrepareFilesTransferV1ResponseMPayload**](InscriptionPrepareFilesTransferV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_prepare_files_transfer_v1_response import InscriptionPrepareFilesTransferV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionPrepareFilesTransferV1Response from a JSON string
inscription_prepare_files_transfer_v1_response_instance = InscriptionPrepareFilesTransferV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionPrepareFilesTransferV1Response.to_json())

# convert the object into a dict
inscription_prepare_files_transfer_v1_response_dict = inscription_prepare_files_transfer_v1_response_instance.to_dict()
# create an instance of InscriptionPrepareFilesTransferV1Response from a dict
inscription_prepare_files_transfer_v1_response_from_dict = InscriptionPrepareFilesTransferV1Response.from_dict(inscription_prepare_files_transfer_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


