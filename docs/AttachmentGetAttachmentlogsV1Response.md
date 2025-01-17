# AttachmentGetAttachmentlogsV1Response

Response for GET /1/object/attachment/{pkiAttachmentID}/getAttachmentlogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**AttachmentGetAttachmentlogsV1ResponseMPayload**](AttachmentGetAttachmentlogsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_get_attachmentlogs_v1_response import AttachmentGetAttachmentlogsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentGetAttachmentlogsV1Response from a JSON string
attachment_get_attachmentlogs_v1_response_instance = AttachmentGetAttachmentlogsV1Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentGetAttachmentlogsV1Response.to_json())

# convert the object into a dict
attachment_get_attachmentlogs_v1_response_dict = attachment_get_attachmentlogs_v1_response_instance.to_dict()
# create an instance of AttachmentGetAttachmentlogsV1Response from a dict
attachment_get_attachmentlogs_v1_response_from_dict = AttachmentGetAttachmentlogsV1Response.from_dict(attachment_get_attachmentlogs_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


