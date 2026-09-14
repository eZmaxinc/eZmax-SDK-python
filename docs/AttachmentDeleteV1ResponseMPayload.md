# AttachmentDeleteV1ResponseMPayload

Response for POST /1/object/attachment/{pkiAttachmentID}/delete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_attachment_id** | **int** | The unique ID of the Attachment. | 

## Example

```python
from eZmaxApi.models.attachment_delete_v1_response_m_payload import AttachmentDeleteV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentDeleteV1ResponseMPayload from a JSON string
attachment_delete_v1_response_m_payload_instance = AttachmentDeleteV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachmentDeleteV1ResponseMPayload.to_json())

# convert the object into a dict
attachment_delete_v1_response_m_payload_dict = attachment_delete_v1_response_m_payload_instance.to_dict()
# create an instance of AttachmentDeleteV1ResponseMPayload from a dict
attachment_delete_v1_response_m_payload_from_dict = AttachmentDeleteV1ResponseMPayload.from_dict(attachment_delete_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


