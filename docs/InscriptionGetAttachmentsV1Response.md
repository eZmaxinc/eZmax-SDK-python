# InscriptionGetAttachmentsV1Response

Response for GET /1/object/inscription/{pkiInscriptionID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionGetAttachmentsV1ResponseMPayload**](InscriptionGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_attachments_v1_response import InscriptionGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetAttachmentsV1Response from a JSON string
inscription_get_attachments_v1_response_instance = InscriptionGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetAttachmentsV1Response.to_json())

# convert the object into a dict
inscription_get_attachments_v1_response_dict = inscription_get_attachments_v1_response_instance.to_dict()
# create an instance of InscriptionGetAttachmentsV1Response from a dict
inscription_get_attachments_v1_response_from_dict = InscriptionGetAttachmentsV1Response.from_dict(inscription_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


