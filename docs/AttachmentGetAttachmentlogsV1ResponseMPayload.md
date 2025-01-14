# AttachmentGetAttachmentlogsV1ResponseMPayload

Response for GET /1/object/attachment/{pkiAttachmentID}/getAttachmentlogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentlog** | [**List[AttachmentlogResponseCompound]**](AttachmentlogResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_get_attachmentlogs_v1_response_m_payload import AttachmentGetAttachmentlogsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentGetAttachmentlogsV1ResponseMPayload from a JSON string
attachment_get_attachmentlogs_v1_response_m_payload_instance = AttachmentGetAttachmentlogsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachmentGetAttachmentlogsV1ResponseMPayload.to_json())

# convert the object into a dict
attachment_get_attachmentlogs_v1_response_m_payload_dict = attachment_get_attachmentlogs_v1_response_m_payload_instance.to_dict()
# create an instance of AttachmentGetAttachmentlogsV1ResponseMPayload from a dict
attachment_get_attachmentlogs_v1_response_m_payload_from_dict = AttachmentGetAttachmentlogsV1ResponseMPayload.from_dict(attachment_get_attachmentlogs_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


