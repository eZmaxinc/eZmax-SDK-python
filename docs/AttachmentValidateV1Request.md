# AttachmentValidateV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/validate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_attachmentrejectreason_id** | **int** | The unique ID of the Attachmentrejectreason | [optional] 
**e_attachment_verified** | [**FieldEAttachmentVerified**](FieldEAttachmentVerified.md) |  | 
**t_attachment_rejectioncomment** | **str** | The rejectioncomment of the Attachment | [optional] 
**a_s_notification_email_address** | **List[str]** | A list of email addresses to send a rejection notification to. | [optional] 
**t_notification_message** | **str** | The email body to send to the notification recipients. | [optional] 
**b_notification_include_attachment** | **bool** | Should a copy of the attachment be included in the email. | [optional] 

## Example

```python
from eZmaxApi.models.attachment_validate_v1_request import AttachmentValidateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentValidateV1Request from a JSON string
attachment_validate_v1_request_instance = AttachmentValidateV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentValidateV1Request.to_json())

# convert the object into a dict
attachment_validate_v1_request_dict = attachment_validate_v1_request_instance.to_dict()
# create an instance of AttachmentValidateV1Request from a dict
attachment_validate_v1_request_from_dict = AttachmentValidateV1Request.from_dict(attachment_validate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


