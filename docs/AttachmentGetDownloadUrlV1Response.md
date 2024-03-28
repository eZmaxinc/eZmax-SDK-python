# AttachmentGetDownloadUrlV1Response

Response for GET /1/object/attachment/{pkiAttachmentID}/getDownloadUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AttachmentGetDownloadUrlV1ResponseMPayload**](AttachmentGetDownloadUrlV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_get_download_url_v1_response import AttachmentGetDownloadUrlV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentGetDownloadUrlV1Response from a JSON string
attachment_get_download_url_v1_response_instance = AttachmentGetDownloadUrlV1Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentGetDownloadUrlV1Response.to_json())

# convert the object into a dict
attachment_get_download_url_v1_response_dict = attachment_get_download_url_v1_response_instance.to_dict()
# create an instance of AttachmentGetDownloadUrlV1Response from a dict
attachment_get_download_url_v1_response_form_dict = attachment_get_download_url_v1_response.from_dict(attachment_get_download_url_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


