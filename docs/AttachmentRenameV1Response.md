# AttachmentRenameV1Response

Response for POST /1/object/attachment/{pkiAttachmentID}/rename

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AttachmentRenameV1ResponseMPayload**](AttachmentRenameV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_rename_v1_response import AttachmentRenameV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRenameV1Response from a JSON string
attachment_rename_v1_response_instance = AttachmentRenameV1Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentRenameV1Response.to_json())

# convert the object into a dict
attachment_rename_v1_response_dict = attachment_rename_v1_response_instance.to_dict()
# create an instance of AttachmentRenameV1Response from a dict
attachment_rename_v1_response_from_dict = AttachmentRenameV1Response.from_dict(attachment_rename_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


