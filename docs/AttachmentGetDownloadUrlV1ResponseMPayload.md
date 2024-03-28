# AttachmentGetDownloadUrlV1ResponseMPayload

Payload for GET /1/object/attachment/{pkiAttachmentID}/getDownloadUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_download_url** | **str** | The Url to the requested attachment.  Url will expire after 5 minutes. | 

## Example

```python
from eZmaxApi.models.attachment_get_download_url_v1_response_m_payload import AttachmentGetDownloadUrlV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentGetDownloadUrlV1ResponseMPayload from a JSON string
attachment_get_download_url_v1_response_m_payload_instance = AttachmentGetDownloadUrlV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachmentGetDownloadUrlV1ResponseMPayload.to_json())

# convert the object into a dict
attachment_get_download_url_v1_response_m_payload_dict = attachment_get_download_url_v1_response_m_payload_instance.to_dict()
# create an instance of AttachmentGetDownloadUrlV1ResponseMPayload from a dict
attachment_get_download_url_v1_response_m_payload_form_dict = attachment_get_download_url_v1_response_m_payload.from_dict(attachment_get_download_url_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


