# AttachmentSetDocumentTypeV1ResponseMPayload

Response for POST /1/object/attachment/{pkiAttachmentID}/setDocumentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_attachment_id** | **int** | The unique ID of the Attachment. | 

## Example

```python
from eZmaxApi.models.attachment_set_document_type_v1_response_m_payload import AttachmentSetDocumentTypeV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSetDocumentTypeV1ResponseMPayload from a JSON string
attachment_set_document_type_v1_response_m_payload_instance = AttachmentSetDocumentTypeV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachmentSetDocumentTypeV1ResponseMPayload.to_json())

# convert the object into a dict
attachment_set_document_type_v1_response_m_payload_dict = attachment_set_document_type_v1_response_m_payload_instance.to_dict()
# create an instance of AttachmentSetDocumentTypeV1ResponseMPayload from a dict
attachment_set_document_type_v1_response_m_payload_from_dict = AttachmentSetDocumentTypeV1ResponseMPayload.from_dict(attachment_set_document_type_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


