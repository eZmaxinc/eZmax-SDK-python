# AttachmentDownloadV1Response

Response for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/send

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.attachment_download_v1_response import AttachmentDownloadV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentDownloadV1Response from a JSON string
attachment_download_v1_response_instance = AttachmentDownloadV1Response.from_json(json)
# print the JSON string representation of the object
print AttachmentDownloadV1Response.to_json()

# convert the object into a dict
attachment_download_v1_response_dict = attachment_download_v1_response_instance.to_dict()
# create an instance of AttachmentDownloadV1Response from a dict
attachment_download_v1_response_form_dict = attachment_download_v1_response.from_dict(attachment_download_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


