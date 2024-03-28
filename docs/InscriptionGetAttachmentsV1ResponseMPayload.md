# InscriptionGetAttachmentsV1ResponseMPayload

Response for GET /1/object/inscription/{pkiInscriptionID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_attachments_v1_response_m_payload import InscriptionGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetAttachmentsV1ResponseMPayload from a JSON string
inscription_get_attachments_v1_response_m_payload_instance = InscriptionGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
inscription_get_attachments_v1_response_m_payload_dict = inscription_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionGetAttachmentsV1ResponseMPayload from a dict
inscription_get_attachments_v1_response_m_payload_form_dict = inscription_get_attachments_v1_response_m_payload.from_dict(inscription_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


