# AttachmentPrivacyV1Response

Response for POST /1/object/attachment/{pkiAttachmentID}/privacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AttachmentPrivacyV1ResponseMPayload**](AttachmentPrivacyV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_privacy_v1_response import AttachmentPrivacyV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentPrivacyV1Response from a JSON string
attachment_privacy_v1_response_instance = AttachmentPrivacyV1Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentPrivacyV1Response.to_json())

# convert the object into a dict
attachment_privacy_v1_response_dict = attachment_privacy_v1_response_instance.to_dict()
# create an instance of AttachmentPrivacyV1Response from a dict
attachment_privacy_v1_response_from_dict = AttachmentPrivacyV1Response.from_dict(attachment_privacy_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


