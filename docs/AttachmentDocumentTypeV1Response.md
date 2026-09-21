# AttachmentDocumentTypeV1Response

Response for POST /1/object/attachment/{pkiAttachmentID}/documentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AttachmentDocumentTypeV1ResponseMPayload**](AttachmentDocumentTypeV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_document_type_v1_response import AttachmentDocumentTypeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentDocumentTypeV1Response from a JSON string
attachment_document_type_v1_response_instance = AttachmentDocumentTypeV1Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentDocumentTypeV1Response.to_json())

# convert the object into a dict
attachment_document_type_v1_response_dict = attachment_document_type_v1_response_instance.to_dict()
# create an instance of AttachmentDocumentTypeV1Response from a dict
attachment_document_type_v1_response_from_dict = AttachmentDocumentTypeV1Response.from_dict(attachment_document_type_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


